# Compiler command and common flags
CC = cc0
# Compiler command in debug mode
CCD = $(CC) -d
EXEC = $(CC) -x
EXECD = $(CCD) -x

default:
	@echo "Usage:"
	@echo "  make queue-sum"
	@echo "  make stack-size"
	@echo "  make clean"
	@echo ""

queue-sum: int-elem.c0 queue.c0 queue-sum.c0 queue-sum-test.c0
	$(EXECD) int-elem.c0 queue.c0 queue-sum.c0 queue-sum-test.c0


stack-size: int-elem.c0 stack.c0 stack-size.c0 stack-size-test.c0
	$(EXECD) int-elem.c0 stack.c0 stack-size.c0 stack-size-test.c0

clean:
	rm -f a.out
