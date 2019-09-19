# Files that comprise a solution
HANDIN_FILES=scavhunt.c0 puzzle.c0

# Files that should end up in the handout *and* the tests
BOTH_FILES=scavhunt-main.c0

# Files and directories that should end up only in the handout (given to students)
HANDOUT_FILES=$(BOTH_FILES) scavhunt.c0 puzzle.c0 puzzle-test.c0
HANDOUT_SUBDIRS=

# Internal files to be sent to the autograder 
TEST_FILES=$(BOTH_FILES) grader.py testgreet.c0 scavhunt-test.c0 tutorial.c0 feedback.c0 puzzle-grade.c0
