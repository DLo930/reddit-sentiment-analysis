# Files that comprise a solution
HANDIN_FILES=queue.c1 queue-use.c1 queue-test.c1 queue.c queue-test.c

# Files that should end up in the handout *and* the tests
BOTH_FILES=lib/contracts.h lib/xalloc.h lib/xalloc.c queue.h

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib
HANDOUT_FILES=$(BOTH_FILES) README.txt queue.c1 

# Internal files to be sent to the autograder 
TEST_FILES=$(BOTH_FILES) grader.py gradeutil.c1 queue-alt.c1 \
  grade-is_queue.c1 grade-constant.c1 grade-linear.c1 grade-generic.c1 \
  grade-use.c1 \
  grade-queue.c grade-free.c c0main.c
