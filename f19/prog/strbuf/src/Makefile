CC=gcc
CFLAGS=-Wall -Wextra -Werror -std=c99 -pedantic

# Default target.  If you change this, you must make sure that
# 'make strbuf-d' and 'make strbuf' compile as expected before
# you hand in your files.
default: strbuf-d

# The *.dSYM directories will not exist on Linux, but rm -rf
# should tolerate that.
clean:
	-rm -rf strbuf-d strbuf-d.dSYM strbuf strbuf.dSYM strbuf-bug?

# These two targets are a little abusive of make.
# However, the alternative is a cryptic error message that students will likely
# not understand.
strbuf.c:
	@echo "Error: strbuf.c does not exist. You need to write this file before compiling."
	exit 1

strbuf-test.c:
	@echo "Error: strbuf-test.c does not exist. You need to write this file before"
	@echo "       compiling."
	exit 1

# Do not change the following two targets,
# because this is what the Autograder uses
strbuf-d: lib/contracts.h lib/xalloc.h lib/xalloc.c strbuf.h strbuf.c strbuf-test.c
	$(CC) -DDEBUG -g $(CFLAGS) lib/xalloc.c -o strbuf-d strbuf.c strbuf-test.c

strbuf: lib/contracts.h lib/xalloc.h lib/xalloc.c strbuf.h strbuf.c strbuf-test.c
	$(CC) $(CFLAGS) lib/xalloc.c -o strbuf strbuf.c strbuf-test.c

# Following targets work on Andrew linux servers in order to link
# your strbuf-test.c against buggy strbuf implementations provided
# by the course staff.  Use (for example):
#
# make strbuf-bug1
# ./strbuf-bug1
#
# should raise an "assert" exception if you have caught the bug.
# It is your responsibility to make sure that the standard reference
# implementation (available only on Autolab) actually passes your tests.
#
# You are being given bugs 1-5 to test in this manner.
# Bugs 6-8 are only available through Autolab.

LIBDIR=/afs/cs/academic/class/15122-s13/libhw7

strbuf-bug%: lib/contracts.h lib/xalloc.h lib/xalloc.c strbuf.h strbuf-test.c $(LIBDIR)/strbuf-bug%.o
	$(CC) $(CFLAGS) lib/xalloc.c -o $@ $(LIBDIR)/$@.o strbuf-test.c

# You may add further targets below.  Recommended simple format:
# <target>: <dependencies>
#	<command-to-execute>
# where <target> is the name of the binary to create
# <dependencies> are the files that, if changed, require regeneration of target
# <command-to-execute> is the shell command that will create the target
