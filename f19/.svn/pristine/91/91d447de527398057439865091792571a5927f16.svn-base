# This semester's configuration
include ../misc/inc/edition.mk

# Common definitions that rarely need to be changed
include ../misc/inc/config.mk


# Autolab
AUTOLAB_DIR:=$(AUTOLAB_BASE)/written$(hw)
PDF_TARGET:=$(AUTOLAB_DIR)/written-$(hw).pdf
YML:=written$(hw).yml
RB:=written$(hw).rb
AUTOLAB_COPY:=autolab/written$(hw)

HWS:=`find * -maxdepth 1 -name "??.tex" | cut -f 2 -d '/' | cut -f 1 -d '.'`


### What not to interpret as files
.PHONY: help writeup pdf cleantmp clean refresh


### Print help message
help:
	@echo "make [help]           -- print these instructions"
	@echo "make pdf      [hw=NN] -- compile writeups [of hw NN only]"
	@echo "make sol      [hw=NN] -- compile solutions [of hw NN only]"
	@echo "make view     [hw=NN] -- view writeups [of hw NN only]"
	@echo "make view-sol [hw=NN] -- view solutions [of hw NN only]"
	@echo "make install   hw=NN  -- publish hw NN.pdf on web site"
#	@echo "make publish   hw=NN  -- publish hw NN.pdf on web site"
#	@echo "make cleantmp [hw=NN] -- remove temporary files"
	@echo "make clean    [hw=NN] -- remove pdf's and rubrics as well"
	@echo "make refresh  [hw=NN] -- save Autolab configuration files"
	@echo ""

### Compile an individual file
ifeq ($(hw),)
writeup:
	@for h in $(HWS) ; do                 \
	    echo -n "$$h ";                   \
	    make writeup hw=$$h > /dev/null;  \
	done
	@echo ""
else
writeup: $(hw).tex
	$(PDFLATEX) $(hw)
	@$(PDFLATEX) $(hw)
	@$(call CLEAN,$(hw),$(DEL))
endif
pdf: writeup

### Compile an individual solution file
sol:
ifeq ($(hw),)
	@for h in $(HWS) ; do            \
	    echo -n "$$h ";              \
	    make sol hw=$$h > /dev/null; \
	done
	@echo ""
else
	$(PDFLATEX) --jobname="$(hw)-sol" '\PassOptionsToClass{answers}{exam}\input{$(hw)}'
	@$(PDFLATEX) --jobname="$(hw)-sol" '\PassOptionsToClass{answers}{exam}\input{$(hw)}'
	@$(call CLEAN,$(hw)-sol,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif

### Create autolab directory if needed
autolab_dir:
ifneq ($(hw),)
	@if [ ! -e $(AUTOLAB_DIR) ]; then mkdir -p $(AUTOLAB_DIR) ; fi
	@if [ -e $(AUTOLAB_COPY)/$(YML) ];                \
	  then cp $(AUTOLAB_COPY)/$(YML) $(AUTOLAB_DIR) ; \
	  fi
	@if [ -e $(AUTOLAB_COPY)/$(RB) ];                 \
	  then cp $(AUTOLAB_COPY)/$(RB)  $(AUTOLAB_DIR) ; \
	  fi
endif

### Publish an individual file
ifneq ($(hw),)
#publish: writeup autolab_dir
#	@cp $(hw).pdf $(PDF_TARGET)
publish: writeup
	@$(DIDEROT_CLI) book:writtens $(hw) --pdf $(hw).pdf
else
publish:
	@for l in $(HWS) ; do                    \
	    echo -n "$$l ";                      \
	    make -s publish hw=$$l > /dev/null;  \
	done
	@echo "";
endif
install: publish


### View an individual pdf
ifneq ($(hw),)
view: writeup
	@$(PDF_VIEWER) $(hw).pdf &
else
view:
	@for l in $(HWS) ; do                 \
	    make -s view hw=$$l > /dev/null;  \
	done
endif

### View an individual solution
ifneq ($(hw),)
view-sol: sol
	@$(PDF_VIEWER) $(hw)-sol.pdf &
else
view-sol:
	@for l in $(HWS) ; do                     \
	    make -s view-sol hw=$$l > /dev/null;  \
	done
endif

### Remove temporary files
cleantmp:
	@if [ ! -z $(hw) ];                   \
	then $(call CLEAN,$(hw),$(DEL));      \
	     $(call CLEAN,$(hw)-sol,$(DEL));  \
	else $(call CLEAN,*,$(DEL))           \
	fi
	@find . -name "*~" -exec rm {} \;

### Remove temporary files and *.pdf
clean: cleantmp
	@if [ ! -z $(hw) ];                       \
	then $(call CLEAN,$(hw),$(EXT_DEL));      \
	     $(call CLEAN,$(hw)-sol,$(EXT_DEL));  \
	else $(call CLEAN,*,$(EXT_DEL))           \
	fi

# Save Autolab configuration locally
refresh:
ifeq ($(hw),)
	@for h in $(HWS) ; do                \
	    make refresh hw=$$h > /dev/null; \
	done
else
	@cp $(AUTOLAB_DIR)/$(RB)  $(AUTOLAB_COPY)
	@cp $(AUTOLAB_DIR)/$(YML) $(AUTOLAB_COPY)
endif
