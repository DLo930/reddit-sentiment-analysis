This homework contains tasks that are manually graded after the
submission deadline.


This homework has a two Autolab instances, one for the checkpoint and
one for the full assignment.
- The checkpoint is in directory ../editorcheck
- The full assignment is in directory ../editor

The Makefile of each operates differently from other homeworks:
- editor: run
  > make init    hw=editor  (new!)
  > make install hw=editor  (or other normal make invocations)

- editorcheck: run
  > make init    hw=editorcheck  (new!)
  > make install hw=editorcheck  (or other normal make invocations)
  > make final   hw=editorcheck  (new!)

(init creates the appropriate src/grader.py file)
(final renames the writeup and handout files on Autolab)
