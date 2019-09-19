# Files that comprise a solution
HANDIN_FILES=tbuf.c0 editor.c0

# Files that should end up in the handout *and* the tests
BOTH_FILES=editor-test.c0 tbuf-test.c0 test-main.c0

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=
HANDOUT_FILES=$(BOTH_FILES) README.txt \
 tbuf.c0 editor.c0 lovas-E0.c0

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
 grade.c1 is_tbuf-grade.c1 tbuf-grade.c1 is_editor-grade.c1 editor-grade.c1 editor-updown-grade.c1
