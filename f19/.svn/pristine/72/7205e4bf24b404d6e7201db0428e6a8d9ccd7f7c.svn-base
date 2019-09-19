# Files that comprise a solution
HANDIN_FILES=gapbuf.c0 dll_pt.c0 tbuf.c0

TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/*.c0))
GRADE:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/grade/*.txt))

# Files that should end up in the handout *and* the tests
BOTH_FILES=elem-char.c0

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=
HANDOUT_FILES=$(BOTH_FILES) README.txt \
 gapbuf.c0 gapbuf-test.c0 \
 dll_pt.c0 dll_pt-test.c0 \
 tbuf.c0 tbuf-test.c0 \
 lovas-E0.c0

# Internal files to be sent to the autograder 
TEST_FILES=$(BOTH_FILES) $(TESTS) $(GRADE) grader.py \
 gapbuf-mimic.c0 gapbuf-grade.c0 \
 dll_pt-mimic.c0 dll_pt-grade.c0 \
 tbuf-tools.c0 tbuf-grade.c0

# Creating the grader for checkpoint/final submission
init:
	@cd $(hw)/$(SRC_DIR)                        && \
	  echo "FINAL = True\n" > grader.py         && \
	  cat grader-base.py >> grader.py
