# Compiler command and common flags
CC = gcc -Wall -Wextra -Wshadow -Werror -std=c99 -pedantic
# Compiler command in debug mode
CCD = $(CC) -DDEBUG -g
LIB = lib/*.c

help:
	@echo "make [help]   -- print these instructions"
	@echo "make compile  -- compile representation xyz"
	@echo "make run      -- run representation xyz"
	@echo "make vrun     -- run representation xyz with valgrind"
	@echo "make clean    -- remove temporary files"

# compile
compile: graph.c test.c
	$(CCD) $(LIB) graph.c test.c

# compile and run
run: compile
	./a.out

# compile and run with valgrind
vrun: compile
	valgrind ./a.out

# clean up
clean:
	@rm -rf a.out *.dSYM *~
