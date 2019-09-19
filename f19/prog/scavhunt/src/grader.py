# HW1 [scavhunt] grader

from gradeC0 import *

#qatool = "Piazza"
qatool = "Diderot"

def test_handout(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": obtaining the handout code"
    hint =         "You need to get the starter file scavhunt.c0 and add\n" +\
        "*** the other functions there."
    if expect_success("testgreet", hint):
        return 2
    return 0

def test_tutorial(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": using the C0 Tutorial"
    if expect_success("tutorial",
                      "Contents of fact.c0 not included in scavhunt.c0"):
        return 2
    return 0

def test_afsimg(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": viewing an image on AFS"
    score = 0

    if expect_successes(["salute -d 0",
                         "salute -d 1",
                         "salute -d 2"],
                        "salute() doesn't return the right answers"):
        score = score+2

    if expect_aborts(["salute -d -1",
                      "salute -d 4"],
                     "salute() doesn't abort on invalid inputs"):
        score = score+2
    return score/2

def test_qatool(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": using " +qatool
    if expect_success("salute -d 3",
                      "salute(3) is incorrect, check "+qatool+" for the fix"):
        return 3
    return 0

def test_feedback(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": viewing Autolab feedback"
    hint =         "You're missing a function with no arguments that\n" +\
        "*** returns a string. Once you've completed the other portions of\n" +\
        "*** this assignment, you should be able to tell from the compiler\n" +\
        "*** error messages above what name this function should have.\n" +\
        "*** \n" +\
        "*** It is not important what string the function returns; any\n" +\
        "*** string will do."
    if expect_success("feedback", hint):
        return 4
    return 0

def test_puzzle(tasknum):
    print "="*50
    print "Task " +str(tasknum)+ ": string puzzles"
    score = 0
    if expect_success("puzzletest common_prefix_given",
                      "These are the unit tests given out with the assignment",
                      timeout = 60):
        score += 2
        if expect_success("puzzletest common_prefix_exhaustive",
                          "More systematic test cases for common_prefix",
                          timeout = 60):
            score += 2
    if expect_successes(["puzzletest non_repeating_character ab",
                         "puzzletest non_repeating_character abb",
                         "puzzletest non_repeating_character aab",
                         "puzzletest non_repeating_character acb",
                         "puzzletest non_repeating_character abbb",
                         "puzzletest non_repeating_character acbb",
                         "puzzletest non_repeating_character aabb",
                         "puzzletest non_repeating_character aacb",
                         "puzzletest non_repeating_character aaab",
                         "puzzletest non_repeating_character abbbb",
                         "puzzletest non_repeating_character acbbb",
                         "puzzletest non_repeating_character aabbb",
                         "puzzletest non_repeating_character aacbb",
                         "puzzletest non_repeating_character aaacb",
                         "puzzletest non_repeating_character aaaab"],
                        "The name of the failing test is a hint!",
                        timeout = 60):
        score += 5

    if expect_success("puzzletest same_start_end",
                      "These are the tests for same_start_end. There are lots of them",
                      timeout = 120):
        score += 5
    return min(score, 12)

def main():
    handout_score = test_handout(1)
    tutorial_score = test_tutorial(2)
    afsimg_score = test_afsimg(3)
    qatool_score = test_qatool(4)

    pre_feedback_score = handout_score + tutorial_score + afsimg_score + qatool_score
    if (9 == pre_feedback_score):
        feedback_score = test_feedback(5)
        print_score("Task 5: ", feedback_score, 4)
    else:
        print "="*50
        print "Task 5 will be enabled when other tasks are completed"
        feedback_score = 0
    puzzle_score = test_puzzle(6)

    print '='*50
    print_score("Task 1: ", handout_score,  2)
    print_score("Task 2: ", tutorial_score, 2)
    print_score("Task 3: ", afsimg_score,   2)
    print_score("Task 4: ", qatool_score,   3)
    if (9 == pre_feedback_score):
        print_score("Task 5: ", feedback_score, 4)
    else:
        print "Task 5: will be enabled when other tasks are completed"
    print_score("Task 6: ", puzzle_score,  12)


    print "\n*** FINISHED!"
    print "*** TOTAL SCORE: ",
    print handout_score + tutorial_score + qatool_score + \
        afsimg_score + feedback_score + puzzle_score

    print json.dumps({'scores': {'handout': handout_score,
                                 'tutorial': tutorial_score,
                                 'afsimg': afsimg_score,
                                 'qatool': qatool_score,
                                 'puzzle': puzzle_score,
                                 'feedback': feedback_score}})

if __name__ == "__main__":
    print "TESTING..."
    main()
