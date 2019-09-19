# NOTE: This makefile will not work without doing some work first, see
# README.txt.

# Files that comprise a solution
HANDIN_FILES=c0vm.c

TEST:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/*.c0))
LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c))
LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.h)) $(LIB)
TASK1_TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/task1/*.bc0))
TASK2_TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/task2/*.bc0))
TASK3_TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/task3/*.bc0))
TASK4_TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/task4/*.bc0))
TASK5_TESTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/tests/task5/*.bc0))

# Files that should end up in the handout *and* the tests
#BOTH_FILES=c0vm_main.c $(INC) $(TEST) $(LIB)
BOTH_FILES=c0vm_main.c $(TEST) $(LIB)

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib tests
HANDOUT_FILES=$(BOTH_FILES) Makefile C_IDIOMS.txt COMPILING.txt \
  PROG_HINTS.txt c0vm-ref.txt c0vm.c README.txt

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py cc0.tgz c0vm_alt_abort.c shutup \
 $(TASK1_TESTS) $(TASK2_TESTS) $(TASK3_TESTS) $(TASK4_TESTS) $(TASK5_TESTS)


# Creating the grader for checkpoint/final submission
init:
	@cd $(hw)/$(SRC_DIR)                        && \
	  echo "CHECKPOINT = True\n" > grader.py    && \
	  cat grader-base.py >> grader.py

hw_base:=$(subst check,,$(hw))

final: install
	@cd $(AUTOLAB_DIR)                             && \
	  mv $(hw)-writeup.pdf $(hw_base)-writeup.pdf  && \
	  mv $(hw)-handout.tgz $(hw_base)-handout.tgz


# Preparing cc0.tgz -- fragile
C0_INSTALL:=/usr/local/share

$(hw)/$(SRC_DIR)/cc0.tgz:
	cd $(hw)/$(SRC_DIR) && \
	  tar czvf cc0.tgz -C $(C0_INSTALL) cc0/lib cc0/include cc0/runtime

prepare: $(hw)/$(SRC_DIR)/cc0.tgz
