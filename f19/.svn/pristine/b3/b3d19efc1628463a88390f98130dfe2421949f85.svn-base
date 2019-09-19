# Files that comprise a solution
HANDIN_FILES=bloom-test.c0 bloom1.c0 bloom2.c0

# Files that should end up in the handout *and* the tests
BOTH_FILES=bloom-worst.c0 bloom-expensive.c0

# Files and directories that should end up only in the handout (given to students)
HANDOUT_FILES=$(BOTH_FILES) README.txt

BROKE_IMPLS=$(subst $(hw)/src/,,$(wildcard $(hw)/src/bloom-broke*.c0))
BAD_IMPLS=$(subst $(hw)/src/,,$(wildcard $(hw)/src/bloom-bad*.c0))
MEH_IMPLS=$(subst $(hw)/src/,,$(wildcard $(hw)/src/bloom-meh*.c0))
OK_IMPLS=$(subst $(hw)/src/,,$(wildcard $(hw)/src/bloom-ok*.c0))

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
  $(BROKE_IMPLS) $(BAD_IMPLS) $(MEH_IMPLS) $(OK_IMPLS) \
  bloom-grade.c0 bloom1-grade.c0 \
  hash-grade.c1 getset-grade.c0 bloom2-grade.c0

# Creating the grader for checkpoint/final submission
init:
	@cd $(hw)/$(SRC_DIR)                       && \
	  echo "UNOFFICIAL = True\n" > grader.py   && \
	  cat grader-base.py >> grader.py

hw_base:=$(subst tests,,$(hw))

final: init install
	@cd $(AUTOLAB_DIR)                             && \
	  mv $(hw)-writeup.pdf $(hw_base)-writeup.pdf  && \
	  mv $(hw)-handout.tgz $(hw_base)-handout.tgz
