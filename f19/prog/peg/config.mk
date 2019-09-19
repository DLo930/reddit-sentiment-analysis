# Files that comprise a solution
HANDIN_FILES=peg-moves.c1 peg1.c1 peg2.c1

LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c1))
GRADE:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/grade/*.txt))

# Files that should end up in the handout *and* the tests
BOTH_FILES=$(LIB) german.txt english.txt french1.txt french2.txt french3.txt

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib
HANDOUT_FILES=$(BOTH_FILES) README.txt performance-debugging.txt \
 peg-moves.c1 peg1.c1 peg2.c1 \
 peg-main.c1 pegmark.c1

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) $(GRADE) grader.py moves-grade.c1 our-peg-moves.c1 \
  hash-grade.c1 peg-main.c1
