# This semester's configuration
include ../misc/inc/edition.mk

# Common definitions that rarely need to be changed
include ../misc/inc/config.mk

# Where the writeup is
WRITEUP_DIR:=writeup
WRITEUP_SRC:=main
WRITEUP:=$(WRITEUP_DIR)/$(WRITEUP_SRC)
WRITEUP_PDF:=$(hw)-writeup.pdf

# List of all homeworks
HWS:=binheap     \
     bloom       \
     bloomtests  \
     c0vm        \
     c0vmcheck   \
     clac        \
     doslingos   \
     editor      \
     editorcheck \
     exp         \
     huffman     \
     images      \
     lightsout   \
     peg         \
     pixels      \
     queues      \
     ropes       \
     scavhunt    \
     speller     \
     strbuf      \
     tbuf
### Notes:
# - binomial is incomplete
# - parse is missing the writeup


ifeq ($(hw),scavhunt)
num:= 1
else
ifeq ($(hw),pixels)
num:=2
else
ifeq ($(hw),images)
num:=3
else
ifeq ($(hw),speller)
num:=4
else
ifeq ($(hw),doslingos)
num:=4
else
ifeq ($(hw),clac)
num:=5
else
ifeq ($(hw),exp)
num:=5
else
ifeq ($(hw),editor)
num:=6
else
ifeq ($(hw),tbuf)
num:=6
else
ifeq ($(hw),bloom)
num:=7
else
ifeq ($(hw),peg)
num:=8
else
ifeq ($(hw),ropes)
num:=8
else
ifeq ($(hw),strbuf)
num:=9
else
ifeq ($(hw),queues)
num:=9
else
ifeq ($(hw),huffman)
num:=10
else
ifeq ($(hw),lightsout)
num:=10
else
ifeq ($(hw),c0vm)
num:=11
else
num:=-1
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif
endif



# Autolab
AUTOLAB_DIR:=$(AUTOLAB_BASE)/$(hw)
GRADER:=gradeC0.py
SOL_DIR:=solution
SRC_DIR:=src
TEST_DIR:=test_env
HWGRADER:=$(SRC_DIR)/grader.py
HWGRADERBASE:=$(SRC_DIR)/grader-base.py
HANDOUT_DIR:=$(hw)-handout
HANDOUT:=$(hw)-handout.tgz
HANDIN:=handin.tgz
AUTOGRADER:=autograde.tar
AUTO_MAKE:=autograde-Makefile
YML:=$(hw).yml
RB:=$(hw).rb
HW_CONFIG:=config.mk
INC:=inc

# Public directory where to put a copy of handout
PUBDIR=$(WWW_DIR)/hw


### Print help message
help:
	@echo "make [help]              -- print these instructions"
	@echo "make init       hw=xyz   -- initialization of hw xyz (some hw only)"
	@echo "make pdf       [hw=xyz]  -- compile writeups [of hw xyz only]"
	@echo "make view      [hw=xyz]  -- view writeups [of hw xyz only]"
	@echo "make autofiles  hw=xyz   -- generate Autolab files for hw xyz"
	@echo "make test       hw=xyz   -- test locally autograder for hw xyz"
	@echo "make install    hw=xyz   -- Install autograder for hw xyz (number nn) on Autolab"
	@echo "make final      hw=xyz   -- finalization of hw xyz (some hw only)"
	@echo "make refresh    hw=xyz   -- save Autolab configuration for hw xyz"

	@echo "make meta      [hw=xyz]  -- compile annotated writeups [of hw xyz only]"
	@echo "make view-meta [hw=xyz]  -- view annotated writeups [of hw xyz only]"
#	@echo "make cleantmp  [hw=xyz]  -- remove temporary latex files [for hw xyz]"
	@echo "make clean     [hw=xyz]  -- remove temporary autolab files [for hw xyz]"
	@echo ""


### What not to interpret as files
.PHONY: help writeup pdf all cleantmp clean


### Produce the writeup for an individual file
ifeq ($(hw),)
writeup:
	@for h in $(HWS); do                  \
	    echo -n "$$h ";                   \
	    make writeup hw=$$h > /dev/null;  \
	done
	@echo ""
else
writeup: $(hw)/$(WRITEUP).tex
	@cd $(hw)/$(WRITEUP_DIR)                  && \
           $(PDFLATEX) $(WRITEUP_SRC)             && \
           $(PDFLATEX) $(WRITEUP_SRC) > /dev/null
	@cd $(hw)                                 && \
	  mv $(WRITEUP).pdf $(WRITEUP_PDF)        && \
	  $(call CLEAN,$(WRITEUP),$(DEL));
endif
pdf: writeup

### View an individual pdf
ifneq ($(hw),)
view: writeup
	@$(PDF_VIEWER) $(hw)/$(WRITEUP_PDF) &
else
view:
	@for l in $(HWS) ; do                  \
	    make -s view hw=$$l > /dev/null;  \
	done
endif

### Compile writeup with annotations
ifeq ($(hw),)
meta:
	@for h in $(HWS); do                  \
	    echo -n "$$h ";                   \
	    make meta hw=$$h > /dev/null;     \
	done
	@echo ""
else
meta: $(hw)/$(WRITEUP).tex
	@cd $(hw)/$(WRITEUP_DIR)                  && \
           $(PDFLATEX) --jobname="meta" '\PassOptionsToClass{answers}{exam}\input{$(WRITEUP_SRC)}'                          && \
           $(PDFLATEX) --jobname="meta" '\PassOptionsToClass{answers}{exam}\input{$(WRITEUP_SRC)}' > /dev/null              && \
	  mv meta.pdf ../../$(hw)-meta.pdf  && \
	  $(call CLEAN,meta,$(DEL));
endif

### View an individual annotated pdf
ifneq ($(hw),)
view-meta: meta
	@$(PDF_VIEWER) $(hw)-meta.pdf &
else
view-meta:
	@for l in $(HWS) ; do                       \
	    make -s view-meta hw=$$l > /dev/null;  \
	done
endif

### Remove temporary files
cleantmp:
ifeq ($(hw),)
	@for h in $(HWS); do            \
            make -s cleantmp hw=$$h;    \
	done
else
	@cd $(hw)                           && \
	  $(call CLEAN,$(WRITEUP),$(DEL))   && \
	  find . -name "*~" -exec rm {} \;
endif

### Remove temporary Autolab files and *.pdf
clean: cleantmp
ifeq ($(hw),)
	@for h in $(HWS); do      \
	   make -s clean hw=$$h;  \
	done
else
	@cd $(hw)                    && \
	  rm -f  $(WRITEUP_PDF)      && \
	  rm -rf $(HANDOUT_DIR)      && \
	  rm -f  $(HANDOUT)          && \
	  rm -f  $(AUTOGRADER)       && \
	  rm -f  $(HANDIN)           && \
	  rm -rf $(TEST_DIR)         && \
	  if [ -e $(HWGRADERBASE) ];    \
	  then rm -f $(HWGRADER);       \
	  fi
	@rm -f $(hw)-meta.pdf
endif

### Create Autolab files

# Import configuration for current homework
ifneq ($(hw),)
  include $(hw)/$(HW_CONFIG)
endif

.PHONY: $(hw)/$(HANDIN) $(hw)/$(HANDOUT) $(hw)/$(AUTOGRADER) $(hw)/$(TEST_DIR) $(hw)/test

ifneq ($(hw),)
autofiles: $(hw)/$(HANDOUT) $(hw)/$(AUTOGRADER)
else
autofiles: help
endif

# Handout for current hw
$(hw)/$(HANDOUT):
	@cd $(hw)                                           && \
	  rm -rf $(HANDOUT_DIR)                             && \
	  mkdir   $(HANDOUT_DIR)                            && \
	  for dir in $(HANDOUT_SUBDIRS); do                    \
	    mkdir -p $(HANDOUT_DIR)/$$dir;                     \
	  done                                              && \
	  for file in $(HANDOUT_FILES); do                     \
	    cp -p $(SRC_DIR)/$$file $(HANDOUT_DIR)/$$file;     \
	  done                                              && \
	  tar -cf - --warning=no-file-changed $(HANDOUT_DIR) | gzip -c > $(HANDOUT)
# The above is a workaround because the following fails for large files
#	  tar -czf $(HANDOUT) --warning=no-file-changed $(HANDOUT_DIR)

# Autograder
$(hw)/$(AUTOGRADER):
	@cd $(hw)                                                      && \
	  cp ../$(INC)/$(GRADER) $(SRC_DIR)                            && \
	  tar -C $(SRC_DIR) -cf $(AUTOGRADER) --warning=no-file-changed $(TEST_FILES) $(GRADER)  && \
	  rm $(SRC_DIR)/$(GRADER)

### Simulate autograder on solution directory

# Fake handin for testing
$(hw)/$(HANDIN):
	cd $(hw) && \
	  tar -h -C $(SOL_DIR) -czf $(HANDIN) $(HANDIN_FILES)

# Run autolab locally for current hw
ifneq ($(hw),)
test: $(hw)/$(AUTOGRADER) $(hw)/$(HANDIN)
	@cd $(hw)                                && \
	  rm -rf           $(TEST_DIR)           && \
	  mkdir            $(TEST_DIR)           && \
	  cp $(AUTO_MAKE)  $(TEST_DIR)/Makefile  && \
	  cp $(AUTOGRADER) $(TEST_DIR)           && \
	  cp $(HANDIN)     $(TEST_DIR)           && \
	  $(MAKE) -C       $(TEST_DIR)
else
test: help
endif

### Autolab installation and sync
.PHONY: autolab_dir install refresh

# Always update config files on refresh
autolab_dir:
ifneq ($(hw),)
	@if [ ! -e $(AUTOLAB_DIR) ]; then mkdir -p $(AUTOLAB_DIR) ; fi
	@cd $(hw)                   && \
	  cp $(YML) $(AUTOLAB_DIR)  && \
	  cp $(RB)  $(AUTOLAB_DIR)
endif

ALL_INSTALL_DEPS=$(hw)/$(AUTO_MAKE) $(hw)/$(AUTOGRADER)
REG_INSTALL_DEPS=autolab_dir $(hw)/$(RB) $(hw)/$(YML)

# Install Autolab files on Autolab and handouts in public directory
ifneq ($(hw),)
install: $(ALL_INSTALL_DEPS) $(REG_INSTALL_DEPS) autofiles writeup
	@cd $(hw)                           && \
	  cp $(AUTOGRADER)  $(AUTOLAB_DIR)  && \
	  cp $(AUTO_MAKE)   $(AUTOLAB_DIR)  && \
	  cp $(HANDOUT)     $(AUTOLAB_DIR)  && \
	  cp $(WRITEUP_PDF) $(AUTOLAB_DIR)  && \
	  cp $(HANDOUT)     $(PUBDIR)
	@$(DIDEROT_CLI) book:programming $(num) --pdf $(hw)/$(hw)-writeup.pdf
else
install: help
endif

# Save Autolab configuration locally
refresh:
ifneq ($(hw),)
	@cd $(hw)                     && \
	  cp $(AUTOLAB_DIR)/$(RB)  .  && \
	  cp $(AUTOLAB_DIR)/$(YML) .
else
refresh: help
endif
