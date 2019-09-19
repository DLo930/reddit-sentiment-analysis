# Compiler command and common flags
CC = gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic
# Compiler command in debug mode
CCD = $(CC) -DDEBUG -g
LIB = lib/*.c

# compile
compile: connected.c main.c
	$(CCD) $(LIB) -o search connected.c main.c

# clean up
clean:
	@rm -rf search *.dSYM *~
