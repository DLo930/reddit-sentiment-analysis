### NOTE: run
#     make readme hw=images
#     make lab hw=images
# for this homework

### Configuration parameters:
# Pick color you use in remove-COLOR example
#COLOR=red
#COLOR=green
COLOR=blue

#V=rotate-mask
V=reflect-blur

# Autolab Lab directory corresponding to this homework [OBSOLETE]
LAB:=lab04


### There shouldn't be a need to change anything below this line
ifeq ($V,rotate-mask)
 VERSION=$(ROTATEMASK)
 HANDIN_FILES=imageutil.c0 rotate.c0 mask.c0 manipulate.c0 images-test.c0
else ifeq ($V,reflect-blur)
 VERSION=$(REFLECTBLUR)
 HANDIN_FILES=imageutil.c0 reflect.c0 blur.c0 manipulate.c0 images-test.c0
else
 $(error unknown assignment version $V)
endif


ROTATEMASK= rotate-main.c0 maskblur-main.c0 maskedge-main.c0 \
   images/carnegie-rotate.png \
   images/cmu-edge.png images/cmu-gaussian.png \
   sobelX.txt sobelY.txt \

REFLECTBLUR= reflect-main.c0 blur-main.c0 \
  images/carnegie-reflect.png \
  images/scs-blur-slightly.png images/scs-blur.png \

BUGGY_IMPLS=$(subst $(hw)/src/,,$(wildcard $(hw)/src/labtests/*.c0))



# Files that should end up in the handout *and* the tests
BOTH_FILES= $(VERSION)\
  images/g5.png \
  images/carnegie.png \
  images/scs.png \
  images/cmu.png \
  images/tinytestpattern.png \
  images/g5-remove-$(COLOR).png images/g5-remove-$(COLOR)-bug.png \
  blur-mask.txt blur-slightly-mask.txt blur-more-mask.txt \

# Files and directories that should end up only in the handout (given to students)
HANDOUT_SUBDIRS=images
HANDOUT_FILES=$(BOTH_FILES) README.txt \
  imageutil.c0 \
  remove-$(COLOR).c0 remove-$(COLOR)-main.c0 remove-$(COLOR)-test.c0 \
  manipulate-main.c0 \

# Internal files to be sent to the autograder
TEST_FILES=$(BOTH_FILES) $(BUGGY_IMPLS) \
  imageutil-test.c0 grader.py labgrader.py pixel-int.c0 \
  imageutil-sol.c0 \
  images/scs-rotate.png \
  rotate-test.c0 rotate-comp.c0 \
  mask1.txt images/carnegie-blur1.png images/g5-blur1.png \
  mask2.txt images/carnegie-blur2.png images/g5-blur2.png \
  mask3.txt images/carnegie-blur3.png images/g5-blur3.png \
  blur-test.c0 blur-comp.c0 \
  manipulate-test.c0 \
  reflect-comp.c0 reflect-test.c0 images/g5-reflect.png \
  mask-comp.c0 mask-test.c0 images/g5-edge.png images/carnegie-edge.png \

# Files used in generating src/README.txt, line by line:
## Header and start of file list
## File list starting 'Files that don't exist yet'
## File list starting 'Data'
## imagediff instructions
## Task version instructions
READMEFILES=\
  common1.txt $(COLOR)1.txt $(V)1.txt \
  common2.txt $(V)2.txt \
  common3.txt $(V)3.txt common4.txt $(COLOR)2.txt $(V)4.txt \
  $(COLOR)3.txt \
  $(V)5.txt

readme:
	@rm -f $(hw)/$(SRC_DIR)/README.txt
	@cd $(hw)/$(SRC_DIR)/README            && \
	   cat $(READMEFILES) > ../README.txt

lab: $(hw)/autograde.tar
	cd $(hw)                                              && \
	  mkdir -p         $(AUTOLAB_BASE)/$(LAB)             && \
	  cp labtests.yml  $(AUTOLAB_BASE)/$(LAB)/$(LAB).yml  && \
	  cp labtests.rb   $(AUTOLAB_BASE)/$(LAB)/$(LAB).rb   && \
	  cp autograde.tar $(AUTOLAB_BASE)/$(LAB)             && \
	  cat labgrade-Makefile autograde-Makefile > $(AUTOLAB_BASE)/$(LAB)/autograde-Makefile
