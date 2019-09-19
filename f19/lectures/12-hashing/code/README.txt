To compile:
	# cc0 -d stack.c1 main.c1
and run
	# a.out

stack.c0 and elem-stack.c0 are given for reference and can be tested
using coin:
	# coin -d elem-stack.c0
        # coin -d stack-client.c0 stack.c0
or cc0:
	# cc0 -d -x elem-stack.c0 main.c0
        # cc0 -d -x stack-client.c0 stack.c0 main.c0
