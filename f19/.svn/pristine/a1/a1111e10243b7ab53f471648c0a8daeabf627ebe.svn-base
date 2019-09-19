# This semester's configuration
include ../misc/inc/edition.mk

# Common definitions that rarely need to be changed
include ../misc/inc/config.mk


AUTOLAB_DIR:=$(AUTOLAB_BASE)/lab$(lab)
PDF_TARGET:=$(AUTOLAB_DIR)/lab$(lab).pdf
AFS_BASE:=/afs/andrew.cmu.edu/course/15/122/misc
CFG_FILE:=questions/CONFIG/config-$(lab).mk
### If there is a configuration file for this lab, load it
ifneq ($(wildcard $(CFG_FILE)),)
include $(CFG_FILE)
endif
LAB_PATH:=questions/$(LAB_DIR)
AFS_PATH:=$(AFS_BASE)/lab$(lab)
HANDOUT_DIR:=handout
HANDOUT_TGT:=handout-$(lab).tgz
YML:=lab$(lab).yml
RB:=lab$(lab).rb
AUTOLAB_CONFIG:=misc/autolab/lab$(lab)

# All labs
LABS:=`find * -maxdepth 1 -name "??.tex" | cut -f 2 -d '/' | cut -f 1 -d '.'`

### What not to interpret as files
.PHONY: help writeup pdf sol publish install view view-sol cleantmp clean refresh


### Print help message
help:
	@echo "make [help]            -- print these instructions"
	@echo "make pdf      [lab=NN] -- compile writeups [of lab NN only]"
	@echo "make sol      [lab=NN] -- compile solutions [of lab NN only]"
	@echo "make view     [lab=NN] -- view writeups [of lab NN only]"
	@echo "make view-sol [lab=NN] -- view solutions [of lab NN only]"
	@echo "make install  [lab=NN] -- publish lab NN on web site and Autolab"
#	@echo "make publish  [lab=NN] -- publish lab NN on web site and Autolab"
#	@echo "make install  [lab=NN] -- same as 'publish'"
#	@echo "make cleantmp [lab=NN] -- remove temporary files"
	@echo "make clean    [lab=NN] -- remove pdf's as well"
	@echo "make refresh  [lab=NN] -- save Autolab configuration files"
	@echo ""

### Compile an individual file or all files
writeup:
ifeq ($(lab),)
	@for l in $(LABS) ; do                \
	    echo -n "$$l ";                   \
	    make writeup lab=$$l > /dev/null; \
	done
	@echo ""
else
	$(PDFLATEX) $(lab)
	@$(PDFLATEX) $(lab)
	@$(call CLEAN,$(lab),$(DEL))
	@find . -name "*~" -exec rm {} \;
endif
pdf: writeup

### Compile an individual solution file
sol:
ifeq ($(lab),)
	@for l in $(LABS) ; do            \
	    echo -n "$$l ";               \
	    make sol lab=$$l > /dev/null; \
	done
	@echo ""
else
	$(PDFLATEX) --jobname="$(lab)-sol" '\newcommand{\issolution}{true}\input{$(lab)}'
	@$(PDFLATEX) --jobname="$(lab)-sol" '\newcommand{\issolution}{true}\input{$(lab)}'
	@$(call CLEAN,$(lab)-sol,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif


### Create autolab directory if needed
autolab_dir:
ifneq ($(lab),)
	@if [ ! -e $(AUTOLAB_DIR) ]; then mkdir -p $(AUTOLAB_DIR) ; fi
	@if [ -e $(AUTOLAB_CONFIG)/$(YML) ];                \
	  then cp $(AUTOLAB_CONFIG)/$(YML) $(AUTOLAB_DIR) ; \
	  fi
	@if [ -e $(AUTOLAB_CONFIG)/$(RB) ];                 \
	  then cp $(AUTOLAB_CONFIG)/$(RB)  $(AUTOLAB_DIR) ; \
	  fi
endif

### Create handout if there is one
ifneq ($(lab),)
handout: autolab_dir
	@if [ -e $(LAB_PATH)/$(HANDOUT_DIR) ];                      \
	 then                                                       \
	   tar cz -C $(LAB_PATH) -f $(HANDOUT_TGT) $(HANDOUT_DIR) ; \
	   mv $(HANDOUT_TGT) $(AUTOLAB_DIR) ;                       \
	   rm -rf $(AFS_PATH) ;                                     \
	   cp -a $(LAB_PATH)/$(HANDOUT_DIR) $(AFS_PATH) ;           \
	fi
endif

### Publish one or all labs
ifneq ($(lab),)
publish: writeup autolab_dir handout
	@# Copy PDF
	@$(DIDEROT_CLI) book:labs $(lab) --pdf $(lab).pdf
	@mv $(lab).pdf $(PDF_TARGET)
else
publish:
	@for l in $(LABS) ; do                    \
	    echo -n "$$l ";                       \
	    make -s publish lab=$$l > /dev/null;  \
	done
	@echo "";
endif
install: publish

### View an individual pdf
ifneq ($(lab),)
view: writeup
	@$(PDF_VIEWER) $(lab).pdf &
else
view:
	@for l in $(LABS) ; do                 \
	    make -s view lab=$$l > /dev/null;  \
	done
endif

### View an individual solutions
ifneq ($(lab),)
view-sol: sol
	@$(PDF_VIEWER) $(lab)-sol.pdf &
else
view-sol:
	@for l in $(LABS) ; do                     \
	    make -s view-sol lab=$$l > /dev/null;  \
	done
endif

### Remove temporary files
cleantmp:
ifeq ($(lab),)
	@for l in $(LABS) ; do      \
	    make -s cleantmp lab=$$l;  \
	done
else
	@$(call CLEAN,$(lab),$(DEL))
	@$(call CLEAN,$(lab)-sol,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif

### Remove temporary files and *.pdf
clean: cleantmp
ifeq ($(lab),)
	@for l in $(LABS) ; do          \
	    make -s clean lab=$$l;  \
	done
else
	@rm -f $(HANDOUT_TGT)
	@$(call CLEAN,$(lab),$(EXT_DEL))
	@$(call CLEAN,$(lab)-sol,$(EXT_DEL))
endif

# Save Autolab configuration locally
refresh:
ifeq ($(lab),)
	@for l in $(LABS) ; do                \
	    make refresh lab=$$l > /dev/null; \
	done
else
	@cp $(AUTOLAB_DIR)/$(RB)  $(AUTOLAB_CONFIG)
	@cp $(AUTOLAB_DIR)/$(YML) $(AUTOLAB_CONFIG)
endif
