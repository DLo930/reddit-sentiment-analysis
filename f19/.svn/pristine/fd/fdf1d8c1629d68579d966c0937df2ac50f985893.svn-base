# Compiler command and common flags
CC = gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic
# Compiler command in debug mode
CCD = $(CC) -DDEBUG -g


# compile
test: test.c
	$(CCD) -o test lib/*.c test.c

# compile and run
run: test
	./test

vrun: test
	valgrind ./test

# clean up
clean:
	rm -rf test test.dSYM
