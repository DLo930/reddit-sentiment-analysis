# Common Makefile definitions that rarely need to be changed

# Where are we running?
HOSTNAME:=$(shell hostname -f | sed -e 's/^[^.]*\.//')

# Iliano's machine (not important if you are not Iliano)
LOCAL_HOSTNAME:=ladigue

# Full Autolab path for this edition
AUTOLAB_BASE:=/afs/cs.cmu.edu/academic/class/$(AUTOLAB_REL_DIR)/autolab

# Full web course path for this edition
ifneq ($(shell hostname -s),$(LOCAL_HOSTNAME))
  WWW_DIR:=/afs/andrew.cmu.edu/course/15/122/www-archive/$(EDITION)
else
  WEB_REL_DIR:=$(EDITION_LOCAL)-CMU-CS122
  WWW_DIR:=~/public_html/courses/$(WEB_REL_DIR)
endif

# Temporary file extensions
DEL:=aux log out
EXT_DEL:=pdf rubric xml

### $(call CLEAN,file,exts) removes file.xyz with xyz in exts
define CLEAN
for ext in $2; do  \
  rm -f $1.$$ext;  \
done
endef

# Which latex to use?  (default latex on unix.andrew.cmu.is obsolete)
ifeq ($(HOSTNAME),andrew.cmu.edu)
  PDFLATEX=/afs/cs.cmu.edu/academic/class/15122-f14/tex/2014/bin/x86_64-linux/pdflatex
else
  PDFLATEX=pdflatex
endif


# PDF viewer
ifeq ($(shell uname),Linux)
  PDF_VIEWER:=evince
else
  # MacOS
  PDF_VIEWER:=open -a Preview.app
endif

### Diderot configuration -- not use
DIDEROT_CONFIG:=misc/diderot.json

### Diderot command line interface
# Executable
#DIDEROT_CLI_EXEC:=../misc/diderot/cli.old/diderot_admin
# Credential file
#DIDEROT_CREDS:=../misc/diderot/credentials.txt
# Command prefix
#DIDEROT_CLI:=$(DIDEROT_CLI_EXEC) --credentials $(DIDEROT_CREDS) --command

# Executable
DIDEROT_CLI_EXEC:=../misc/diderot/cli/diderot_admin
# Credential file in ~/.diderot/credentials
# Command prefix
DIDEROT_CLI:=$(DIDEROT_CLI_EXEC) upload_chapter $(DIDEROT_COURSE)
