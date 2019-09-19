AUTOLAB_BASE=/afs/cs.cmu.edu/academic/class/15122-f16/autolab
AUTOLAB_Q_BASE=/afs/cs.cmu.edu/academic/class/15122q-s16/autolab

DOMAIN=$(shell hostname -d)
ifeq ($DOMAIN,andrew.cmu.edu)
  PUBDIR=/afs/cs.cmu.edu/user/iliano/www/misc/15122
else
  PUBDIR=~iliano/public_html/courses/16F-CMU-CS122/hw
endif

WRITEUP_DIR:=writeup
#WRITEUP:=$(NAME)-writeup
WRITEUP:=main
SOLUTION=solution
AUTOLAB_DIR=$(AUTOLAB_BASE)/$(NAME)
AUTOLAB_Q_DIR=$(AUTOLAB_Q_BASE)/$(NAME)

ifeq ($DOMAIN,andrew.cmu.edu)
  PDFLATEX=/afs/cs.cmu.edu/academic/class/15122-f14/tex/2014/bin/x86_64-linux/pdflatex
else
  PDFLATEX=pdflatex
endif

GRADER=gradeC0.py

default: $(NAME)-handout.tgz autograde.tar

all: handin.tgz $(NAME)-handout.tgz autograde.tar

.PHONY: clean
clean:
	rm -Rf $(NAME)-handout test_env *.tgz *~ test_env

# Tarballs (always make the tarballs!)
.PHONY: handin.tgz $(NAME)-handout.tgz autograde.tar test_env test

handin.tgz:
	tar -h -C $(SOLUTION) -czf handin.tgz $(HANDIN_FILES)

$(NAME)-handout.tgz:
	rm -Rf $(NAME)-handout
	mkdir $(NAME)-handout
	for dir in $(HANDOUT_SUBDIRS); do mkdir $(NAME)-handout/$$dir; done
	for file in $(HANDOUT_FILES); do cp -p src/$$file $(NAME)-handout/$$file; done
	tar -czf $(NAME)-handout.tgz $(NAME)-handout

src/$(GRADER):
	cp ../inc/$(GRADER) src

autograde.tar: src/$(GRADER)
	@tar -C src -cf autograde.tar $(TEST_FILES) $(GRADER)
	rm src/$(GRADER)

# Simulate autograder on solution directory

test_env:
	mkdir -p test_env

test: test_env autograde.tar handin.tgz
	rm -Rf test_env/*
	cp autograde-Makefile test_env/Makefile
	cp autograde.tar test_env
	cp handin.tgz test_env
	$(MAKE) -C test_env

# PDF
.PHONY: pdfs

pdfs:
	cd $(WRITEUP_DIR); $(PDFLATEX) $(WRITEUP)
	cd $(WRITEUP_DIR); $(PDFLATEX) $(WRITEUP)

### AUTOLAB INSTALLATION AND SYNC

$(AUTOLAB_DIR):
	mkdir -p $(AUTOLAB_DIR)

$(AUTOLAB_DIR)check:
	mkdir -p $(AUTOLAB_DIR)check

$(AUTOLAB_Q_DIR):
	mkdir -p $(AUTOLAB_Q_DIR)

$(AUTOLAB_Q_DIR)check:
	mkdir -p $(AUTOLAB_Q_DIR)check

# Always update config files on refresh
.PHONY: autolab_dir autolab_dircheck autolab_q_dir autolab_q_dircheck

autolab_dir: $(AUTOLAB_DIR)
	cp $(NAME).yml $(AUTOLAB_DIR)
	cp $(NAME).rb $(AUTOLAB_DIR)

autolab_dircheck: $(AUTOLAB_DIR)check
	cp $(NAME)check.yml $(AUTOLAB_DIR)check
	cp $(NAME)check.rb $(AUTOLAB_DIR)check

autolab_q_dir: $(AUTOLAB_Q_DIR)
	cp $(NAME).yml $(AUTOLAB_Q_DIR)
	cp $(NAME).rb $(AUTOLAB_DIR)

autolab_q_dircheck: $(AUTOLAB_Q_DIR)check
	cp $(NAME)check.yml $(AUTOLAB_Q_DIR)check
	cp $(NAME)check.rb $(AUTOLAB_Q_DIR)check

ALL_INSTALL_DEPS=autograde-Makefile autograde.tar
REG_INSTALL_DEPS=autolab_dir $(NAME).rb $(NAME).yml
CHECK_INSTALL_DEPS=autolab_dircheck \
  $(NAME)check.rb $(NAME)check.yml
REG_Q_INSTALL_DEPS=autolab_q_dir $(NAME).rb $(NAME).yml
CHECK_Q_INSTALL_DEPS=autolab_q_dircheck \
  $(NAME)check.rb $(NAME)check.yml

install: $(ALL_INSTALL_DEPS) $(REG_INSTALL_DEPS) default pdfs
	cp autograde.tar $(AUTOLAB_DIR)/
	cp autograde-Makefile $(AUTOLAB_DIR)/
	cp $(NAME)-handout.tgz $(AUTOLAB_DIR)/
	cp $(WRITEUP_DIR)/$(WRITEUP).pdf $(AUTOLAB_DIR)/$(NAME)-writeup.pdf
#	cp $(WRITEUP_DIR)/$(WRITEUP).pdf $(PUBDIR)/$(NAME)-writeup.pdf
	cp $(NAME)-handout.tgz $(PUBDIR)/

installq: $(ALL_INSTALL_DEPS) $(REG_Q_INSTALL_DEPS) default pdfs
	cp autograde.tar $(AUTOLAB_Q_DIR)/
	cp autograde-Makefile $(AUTOLAB_Q_DIR)/
	cp $(NAME)-handout.tgz $(AUTOLAB_Q_DIR)/
#	cp $(WRITEUP_DIR)/$(WRITEUP).pdf $(AUTOLAB_Q_DIR)/$(NAME)-writeup.pdf

installcheck: $(ALL_INSTALL_DEPS) $(CHECK_INSTALL_DEPS) default pdfs
	cp autograde.tar $(AUTOLAB_DIR)check/
	cp autograde-Makefile $(AUTOLAB_DIR)check/
	cp $(NAME)-handout.tgz $(AUTOLAB_DIR)check/
	cp $(WRITEUP_DIR)/$(WRITEUP).pdf $(AUTOLAB_DIR)check/$(NAME)-writeup.pdf
	cp $(NAME)-handout.tgz $(PUBDIR)/

installcheckq: $(ALL_INSTALL_DEPS) $(CHECK_Q_INSTALL_DEPS) default pdfs
	cp autograde.tar $(AUTOLAB_Q_DIR)check/
	cp autograde-Makefile $(AUTOLAB_Q_DIR)check/
	cp $(NAME)-handout.tgz $(AUTOLAB_Q_DIR)check/
	cp $(WRITEUP_DIR)/$(WRITEUP).pdf $(AUTOLAB_Q_DIR)check/$(NAME)-writeup.pdf
	cp $(NAME)-handout.tgz $(PUBDIR)/

refresh:
	cp $(AUTOLAB_DIR)/$(NAME).rb .
	cp $(AUTOLAB_DIR)/$(NAME).yml .

refreshcheck:
	cp $(AUTOLAB_DIR)check/$(NAME)check.rb .
	cp $(AUTOLAB_DIR)check/$(NAME)check.yml .
