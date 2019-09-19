# Files that comprise a solution
HANDIN_FILES=clac.c0 dict.c0 parse.c0 exp-defs.clac

ALTLIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib-alt/*.c0))
LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c0))

# Files that should end up in the handout *and* the tests
BOTH_FILES=

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib
HANDOUT_FILES=$(LIB) \
  dict.c0 dict-test.c0 clac-main.c0 clac-test.c0 exp-main.c0 exp-test.c0 \
  exp-defs.clac README.txt

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) $(ALTLIB) grader.py \
  clac-impl.c0 clac-grade.c0 \
  is_dict-grade.c0 dict-grade.c0 dict-sol.c0 \
  precstack-grade.c0 \
  parse-grade.c0
