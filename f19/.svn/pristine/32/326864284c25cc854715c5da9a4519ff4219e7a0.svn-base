simple: simple.h simple.c
	gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic -g -DDEBUG lib/*.c test.c simple.c

tree: tree.c
	gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic -g -DDEBUG lib/*.c tree.c


run-simple: simple
	./a.out

run-tree: tree
	./a.out

clean:
	rm -rf a.out a.out.dSYM
