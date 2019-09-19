# Files that comprise a solution
HANDIN_FILES=bitvector.c board-ht.c lightsout.c board-ht.h

LIB_C:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c))
LIB_H:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.h))
2x2_BOARDS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/boards/2x2-*.txt))
3x2_BOARDS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/boards/3x2-*.txt))
4x4_BOARDS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/boards/4x4-*.txt))
CHALLENGE_BOARDS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/boards/board*.txt))
ALL_BOARDS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/boards/*.txt))
BITVEC:=bitvector4.h bitvector5.h bitvector12.h bitvector25.h \
  bitvector32.h bitvector48.h bitvector-array.c bitvector-array.h

# Files that should end up in the handout *and* the tests
BOTH_FILES=$(LIB_C) $(LIB_H)

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib boards
HANDOUT_FILES=$(BOTH_FILES) $(2x2_BOARDS) $(3x2_BOARDS) $(4x4_BOARDS) \
  $(CHALLENGE_BOARDS) README.txt Makefile board-ht.h

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) $(ALL_BOARDS) $(BITVEC) grader.py loplayer.c \
  bitvector-grade.c board-ht-grade.c c0main.c bitarray-sol.c \
  bitarray-alt.c \
  board-ht-orig.h
