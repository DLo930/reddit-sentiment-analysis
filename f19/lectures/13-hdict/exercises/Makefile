# Compiler command and common flags
CC = cc0
# Compiler command in debug mode
CCD = $(CC) -d
EXEC = $(CC) -x
EXECD = $(CCD) -x

default:
	@echo "Usage:"
	@echo "  make student-record"
	@echo "  make tabulate"
	@echo "  make clean"
	@echo ""

student-record: hash-student.c0 hdict.c0 hash-student-test.c0
	$(EXECD) hash-student.c0 hdict.c0 hash-student-test.c0

tabulate: hash-student.c0 hdict.c0 hash-tabulate-test.c0
	$(EXECD) hash-student.c0 hdict.c0 hash-student-test.c0

clean:
	rm -f a.out
