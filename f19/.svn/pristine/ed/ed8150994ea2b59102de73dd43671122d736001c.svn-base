# This semester's configuration
include ../misc/inc/edition.mk

# Common definitions that rarely need to be changed
include ../misc/inc/config.mk

FILE:=main
# 00-overview does not have a handout
LECTURES:=`find * -maxdepth 1 -name "??-*" -type d | grep -v 00-overview | grep -v 22-tries`

### What not to interpret as files
.PHONY: help

### Print help message
help:
	@echo "make [help]            -- print these instructions"
	@echo "make pdf       [lec=xyz] -- compile every [only xyz] lecture"
	@echo "make view      [lec=xyz] -- view every [only xyz] lecture"
	@echo "make install   [lec=xyz] -- publish lecture xyz on web site"
	@echo "make meta      [lec=xyz] -- compile annotations for every [only xyz] lecture"
	@echo "make view-meta [lec=xyz] -- view annotations for every [only xyz] lecture"
	@echo "make xml       [lec=xyz] -- generate XML of every [only xyz] lecture"
#	@echo "make cleantmp   [lec=xyz] -- remove temporary files"
	@echo "make clean     [lec=xyz] -- remove pdf's as well"
	@echo ""


## $(call NUM,$(lec)) returns the number nn associated with a lecture
## directory nn-label
define NUM
echo `echo $1 | cut -c 1-2`
endef


## $(call LABEL,$(lec)) returns the descriptor label associated with
## a lecture directory nn-label
define LABEL
echo `echo $1 | cut -c 4-`
endef

######################################################################
## BEGIN: PDF
######################################################################
### What not to interpret as files
.PHONY: pdf view meta view-meta

### Compile an individual lecture or all lectures
ifeq ($(lec),)
pdf:
	@for l in $(LECTURES) ; do        \
	  if [ -f $$l/main.tex ]; then    \
	    echo $$l;                     \
	    make pdf lec=$$l > /dev/null; \
	  fi;                             \
	done
	@echo ""
else
pdf: $(lec)/$(FILE).tex
	@cd $(lec)              &&  \
	   $(PDFLATEX) --jobname="$(FILE)" '\input{../inc/old.tex}\input{$(FILE)}\end{document}'  &&  \
	   $(PDFLATEX) --jobname="$(FILE)" '\input{../inc/old.tex}\input{$(FILE)}\end{document}'
#	   $(PDFLATEX) $(FILE)  &&  \
#	   $(PDFLATEX) $(FILE)
	@$(call CLEAN,$(lec)/$(FILE),$(DEL))
	@mv $(lec)/$(FILE).pdf $(lec).pdf
endif

### Direct compilation
$(lec).pdf:
	if [ ! -f $(lec).pdf ]; then \
	  make pdf lec=$(lec);       \
	fi;

### View an individual pdf
ifneq ($(lec),)
view: pdf
	@$(PDF_VIEWER) $(lec).pdf &
else
view:
	@for l in $(LECTURES) ; do             \
	    make -s view lec=$$l > /dev/null;  \
	done
endif

### Compile a lecture with annotations
ifeq ($(lec),)
meta:
	@for l in $(LECTURES) ; do         \
	  if [ -f $$l/main.tex ]; then     \
	    echo $$l;                      \
	    make meta lec=$$l > /dev/null; \
	  fi;                              \
	done
	@echo ""
else
meta: $(lec)/$(FILE).tex
	@cd $(lec)              &&  \
	   $(PDFLATEX) --jobname="$(FILE)-meta" '\newcommand{\ismeta}{true}\input{../inc/old.tex}\input{$(FILE)}\end{document}' && \
	   $(PDFLATEX) --jobname="$(FILE)-meta" '\newcommand{\ismeta}{true}\input{../inc/old.tex}\input{$(FILE)}\end{document}'
	@$(call CLEAN,$(lec)/$(FILE)-meta,$(DEL))
	@mv $(lec)/$(FILE)-meta.pdf $(lec)-meta.pdf
endif

### View a lecture with annotations
ifneq ($(lec),)
view-meta: meta
	@$(PDF_VIEWER) $(lec)-meta.pdf &
else
view-meta:
	@for l in $(LECTURES) ; do                  \
	    make -s view-meta lec=$$l > /dev/null;  \
	done
endif

######################################################################
## END: PDF
######################################################################

######################################################################
## BEGIN: XML
######################################################################
# textmlt executable
TEXMLT=/usr/local/share/diderot/texmlt
# textmlt executable -- debug version
TEXMLTDBG=/usr/local/share/diderot/texmlt.dbg
# textmlt executable with meta argument
TEX2XML = $(TEXMLT) -meta $(META)
TEX2XMLDBG = $(TEXMLTDBG) -meta $(META)

# Pandoc configuration directory
META=/usr/local/share/diderot/meta
# Project preamble
PREAMBLE = ./inc/preamble-mtl.tex

### What not to interpret as files
.PHONY: xml dpdf dview dmeta dview-meta

### Generate XML for an individual lecture or all lectures
ifeq ($(lec),)
xml:
	@for l in $(LECTURES) ; do        \
	  if [ -f $$l/main.tex ]; then    \
	    echo $$l;                     \
	    make xml lec=$$l > /dev/null; \
	  fi;                             \
	done
	@echo ""
else
xml: $(lec)/$(FILE).tex
	$(TEX2XML) -preamble $(PREAMBLE) $(lec)/diderot.tex
	@mv $(lec)/diderot.xml $(lec).xml
endif

### Generate XML for an individual lecture or all lectures -- debug mode
ifeq ($(lec),)
xmldbg:
	@for l in $(LECTURES) ; do        \
	  if [ -f $$l/main.tex ]; then    \
	    echo $$l;                     \
	    make xml lec=$$l > /dev/null; \
	  fi;                             \
	done
	@echo ""
else
xmldbg: $(lec)/$(FILE).tex
	$(TEX2XMLDBG) -preamble $(PREAMBLE) $(lec)/diderot.tex
	@mv $(lec)/diderot.xml $(lec).xml
endif


### Compile an individual lecture or all lectures
ifeq ($(lec),)
dpdf:
	@for l in $(LECTURES) ; do         \
	  if [ -f $$l/main.tex ]; then     \
	    echo $$l;                      \
	    make dpdf lec=$$l > /dev/null; \
	  fi;                              \
	done
	@echo ""
else
dpdf: $(lec)/$(FILE).tex
	@cd $(lec)              &&  \
	   $(PDFLATEX) --jobname="$(FILE)-diderot" '\input{../inc/new.tex}\input{diderot}\end{document}'  &&  \
	   $(PDFLATEX) --jobname="$(FILE)-diderot" '\input{../inc/new.tex}\input{diderot}\end{document}'
	@$(call CLEAN,$(lec)/$(FILE)-diderot,$(DEL))
	@mv $(lec)/$(FILE)-diderot.pdf $(lec)-diderot.pdf
endif


### View an individual pdf
ifneq ($(lec),)
dview: dpdf
	@$(PDF_VIEWER) $(lec)-diderot.pdf &
else
dview:
	@for l in $(LECTURES) ; do             \
	    make -s dview lec=$$l > /dev/null;  \
	done
endif


### Compile a lecture with annotations
ifeq ($(lec),)
dmeta:
	@for l in $(LECTURES) ; do         \
	  if [ -f $$l/main.tex ]; then     \
	    echo $$l;                      \
	    make dmeta lec=$$l > /dev/null; \
	  fi;                              \
	done
	@echo ""
else
dmeta: $(lec)/$(FILE).tex
	@cd $(lec)              &&  \
	   $(PDFLATEX) --jobname="$(FILE)-meta-diderot" '\newcommand{\ismeta}{true}\input{../inc/new.tex}\input{diderot}\end{document}' && \
	   $(PDFLATEX) --jobname="$(FILE)-meta-diderot" '\newcommand{\ismeta}{true}\input{../inc/new.tex}\input{diderot}\end{document}'
	@$(call CLEAN,$(lec)/$(FILE)-meta-diderot,$(DEL))
	@mv $(lec)/$(FILE)-meta-diderot.pdf $(lec)-meta-diderot.pdf
endif

### View a lecture with annotations
ifneq ($(lec),)
dview-meta: dmeta
	@$(PDF_VIEWER) $(lec)-meta-diderot.pdf &
else
dview-meta:
	@for l in $(LECTURES) ; do                  \
	    make -s dview-meta lec=$$l > /dev/null;  \
	done
endif

######################################################################
## END: XML
######################################################################


######################################################################
## BEGIN: misc
######################################################################
PDF_TARGET:=$(WWW_DIR)/handouts
CODE_TARGET:=$(WWW_DIR)/code

### What not to interpret as files
.PHONY: handout publish install cleantmp clean

### Handouts
ifeq ($(lec),)
handout:
	@for l in $(LECTURES) ; do            \
	  if [ -d $$l/code ]; then            \
	    echo $$l;                         \
	    make handout lec=$$l > /dev/null; \
	  fi;                                 \
	done
	@echo ""
else
handout:
	@if [ -d $(lec)/code ]; then             \
	  cd $(lec)                           && \
	  cp -a code $(lec)                   && \
	  rm -rf $(lec)/*template* $(lec)/OLD && \
	  tar cfz ../$(lec).tgz $(lec)        && \
	  rm -rf $(lec);                         \
	fi;
endif

### Publish an individual file
ifneq ($(lec),)
#publish: $(lec).pdf
num:=`echo $(lec) | cut -c 1-2`
publish: $(lec).pdf
	@if [ -f $(lec)/diderot.tex ]; then       \
	  make xml lec=$(lec);                    \
	  $(DIDEROT_CLI) book:lectures $(num) --xml $(lec).xml --xml_pdf $(lec).pdf --attach $(lec)/img/*.png; \
	else                                      \
	  $(DIDEROT_CLI) book:lectures $(num) --pdf $(lec).pdf; \
	fi;
	@mv $(lec).pdf $(PDF_TARGET)/
	@make handout lec=$(lec)
	@if [ -f $(lec).tgz ]; then      \
	  mv $(lec).tgz $(CODE_TARGET);  \
	fi;
	@make clean lec=$(lec)
else
publish:
	@for l in $(LECTURES) ; do                \
	    echo $$l;                             \
	    make -s publish lec=$$l > /dev/null;  \
	done
endif
install: publish

### Remove temporary files
cleantmp:
ifeq ($(lec),)
	@for l in $(LECTURES) ; do  \
	    make -s cleantmp lec=$$l;  \
	done
else
	@$(call CLEAN,$(lec),$(DEL))
	@$(call CLEAN,$(lec)-meta,$(DEL))
	@find . -name "*~" -exec rm {} \;
endif

### Remove temporary files and *.pdf
clean: cleantmp
ifeq ($(lec),)
	@for l in $(LECTURES) ; do  \
	    make -s clean lec=$$l;  \
	done
else
	@$(call CLEAN,$(lec),$(EXT_DEL))
	@$(call CLEAN,$(lec)-meta,$(EXT_DEL))
	@$(call CLEAN,$(lec)-diderot,$(EXT_DEL))
	@$(call CLEAN,$(lec)-meta-diderot,$(EXT_DEL))
endif

######################################################################
## END: misc
######################################################################
