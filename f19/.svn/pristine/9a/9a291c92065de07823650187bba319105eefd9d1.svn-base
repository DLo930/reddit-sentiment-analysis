# This semester's configuration
include ../misc/inc/edition.mk

# Common definitions that rarely need to be changed
include ../misc/inc/config.mk

AUTOLAB_DIR:=$(AUTOLAB_BASE)/rec$(rec)
PDF_TARGET:=$(AUTOLAB_DIR)/rec$(rec).pdf
YML:=rec$(rec).yml
RB:=rec$(rec).rb
AUTOLAB_CONFIG:=misc/autolab/rec$(rec)

# All recitations
RECS:=`find . -maxdepth 1 -name "??.tex" | cut -f 2 -d '/' | cut -f 1 -d '.'`


### What not to interpret as files
.PHONY: help writeup pdf sol publish install view view-sol cleantmp clean refresh


### Print help message
help:
	@echo "make [help]            -- print these instructions"
	@echo "make pdf      [rec=NN] -- compile writeups [of recitation NN only]"
	@echo "make sol      [rec=NN] -- compile solutions [of recitation NN only]"
	@echo "make view     [rec=NN] -- view writeups [of recitation NN only]"
	@echo "make view-sol [rec=NN] -- view solutions [of recitation NN only]"
	@echo "make install  [rec=NN] -- publish rec NN on web site and Autorec"
#	@echo "make publish  [rec=NN] -- same as 'install'"
#	@echo "make cleantmp [rec=NN] -- remove temporary files"
	@echo "make clean    [rec=NN] -- remove pdf's as well"
	@echo "make refresh  [rec=NN] -- save Autolab configuration files"
	@echo ""

### Compile an individual file or all files
writeup:
ifeq ($(rec),)
	@for l in $(RECS) ; do                \
	    echo -n "$$l ";                   \
	    make writeup rec=$$l > /dev/null; \
	done
	@echo ""
else
	$(PDFLATEX) $(rec)
	@$(PDFLATEX) $(rec)
	@$(call CLEAN,$(rec),$(DEL))
	@find . -name "*~" -exec rm {} \;
endif
pdf: writeup

### Compile an individual solution file
sol:
ifeq ($(rec),)
	@for l in $(RECS) ; do            \
	    echo -n "$$l ";               \
	    make sol rec=$$l > /dev/null; \
	done
	@echo ""
else
	$(PDFLATEX) --jobname="$(rec)-sol" '\newcommand{\issolution}{true}\input{$(rec)}'
	@$(PDFLATEX) --jobname="$(rec)-sol" '\newcommand{\issolution}{true}\input{$(rec)}'
	@$(call CLEAN,$(rec)-sol,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif


### Create autolab directory if needed
autolab_dir:
ifneq ($(rec),)
	@if [ ! -e $(AUTOLAB_DIR) ]; then mkdir -p $(AUTOLAB_DIR) ; fi
	@if [ -e $(AUTOLAB_CONFIG)/$(YML) ];                \
	  then cp $(AUTOLAB_CONFIG)/$(YML) $(AUTOLAB_DIR) ; \
	  fi
	@if [ -e $(AUTOLAB_CONFIG)/$(RB) ];                 \
	  then cp $(AUTOLAB_CONFIG)/$(RB)  $(AUTOLAB_DIR) ; \
	  fi
endif

### Publish an individual file
ifneq ($(rec),)
#publish: writeup autolab_dir
#	@mv $(rec).pdf $(PDF_TARGET)
publish: writeup
	@$(DIDEROT_CLI) book:recitations $(rec) --pdf $(rec).pdf
else
publish:
	@for l in $(RECS) ; do                    \
	    echo -n "$$l ";                       \
	    make -s publish rec=$$l > /dev/null;  \
	done
	@echo "";
endif
install: publish

### View an individual pdf
ifneq ($(rec),)
view: writeup
	@$(PDF_VIEWER) $(rec).pdf &
else
view:
	@for l in $(RECS) ; do                 \
	    make -s view rec=$$l > /dev/null;  \
	done
endif

### View an individual solutions
ifneq ($(rec),)
view-sol: sol
	@$(PDF_VIEWER) $(rec)-sol.pdf &
else
view-sol:
	@for l in $(RECS) ; do                     \
	    make -s view-sol rec=$$l > /dev/null;  \
	done
endif


### Remove temporary files
cleantmp:
ifeq ($(rec),)
	@for l in $(RECS) ; do      \
	    make -s cleantmp rec=$$l;  \
	done
else
	@$(call CLEAN,$(rec),$(DEL))
	@$(call CLEAN,$(rec)-sol,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif

### Remove temporary files and *.pdf
clean: cleantmp
ifeq ($(rec),)
	@for l in $(RECS) ; do          \
	    make -s clean rec=$$l;  \
	done
else
	@$(call CLEAN,$(rec),$(EXT_DEL))
	@$(call CLEAN,$(rec)-sol,$(EXT_DEL))
endif

# Save Autolab configuration locally
refresh:
ifeq ($(rec),)
	@for l in $(RECS) ; do                \
	    make refresh rec=$$l > /dev/null; \
	done
else
	@cp $(AUTOLAB_DIR)/$(RB)  $(AUTOLAB_CONFIG)
	@cp $(AUTOLAB_DIR)/$(YML) $(AUTOLAB_CONFIG)
endif
