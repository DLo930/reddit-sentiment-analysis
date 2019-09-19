# Files that comprise a solution
HANDIN_FILES=huffman.c

LIB_C:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c))
LIB_H:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.h))
DATA_ALL:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/*))
DATA_STU:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/free_coffee.*))      \
          $(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/free_coffeeNL.*))    \
          $(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/more_free_coffee.*)) \
          $(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/shakespeare.*))      \
          $(subst $(hw)/src/,,$(wildcard $(hw)/src/data/*/nobody.*))

# Files that should end up in the handout *and* the tests
BOTH_FILES=$(LIB_H) $(LIB_C)           \
           freqtable.h   freqtable.c   \
           htree.h       htree.c       \
           encode.h      encode.c      \
           bitpacking.h  bitpacking.c  \
           compress.h    compress.c    \
                         main.c


# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib data data/source data/freq data/htree data/binascii data/compressed
HANDOUT_FILES=$(BOTH_FILES) \
 README.txt   \
 test-htree.c \
 huffman.c    \
 Makefile     \
 $(DATA_STU)

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
  huffman-grade.c                  \
  our-huffman.c                    \
  our-test-htree.c                 \
  test-pack.c                      \
  huffman-rename2-ours.h           \
  huffman-rename2-theirs.h         \
  huffman-rename3-ours.h           \
  huffman-rename3-theirs.h         \
  huffman-rename4-ours.h           \
  huffman-rename4-theirs.h         \
  $(DATA_ALL)
