# Compiler command and common flags
CC = cc0
# Compiler command in debug mode
CCD = $(CC) -d
EXEC = $(CC) -x
EXECD = $(CCD) -x

default:
	@echo "Usage:"
	@echo "  make print-genlist"
	@echo "  make compose-pipeline"
	@echo "  make clean"
	@echo ""

print-genlist: print-genlist.c1 print-genlist-test.c1
	$(EXECD) print-genlist.c1 print-genlist-test.c1

compose-pipeline:  compose-pipeline.c1 compose-pipeline-test.c1
	$(EXECD) compose-pipeline.c1 compose-pipeline-test.c1

clean:
	rm -f a.out
