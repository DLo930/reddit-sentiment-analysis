
Starting a solution directory
=============================

First, make the directory and set up SVN to ignore most of the files
in that directory; obviously replace "andrewid" with your name or
andrewid.

$ cd 2
$ mkdir sol-andrewid             # or "mkdir solution" for the canonical solution
$ svn add sol-andrewid
$ cd sol-andrewid 
$ svn propset svn:ignore '*' .   # single quotes around the * are important

Second, copy the handout code

$ make                           # this distills the handout code
$ mv hw2-handout/* sol-andrewid  # this puts that code in your directory

You want to use "svn add" to add *only* the files relevant to the
solution, the ones named as "HANDIN_FILES" in the Makefile.

Running the autograder
======================

Once you have a directory with the appropriate HANDIN_FILES in it, you
can run the autograder by typing

$ make test SOLUTION=sol-andrewid

If you omit SOLUTION=sol-andrewid and just type "make test" it
defaults to trying to test the solution in the directory "solution".

All of the executables created by the autograder are placed in the
directory test_env, so if you want to run them by hand (for instance,
to see *where* a failed assertion failed), you can cd into the
test_env directory and run tests directly.

Installing into autolab
=======================

The prog/common/homework.mk file is the parent of all makefiles: it
needs to be updated with the autolab directories for the current
semester.

The FIRST TIME "make install" is run in prog/someassignment, the
necessary autolab files for someassignment are created in Autolab-land
and the configuration files someassignment.rb and someassignment.yml
are placed there. We do not copy these configuration files multiple
times!

Those configuration files are only updated, inside Autolab-land space,
every time you click "Export Assessment" from the assignments Autolab
admin menu. If you want to update the .yml and .rb files for an
assignment, you'll then type "make refresh". That command copies the
configuration files from Autolab-land BACK to SVN land.

EVERY TIME you type "make install"
 - the handout is rebuilt
 - the PDF is rebuilt
 - the handout and pdf are thrown into Autolab-land
 - the .tgz of the code handout is thrown into the directory listed as
   PUBDIR in common/homework.mk

For assignments with a checkpoint, "make installcheck" populates the
checkpoint.
