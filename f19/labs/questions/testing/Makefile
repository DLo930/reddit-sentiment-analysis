CC = /usr/bin/gcc
CFLAGS = -Wall -g
LIBS = -lpthread

FILES = src/check_test.c src/csapp.c
OUTFILE = src/check-test
HANDOUT_DIR = handout
HANDOUT = $(HANDOUT_DIR)/check-test

all: check_test

# What not to interpret as files
.PHONY: handout

#
# Using link-time interpositioning to introduce non-determinism in the
# order that parent and child execute after invoking fork
#
check_test: $(FILES)
	$(CC) $(CFLAGS) -o $(OUTFILE) $(FILES) $(LIBS)


# Clean up
clean:
	rm -rf $(HANDOUT_DIR) *.o *~

# Create Hand-in
handout: $(FILES) clean
	mkdir $(HANDOUT_DIR)
	$(CC) $(CFLAGS) -o $(HANDOUT) $(FILES) $(LIBS)
	cp src/main.c0 $(HANDOUT_DIR)/main.c0
	cp src/testlib.c0 $(HANDOUT_DIR)/testlib.c0
	cp src/blank_set-test.c0 $(HANDOUT_DIR)/set-test.c0
	tar czvf handout-04.tgz $(HANDOUT_DIR)/
