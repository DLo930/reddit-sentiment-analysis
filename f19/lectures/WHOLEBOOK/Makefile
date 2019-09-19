# Common definitions that rarely need to be changed
include ../../misc/inc/config.mk

### File extensions to delete
EXT_DEL1:=log out bbl blg toc
EXT_DEL2:=idx ilg ind lof maf mtc*
EXT_DEL_ALL:=aux $(EXT_DEL1) $(EXT_DEL2)
MAIN:=all


help:
	@echo "Usage:"
	@echo "  make all       : compiles everything"
	@echo "  make meta      : compiles everything with annotations"
	@echo "  make cleantmp  : removes temporary files"
	@echo "  make clean     : removes all generated files"
	@echo "  make help      : display this message"

all:
	pdflatex '\newcommand{\all}{}\input{$(MAIN)}'
	bibtex $(MAIN)
	makeindex $(MAIN)
	@pdflatex '\newcommand{\all}{}\input{$(MAIN)}'
	@pdflatex '\newcommand{\all}{}\input{$(MAIN)}'

run: $(arg)/main.tex
	pdflatex -jobname $(arg) '\newcommand{\all}{$(arg)/main}\input{$(MAIN)}'
	@$(call CLEAN,$(arg),$(EXT_DEL_ALL))

meta:
	pdflatex --jobname="meta" '\newcommand{\ismeta}{true}\newcommand{\all}{}\input{$(MAIN)}'
	bibtex meta
	makeindex meta
	@pdflatex --jobname="meta" '\newcommand{\ismeta}{true}\newcommand{\all}{}\input{$(MAIN)}'
	@pdflatex --jobname="meta" '\newcommand{\ismeta}{true}\newcommand{\all}{}\input{$(MAIN)}'

cleantmp:
ifeq ($(arg),)
	@$(call CLEAN,*,$(EXT_DEL_ALL))
else
	@$(call CLEAN,$(arg),$(EXT_DEL_ALL))
endif
	@find -name "*~" -exec rm {} \;

cleanpdf: cleantmp
ifeq ($(arg),)
	@rm -f *.pdf
else
	@rm -f $(arg).pdf
endif

clean: cleanpdf
	@$(call CLEAN,*,$(EXT_DEL_ALL))
	@rm -f */*.aux
