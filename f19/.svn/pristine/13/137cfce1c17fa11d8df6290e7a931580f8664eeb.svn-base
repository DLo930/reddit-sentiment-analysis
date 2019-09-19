# Files that comprise a solution
HANDIN_FILES=doslingos.c0 doslingos-test.c0 \
  analysis.c0

LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c0))
TEXTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/texts/*.txt))
SEKRETTEXTS:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/texts/sekret/*.txt))
COUNTVOCAB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/countvocab-*.c0))
SORTBYFREQ:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/sortbyfreq-*.c0))

# Files that should end up in the handout *and* the tests
BOTH_FILES=$(LIB)

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib texts
HANDOUT_FILES=$(BOTH_FILES) README.txt texts/news_vocab_sorted.txt \
  texts/scott_tweet.txt texts/sonnets.txt texts/shakespeare.txt \
  doslingos-awful.c0 echo.c0

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
  $(COUNTVOCAB) $(SORTBYFREQ) \
  doslingos-cv-grade.c0 doslingos-sf-grade.c0 $(TEXTS) $(SEKRETTEXTS)

##TEXBUNDLE_FILES=
