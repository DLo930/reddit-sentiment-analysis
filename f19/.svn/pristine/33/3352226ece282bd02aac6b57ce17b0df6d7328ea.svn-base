# Files that comprise a solution
HANDIN_FILES=rope.c1 rope-test.c0

# Files that should end up in the handout *and* the tests
BOTH_FILES=hdict.c1

# Files and directories that should end up only in the handout (given to students)
HANDOUT_FILES=$(BOTH_FILES) README.txt \
  rope.c1

BUGS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/bug/*.c1))

# Internal files to be sent to the autograder 
TEST_FILES=$(BOTH_FILES) $(BUGS) grader.py \
  hdict-alt.c1 \
  makesomeropes.c0 \
  grade-isrope.c0 \
  grade-basic.c0 \
  grade-rec.c0 \
  grade-sub.c0 \
  grade-reduce.c0 \
  rope-sol-B.c1
