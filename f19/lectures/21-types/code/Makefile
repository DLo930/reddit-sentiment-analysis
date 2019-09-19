# Compiler command and common flags
CC=gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic
# Compiler command in debug mode
CCD = $(CC) -DDEBUG -g

# compile
leafytree: leafytree.c
	$(CCD) -o leafytree lib/*.c leafytree.c

# compile and run
run: leafytree
	./leafytree

# clean up
clean:
	rm -rf leafytree leafytree.dSYM
