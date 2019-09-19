# Files that comprise a solution
HANDIN_FILES=speller.c0 speller-test.c0 analysis.c0

LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c0))
TEXTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/texts/*.txt))
CHECKWORD:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/checkword-*.c0))
MERGE:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/checkbetter-*.c0))

# Files that should end up in the handout *and* the tests
BOTH_FILES=$(LIB)

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib texts
HANDOUT_FILES=$(BOTH_FILES) README.txt \
  texts/dict.txt texts/small-dict.txt \
  texts/scott-tweet.txt texts/sloth.txt texts/shakespeare.txt \
  speller-awful.c0 echo.c0

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
  $(CHECKWORD) $(MERGE) \
  speller-grade.c0 $(TEXTS)

##TEXBUNDLE_FILES=
