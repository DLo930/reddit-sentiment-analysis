# default target
default:
	$(MAKE) tries-test

clean:
	-rm -rf tries-test tries-test.dSYM tries2-test tries2-test.dSYM

tries-test: lib/contracts.h lib/xalloc.h lib/xalloc.c tries.h tries.c tries-test.c
	$(CC) -DDEBUG -g -Wall -Wextra -Werror -std=c99 -pedantic lib/xalloc.c \
	  -o tries-test tries.c tries-test.c

