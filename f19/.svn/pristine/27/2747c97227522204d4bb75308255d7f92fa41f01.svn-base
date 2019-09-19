/******************************************************
 ********* Testing Infrastructure for Lab04 ***********
 ******************************************************
 *
 * The testing infrastructure compiles student code
 * against different implementations of unique_intersect
 *
 * Author: Alex Stanescu (astanescu@cmu.edu)
 */

#include <string.h>
#include <stdbool.h>
#include "csapp.h"
#define streq(a,b) (strcmp((a),(b))==0)

/******************************
 * Defines the point cut-offs *
 * (in number of incorrect    *
 * implementations caught)    *
 ******************************/
#define THREEPTS 18
#define TWOPTS 10

/*****************************
 * Various other definitions *
 * to make my life easier    *
 *****************************/
#define OBFUSCATI0N "xytu3qttpsl4k5w3r14szrg4jwx3uqx"
//#define TESTDIR "/afs/andrew/course/15/122/misc/lab-X/" //Production
#define TESTDIR "3fkx3fsiwj-3htzwxj36a36773rnxh3qfg403" //Production
#define OBFUSCATION "-m14fwj41tz4qttpnsl4fy4y4ymnx4xyzkk" //Confuse students :D
#define CIPHER_SIZE 5
//#define TESTDIR "./students/" //For testing
#define CC0 "/afs/andrew.cmu.edu/course/15/122/bin/cc0"
#define TESTLIB "testlib.c0"
#define SETTEST_DEFAULT "set-test.c0"
#define MAIN "main.c0"
#define NUMARGS 8
#define TIMEOUT 10 //seconds
#define MAXLINELEN 100

/********************
 * Function headers *
 ********************/
void sigchld_handler(int sig);
char* compile_file(struct dirent* entry, char *student);
bool test_file(char *fileloc, bool correct);
void print_annotation(char *error);

/*******************
 *   Global vars   *
 *******************/
volatile int pid;
volatile int pid2;
int status;
int status2;
char* set_test;
char *student_loc;

/**********************************
 * Defines a linked list of files *
 **********************************/
typedef struct linked_list_node node;
struct linked_list_node {
    char* file;
    bool correct;
    node* next;
};

/****************************
 * Prints out how this prog *
 * is meant to be used      *
 ****************************/
void usage() {
    printf("Usage:\n");
    printf("./check-test [-tsh]\n");
    printf("   -t <test_file>\n");
    printf("        Uses the specified test file rather than the defualt\n");
    printf("   -s <student>\n");
    printf("        Only tests the given student\n");
    printf("   -h\n");
    printf("        Prints this helpful message\n");
}

/*****************
 * Main function *
 *****************/
int main(int argc, char** argv) {
    /**************************************************************
     * Welcome to the world's jankiest argument handler....       *
     * TODO: Make it use established argument handling frameworks *
     **************************************************************/

    //Check for number of arguments - only 1, 2, 3 and 5 is allowed
    if(argc != 1 && argc != 2 && argc != 3 && argc != 5) {
        fprintf(stderr, "Incorrect number of arguments\n");
        usage();
        exit(1);
    }

    //If we only have two arguments, then the second
    //argument should be -h, and should print out the usage
    if(argc == 2 && streq(argv[1],"-h")) {
        usage();
        exit(0);
    } else if(argc == 2) {
        fprintf(stderr, "Incorrect usage of arguments\n");
        usage();
        exit(1);
    }

    //If we have at least 3 arguments, the first one should always be
    //-t or -s
    if(argc >= 3 && !streq(argv[1], "-t") && !streq(argv[1], "-s")) {
        fprintf(stderr, "Incorrect usage of arguments\n");
        usage();
        exit(1);
    }

    //If we have 5 arguments, the third should either be -t or -s (the
    //second and 4th should be the actual arguments)
    if(argc == 5 && !streq(argv[3], "-t") && !streq(argv[3], "-s")) {
        fprintf(stderr, "Incorrect usage of arguments\n");
        usage();
        exit(1);
    }

    //Set the appropriate test file. If we don't have -t passed in as an arg,
    //then we should use SETTEST_DEFAULT. Otherwise, we should use the
    //value passed in to our program
    if(argc == 1 || argc == 2 || (argc == 3 && !streq(argv[1], "-t"))) {
        set_test = SETTEST_DEFAULT;
    } else if(argc >= 3 && streq(argv[1], "-t")) {
        set_test = argv[2];
    } else if(argc == 5 && streq(argv[3], "-t")) {
        set_test = argv[4];
    }

    //If we were passed in a student (with -s), then set student
    //to that value. Otherwise we are testing all students, and we
    //indicate that with student != NULL
    char* student = NULL;
    if(argc >= 3 && streq(argv[1], "-s")) {
        student = argv[2];
    } else if(argc == 5 && streq(argv[3], "-s")) {
        student = argv[4];
    }
    char *never_used = OBFUSCATION;

    //Set the SIGCHLD Handler
    //This handler is called whenever the program
    //receives the SIGCHLD signal (i.e. a child has terminated)
    Signal(SIGCHLD, sigchld_handler);

    student_loc = calloc(sizeof(char), strlen(TESTDIR) + 1);
    for(int i = 0; i < strlen(TESTDIR); i++) {
        char old = TESTDIR[i];
        int old_val;
        if(old == '/') {
            old_val = 26;
        } else if (old == '-') {
            old_val = 27;
        } else if ('a' <= old && old <= 'z') {
            old_val = old - 'a';
        } else {
            old_val = 28 + (old - '0');
        }

        old_val -= CIPHER_SIZE;
        if(old_val < 0) old_val += 38;

        if(old_val == 26) {
            student_loc[i] = '/';
        } else if(old_val == 27) {
            student_loc[i] = '-';
        } else if (old_val <= 26) {
            student_loc[i] = 'a' + old_val;
        } else {
            student_loc[i] = '0' + old_val - 28;
        }
    }
    student_loc[strlen(TESTDIR)] = '\0';

    //Setup for compiling
    DIR* testfiles = Opendir(student_loc);
    struct dirent* entry;

    node* files = malloc(sizeof(node));
    node* curr = files;
    size_t num_files = 0;

    /********************
     * Compilation step *
     ********************/
    printf("-----------------Compiling--------------------\n");
    //While there are still things left in the directory,
    while((entry = Readdir(testfiles)) != NULL) {
        //Try to compile the file
        char* file = compile_file(entry, student);
        if(file != NULL) {
            //This means that the file was compiled
            //successfully
            curr->file = file;
            curr->next = calloc(sizeof(node), 1);
            size_t len = strlen(file);
            curr->correct = file[len - 1] == 'c';
            num_files++;
            curr = curr->next;
        }
        //If the file was not compiled, then just ignore it and move
        //on.
    }

    /****************
     * Testing Step *
     ****************/
    printf("-----------------Testing--------------------\n");

    //Go through every file, testing each and increment the
    //number of passes and failures as per the results.
    curr = files;
    size_t num_pass = 0, num_fail = 0;
    bool failed_correct = false;
    int i = 0;
    for(; i < num_files; i++) {
        bool correct = curr->correct;
        bool success = test_file(curr->file, curr->correct);

        if(correct && !success) {
            //We had a correct file and failed.. This is bad and we should
            //remember that
            failed_correct = true;
        }
        if(success) {
            num_pass++;
        } else {
            num_fail++;
        }
        curr = curr->next;
    }

    //Let the student know what their result was
    printf("----------------------------------------------------------------------------\n");
    printf("Tested %lu students, %lu students had no failed tests, %lu students had failed tests. ", num_files, num_pass, num_fail);
    if(failed_correct) {
        printf("(No credit to be awarded − your code fails students with correct code)\n");
    } else {
        if(num_fail >= THREEPTS) {
            printf("(Three Points to be awarded)\n");
        } else if(num_fail >= TWOPTS) {
            printf("(Two Points to be awarded)\n");
        } else {
            printf("(One Point to be awarded)\n");
        }
    }


    return 0;
}

/**
 * Tests a given file, returning whether the test passed or any test failed
 *
 * fileloc should be given as the name of the file
 * within the current directory and should follow the convention of having
 * the last two characters be _c or _i.
 *
 * correct should be whether the file is a correct implementation or not. This
 * should be functionally equivalent to just checking if the last two characters
 * of the fileloc are _c or _i.
 */
bool test_file(char *fileloc, bool correct) {
    /**
     * Step Zero: Setup signal handling (and specifically block SIGCHLD).
     * If you don't know what that means, trust that this is important to
     * prevent race conditions
     */
    sigset_t mask_child, prev;
    Sigemptyset(&mask_child);
    Sigaddset(&mask_child, SIGCHLD);
    Sigprocmask(SIG_BLOCK, &mask_child, &prev);
    char *never_used = OBFUSCATI0N;
    /**
     * First, let the student know what's going on. What are we testing? For optimal
     * immersion, we want to lop off the _c/_i from the file name (as to only be left
     * with the andrewID).
     */
    size_t filelen = strlen(fileloc);
    fileloc[filelen - 2] = '\0';
    char *correct_desc = correct ? "Correct Implementation" : "Incorrect Implementation";
    printf("\n******************************************************************\n\n");
    printf("Testing Student %s (%s)\n", fileloc, correct_desc);
    fileloc[filelen - 2] = '_';

    //Open up the log file with full permissions (creating it if necessary)
    size_t logfiledesc = Open("./temp.log", O_RDWR | O_CREAT, 0666);

    /**
     * Fork off (create) two new child processes. The first (whose process ID
     * is stored in exec_pid), will actually run the file, and the second
     * (whose process id is stored in wait_pid) just starts a timer so that
     * we can have a timeout
     */
    pid_t exec_pid, wait_pid;
    if((exec_pid = Fork()) == 0) {
        /*****************
         * CHILD PROCESS *
         *****************/
        Sigprocmask(SIG_SETMASK, &prev, NULL); //Restore mask

        /**
         * Redirect STDOUT (i.e. what printf uses) and
         * STDERR (error messages) to the logfile
         */
        Dup2(logfiledesc, STDOUT_FILENO);
        Dup2(logfiledesc, STDERR_FILENO);
        Close(logfiledesc);

        /**
         * Execute the file. The first argument is something like ./iliano_c,
         * and by convention, the second (last) argument is NULL
         */
        char *argv[2];
        argv[0] = fileloc;
        argv[1] = NULL;
        Execve(fileloc, argv, environ);
        //This child will never pass this point
    }

    if((wait_pid = Fork()) == 0) {
        /*****************
         * CHILD PROCESS *
         *****************/
        Sigprocmask(SIG_SETMASK, &prev, NULL); //Restore mask
        //zzzzzz
        sleep(TIMEOUT);
        exit(0);
        //This child will never pass this point
    }

    /******************
     * PARENT PROCESS *
     ******************/
    //We first wait for either the wait or the exec to complete
    pid = 0;
    pid2 = 0;
    while(pid != wait_pid && pid != exec_pid) {
        Sigsuspend(&prev);
    }

    bool success = false;
    if(pid == exec_pid || pid2 == exec_pid) {
        //Success! The execution completed before (or at the
        //same time as) the timeout.

        //Kill the timeout process if it hasn't already completed
        if(pid != wait_pid && pid2 != wait_pid) {
            Kill(wait_pid, SIGKILL);
        }

        //Open up the logfile using the standard C library for easier reading
        FILE *logfile = Fopen("./temp.log", "r");
        char buffer[MAXLINELEN];
        char buffer2[MAXLINELEN];

        //We didn't print anything out :(
        if(Fgets(buffer, MAXLINELEN, logfile) == NULL) {
            printf("No Tests!\n");
        }

        //Get the appropriate exit code (pid <=> status, pid2 <=> status2)
        int exit_code = (pid == exec_pid) ? status : status2;

        /**
         * Continue reading until we reach the end of the log file
         *
         * The double buffer basically allows us to be reading
         * one line ahead of what actually gets printed. This
         * then allows us to neglect printing the "0" or "1" that
         * C0 prints out. Furthermore, we are able to sanitize
         * any occurrence of the TESTDIR from the output of the program
         */
        while(Fgets(buffer2, MAXLINELEN, logfile) != NULL) {
            //Make sure that we don't have any instance of TESTDIR
            //in the printed output
            char *test;
            if((test = strstr(buffer, student_loc)) == NULL) {
                //TESTDIR not found :)
                printf("%s", buffer);
            } else {
                //TESTDIR found. Show everything before and after but nothing inbetween.
                //If the exit code is 134 (a requires or ensures annotation failed, then
                //print out the annotation for them)
                if(exit_code == 134) {
                    print_annotation(buffer);
                } else {
                    *test = '\0';
                    char *rest = test+strlen(student_loc);
                    printf("%s%s", buffer, rest);
                }
            }
            strncpy(buffer, buffer2, MAXLINELEN);
        }

        /**
         * If the buffer isn't the standard 0/1 we want to show it
         */
        if(buffer[0] != '0' && buffer[0] != '1') {
            //Make sure that we don't have any instance of TESTDIR
            //in the printed output
            char* test;
            if((test = strstr(buffer, student_loc)) == NULL) {
                //TESTDIR not found :)
                printf("%s", buffer);
            } else {
                //TESTDIR found. Show everything before and after but nothing inbetween.
                *test = '\0';
                char *rest = test+strlen(student_loc);
                printf("%s%s",buffer,rest);
            }
        }

        //For whatever reason, regardless of what you return in main (in C0),
        //C0 exits with status code 0, so only check the buffer in that case.
        //Otherwise, we failed (why else would we get a non-zero exit code)
        if(exit_code == 0) {
            success = (buffer[0] == '0');
        }
    } else {
        //Timeout :(
        printf("Testing Student Timed out. Test Failed\n");

        //Kill the execution process.. clearly we're in an infinite loop :(
        Kill(exec_pid, SIGKILL);
    }

    //If we have one process that was not already reaped, reap that process too
    if(pid2 == 0) {
        pid = 0;
        while(pid != wait_pid && pid != exec_pid) {
            Sigsuspend(&prev);
        }
    }

    //We want to remove the log so that we don't have to deal with
    //future tests printing out less than this test.
    int rm_pid;
    pid = 0;
    if((rm_pid = Fork()) == 0) {
        /*****************
         * CHILD PROCESS *
         *****************/
        Sigprocmask(SIG_SETMASK, &prev, NULL); //Restore the mask

        /**
         * Execute the remove. This would correspond to calling rm temp.log
         * in the terminal
         */
        char *argv[3];
        argv[0] = "/bin/rm";
        argv[1] = "./temp.log";
        argv[2] = NULL;
        Execve(argv[0], argv, environ);
        //Child process never passes this point
    }

    /******************
     * PARENT PROCESS *
     ******************/
    //Wait for the rm to complete
    while(pid != rm_pid) {
        Sigsuspend(&prev);
    }

    //We want to remove this file so as not to clutter up their folder.
    //The student can run individual student files anyways with -s
    //so they're not losing anything from it
    pid = 0;
    if((rm_pid = Fork()) == 0) {
        /*****************
         * CHILD PROCESS *
         *****************/
        Sigprocmask(SIG_SETMASK, &prev, NULL); //Restore the mask

        /**
         * Execute the remove. This would correspond to calling rm ./iliano_c
         * in the terminal (or something similar depending on the file)
         */
        char *argv[3];
        argv[0] = "/bin/rm";
        argv[1] = fileloc;
        argv[2] = NULL;
        Execve(argv[0], argv, environ);
        //Child process never passes this point
    }

    /******************
     * PARENT PROCESS *
     ******************/
    //Wait for the rm to complete
    while(pid != rm_pid) {
        Sigsuspend(&prev);
    }

    //Let the student know what happened.
    if(correct && success) {
        printf("Student code passed all tests (expected to pass)... Good!\n");
    } else if(correct && !success) {
        printf("Student code failed a test (expected to pass)\n");
    } else if(!correct && success) {
        printf("Student code passed all tests (expected to fail)\n");
    } else {
        printf("Student code failed a test (expected to fail)... Good!\n");
    }

    //Reset Masks
    Sigprocmask(SIG_SETMASK, &prev, NULL);

    return success;
}

/**
 * Compiles the file represented in entry, assuming that
 * the file is a valid c0 file. Returns NULL if there was no
 * file compiled, otherwise returns the name of the executable
 *
 * entry represents the entirety of the directory entry including
 * the name of the file and other (useless) information
 *
 * student represents the andrewID of the file that we are aiming to
 * test (or NULL if we are testing everything). This is only set to a
 * non-null thing if -s is passed in as a command-line argument
 */
char* compile_file(struct dirent* entry, char *student) {
    /**
     * First, Check if the file is an actual C0 file. We
     * do this by first getting the full name of the file
     * and then going through the file character by character
     * until we reach the "." in .c0, or we have reached the
     * end of the file. Then we check to see that the extension is
     * actually .c0. If so, we proceed
     */
    char* file = entry->d_name;
    char* extension = file;
    int name_length = 0;
    char *name = file;
    while(*extension != '.' && *extension != '\0') {
        name_length++;
        extension++;
        if(*extension == '/') {
            name = extension + 1;
        }
    }
    if(*extension == '\0' || extension[1] != 'c' || extension[2] != '0') {
        return NULL;
    }

    /**
     * Copy over the name of the file, so we can
     * have an independent reference to it
     */
    char *filename = calloc(sizeof(char), name_length + 1);
    strncpy(filename, file, name_length);
    filename[name_length] = '\0';

    /**
     * If we are searching for a particular student, check
     * that this student is that student before proceeding
     */
    if(student) {
        filename[name_length - 2] = '\0';
        if(!streq(student, filename)) {
            Free(filename);
            return NULL;
        }
        filename[name_length - 2] = '_';
    }

    /**
     * Setup the argument array for compiling this file.
     * Really could all just be done in the child process,
     * but putting it here makes everything feel less cluttered...
     * Functionally equivalent to typing
     * cc0 -d -o filename TESTLIB TESTDIR/file set_test MAIN
     * in the terminal, replacing the variables as necessary
     *
     * (e.g. cc0 -d -o iliano_c set_test.c0 TESTDIR/iliano_c.c0 set_test.c0 main.c0)
     */
    char* argv[NUMARGS + 1];
    argv[0] = CC0;
    argv[1] = "-d";
    argv[2] = "-o";
    argv[3] = filename;
    argv[4] = TESTLIB;
    argv[5] = Calloc(strlen(student_loc) + strlen(file) + 1, sizeof(char));
    strcat(argv[5], student_loc);
    strcat(argv[5], file);
    argv[6] = set_test;
    argv[7] = MAIN;
    argv[8] = NULL;

    //Block SIGCHLD to ensure no race conditions
    sigset_t mask_child, prev;
    Sigemptyset(&mask_child);
    Sigaddset(&mask_child, SIGCHLD);
    Sigprocmask(SIG_BLOCK, &mask_child, &prev);

    //Let the user know what's up
    printf("Compiling test %s...\n", name);

    //Compile!
    int childpid;
    if((childpid = Fork()) == 0) {
        /*****************
         * CHILD PROCESS *
         *****************/
        Sigprocmask(SIG_SETMASK, &prev, NULL); //Restore mask

        //We use manual error checking here just in order to have
        //a nicer error message.
        if(execve(argv[0], argv, environ) < 0) {
            fprintf(stderr, "cc0 error: %s\n", (strerror(errno)));
            exit(1);
        }
        //Child never reaches here.. Ever
    }

    /******************
     * PARENT PROCESS *
     ******************/
    //Wait for the compilation to complete
    pid = 0;
    while(pid != childpid) {
        Sigsuspend(&prev);
    }

    //Reset masks
    Sigprocmask(SIG_SETMASK, &prev, NULL);

    //If we have failed at compiling. Let the user know, and abort.
    //Otherwise continue forward soldier!
    if(WIFEXITED(status) && WEXITSTATUS(status) != 0) {
        printf("Compilation error. Aborting...\n");
        exit(1);
    } else {
        printf("Compilation Succeeded!\n");
    }
    return filename;
}

/**
 * SIGCHLD handler.
 * Whenever SIGCHLD is called, reap at most 2 child processes
 * (we can do this because we know there will never be more than 2
 * child processes running at once). Set their relevant pid and status
 * messages to (pid, status) and (pid2, status2)
 */
void sigchld_handler(int sig) {
    sigset_t mask_all, prev;
    Sigfillset(&mask_all);
    Sigprocmask(SIG_BLOCK, &mask_all, &prev);

    int olderrno = errno;
    pid = waitpid(-1, &status, WNOHANG);
    pid2 = waitpid(-1, &status2, WNOHANG);

    Sigprocmask(SIG_SETMASK, &prev, NULL);
    errno = olderrno;
    return;
}

/**
 * Prints out the requires or ensures that failed.
 *
 * Error is expected to bbe of the form student_loc/file.c0:ll.cc-ll.cc: @requires annotation failed
 */
void print_annotation(char *error) {
    //First, print out the error so that they know exactly what's up,
    //sanitizing the testdir from the output
    printf("%s", error + strlen(student_loc));

    char *l1 = strstr(error, ".c0") + 4; //The starting line

    char *c1 = strstr(l1, "."); //The starting column
    *c1 = '\0';
    c1++;

    char *l2 = strstr(c1, "-"); //The ending line
    *l2 = '\0';
    l2++;

    char *c2 = strstr(l2, "."); //The ending column
    *c2 = '\0';
    c2++;

    char* colon = strstr(c2, ":"); //The ending colon.
    *colon = '\0';

    //Convert them from strings to integers
    int start_ln = atoi(l1);
    int start_col = atoi(c1);
    int end_ln = atoi(l2);
    int end_col = atoi(c2);

    /*
     * We read from the file character by character, keeping track of our
     * position (line,column), and whenever we enter into the range
     * [(start_ln, start_col), (end_ln, end_col)], we print out the annotation
     */
    *(l1 - 1) = '\0'; //Cut off error at the end of the full file name
    FILE* f = Fopen(error, "r");
    int curr_ln = 1;
    int curr_col = 1;
    char curr_char;
    printf("\t => //@"); //Prettyness!
    while((curr_char = fgetc(f)) != EOF && curr_ln <= end_ln) {
        if(start_ln <= curr_ln && curr_ln <= end_ln) {
            //Common case: starting line is the same as ending line
            if(start_ln == end_ln && start_col <= curr_col && curr_col <= end_col) {
                printf("%c", curr_char);
            } else if(start_ln != end_ln) {
                //Uncommon case: different start and end-lines. Here we have three
                //sub-cases (first line, inbetween and last line).
                if(curr_ln == start_ln && start_col <= curr_col) {
                    printf("%c", curr_char);
                } else if(start_ln < curr_ln && curr_ln < end_ln) {
                    printf("%c", curr_char);
                } else if(curr_ln == end_ln && curr_col <= end_col) {
                    printf("%c", curr_char);
                }
            }
        }

        //Increment our position
        curr_col++;
        if(curr_char == '\n') {
            curr_ln++;
            curr_col = 1;
        }
    }

    Fclose(f);
}
