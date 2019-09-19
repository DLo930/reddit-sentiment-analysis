# Files that comprise a solution
HANDIN_FILES=clac.c0 log.clac

LIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib/*.c0))
ALTLIB:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/lib-alt/*.c0))
DEF:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/def/*.clac))
GRADE:=$(subst $(hw)/src/,,$(wildcard $(hw)/src/grade/*.clac))

# Files that should end up in the handout *and* the tests
BOTH_FILES=

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=lib def
HANDOUT_FILES=$(LIB) README.txt \
  clac.c0 clac-test.c0 clac-main.c0 \
  $(DEF)
#  dict.c0 \
#  def/demo-fail.clac def/demo-print.clac \

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) $(ALTLIB) $(GRADE) $(DEF) grader.py \
  demo-grade.c0 dict-grade.c0 clac-grade.c0 dict-modified.c0 \
  clac-ref-main.c0
