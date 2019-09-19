### NOTE: run
#     make init hw=pixels
# for this homework

# Pick version of hw file tasks.c0
# OH = opacify+histogram; RZ=remove_red+count_zeroes; GS=remove_green+summarize
VARIANT=OH
#VARIANT=RZ
#VARIANT=GS


# Files that comprise a solution
HANDIN_FILES=pixel.c0 pixel-bad.c0 pixel-test.c0 tasks.c0

# Files that should end up in the handout *and* the tests
BOTH_FILES=tasks-test.c0

# Files and directories that should end up only in the handout (given to students)
HANDOUT_FILES=$(BOTH_FILES) README.txt pixel.c0 pixel-array.c0 tasks.c0 \

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) grader.py \
  pixel-grade.c0 \
  pixel-test-exploit.c0 pixel-test-failure.c0 \
  pixel-int.c0 pixel-alt-int.c0 pixel-alt-struct.c0 pixel-alt-string.c0 \
  pixel-bad1.c0 pixel-bad2.c0 pixel-bad3.c0 pixel-bad4.c0 \
  pixel-bad5.c0 pixel-bad6.c0 pixel-bad7.c0 pixel-bad8.c0 \
  pixel-bad9.c0 pixel-badA.c0 pixel-badB.c0 \
  quant-good.c0 \
  quant-bad1.c0 quant-bad2.c0 quant-bad3.c0 quant-bad4.c0 quant-bad5.c0 \
  tasks-unused.c0 \
  tasks-grade.c0

init:
	@cp -f $(hw)/$(SRC_DIR)/tasks-$(VARIANT).c0 $(hw)/$(SRC_DIR)/tasks.c0
	@cp -f $(hw)/$(SRC_DIR)/tasks-$(VARIANT)-test.c0 $(hw)/$(SRC_DIR)/tasks-test.c0
	@cp -f $(hw)/$(SRC_DIR)/tasks-$(VARIANT)-unused.c0 $(hw)/$(SRC_DIR)/tasks-unused.c0
	@cp -f $(hw)/$(SOL_DIR)/tasks-$(VARIANT).c0 $(hw)/$(SOL_DIR)/tasks.c0
