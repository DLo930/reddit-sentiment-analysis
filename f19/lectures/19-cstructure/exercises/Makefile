CC=gcc
CFLAGS=-Wall -Wextra -Werror -Wshadow -std=c99 -pedantic -g

default:
	@echo "Usage:"
	@echo "  make list_free"
	@echo "  make clean"
	@echo ""

list_free: xalloc.c list_free.c
	$(CC) $(CFLAGS) xalloc.c list_free.c

clean:
	rm -Rf *.o a.out *.dSYM
