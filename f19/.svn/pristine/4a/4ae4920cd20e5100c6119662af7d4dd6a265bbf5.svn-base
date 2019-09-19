This homework contains tasks that are autograded only after the
submission deadline.

To install the student-facing version of the autograder (which does
not grade all tasks):
- in src/grader.py, set the variable POSTFINAL to False
- install the homework on Autolab

To install the post-deadline version of the autograder (which grades
all tasks):
- in src/grader.py, set the variable POSTFINAL to True
- install the homework on Autolab
- on Autolab, navigate to 'Admin Options > Manage Submissions' and click
  'Regrade All' (please avoid times near the submission deadline of
  other courses)



This homework has a two Autolab instances, one for the checkpoint and
one for the full assignment.
- The checkpoint is in directory ../c0vmcheck
- The full assignment is in directory ../c0vm

The Makefile of each operates differently from other homeworks:
- c0vm: run
  > make init    hw=c0vm  (new!)
  > make install hw=c0vm  (or other normal make invocations)

- c0vmcheck: run
  > make init    hw=c0vmcheck  (new!)
  > make install hw=c0vmcheck  (or other normal make invocations)
  > make final   hw=c0vmcheck  (new!)

(init creates the appropriate src/grader.py file)
(final renames the writeup and handout files on Autolab)



Currently, you need to create a cc0.tgz correctly in order to run this
code. This is a tarball of the c0 installation, so <whatever>/c0 below
is wherever your local c0 is installed.

$ cd hw/9
$ pushd <whatever>/c0
$ tar czvf cc0.tgz cc0/lib cc0/include cc0/runtime
$ popd
$ mv <whatever>/cc0.tgz src

In Spring 2013 I took away a lot of the nitpicky comparison and large
jump tests, as the new version of the compiler seems intent on never
writing any if_cmpXX with an offset different than 6. A future change
to the bytecode might even consider turning if_cmpXX into a one-byte
or two-byte instructuction, since it's wasted as a three-byte
instruction. Not that there's anything wrong with that, but it's a way
we could manipulate the bytecode. - RJS

UPDATING THE BYTECODE:

If the compiler changes in a way that changes any libraries, or if the
bytecode spec is incremented at all, then the bytecode version for the
compiler will be bumped.

 * The src/lib/c0vm_c0ffi.c and src/lib/c0vm_c0ffi.h files are
   generated automatically by the compiler, and need to be copied from
   the compiler's repository (they are cc0/vm/c0vm_c0ffi.? in the
   source distribution).

 * If libraries were added, then this will need to be reflected in
   autograde-Makefile and src/Makefile

 * All the C0 files need to be recompiled into BC0 files. This takes
   awhile.

   $ cd src/tests/testN/c0
   $ ls *.c0 | xargs -L 1 cc0 -b
   $ mv *.bc0 ..
