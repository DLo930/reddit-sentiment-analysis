This directory contains the source material and deployment scripts for
running an instance of 15-122.  This includes lecture notes, homework
assignments, labs and recitations, quizzes, exams and a few utilities.
It does not contain the course web site, student data, nor any
deployed file.  Other than that, this directory is self-contained:
this instance of 15-122 does not rely on files from surrounding
directories.

Preliminaries: Setting up course services

  a. Autolab
    . Email it-help@cmu.edu asking for a new Autolab instance.  Specify
      the course number, the semester, and the instructors.
    . Once you are notified that the new instance has been created,
      configure it in Manage Course > Course Settings.  Typical changes:
       . Grace days [3]
       . Late penalty [100 %]
       . Version penalty [5 %]

  b. Gradescope: log into gradescope.com and click on "Create a new
     course" (I think there is a way to clone a previous instance)

  c. Piazza
     Either: go to existing instance and click on 'clone this class'
            under the '15-122' menu.
     or: create the new class from scratch


The rest of this document explains how to create and configure a new
instance of 15-122 (e.g., f17) on the basis of an old instance (e.g.,
s17).

0. Getting SVN Access
   If you are able to execute step 1 below, you have SVN access.
   Continue to step 2.

   If step 1 fails, contact iliano@cmu.edu or fp@cs.cmu.edu to get SVN
   access.

   TAs can access selected portion of the SVN repository by using the
   shared username 'ta15122'.  Email iliano@cmu.edu for the
   corresponding password.


1. Make a copy of the old instance as the new instance:
	# cd <15-122 svn root>
        # svn cp s17 f17
        # svn ci -m "Copied f17 as s17"
        # cd f17
   At this point, the s17 directory is identical to the f17 directory.


2. Configure the global latex macros
	# emacs misc/latex/edition.sty
   Make changes as appropriate (typically just to \YEAR, \SEASON,
   \gradescope, \gradescopeEntryCode, \autolab and \piazzaURL)

   Configure the global Makefile definitions
	# emacs misc/inc/edition.mk
   Update AUTOLAB_REL_DIR and EDITION.  For installation to totally
   new platforms, update macros and/or definitions in the global
   Makefile configuration file
	# emacs misc/inc/config.mk


3. Configure, finalize and deploy lectures, labs, recitations,
   programming assignments, written assignments, quizzes and exams.

   To install labs, recitations, and programming and written
   assignments from your local machine, you will need to have
   an AFS client configured to use the 'cs.cmu.edu' cell.  Before
   running 'make install' (see below), issue the following commands
   (once is enough for a whole day):
        # kinit
        # aklog
        # aklog andrew.cmu.edu
   (You may consider writing a bash script with these commands.)

3(a). Lectures.
   Configuration:
	# cd lectures
   If wanted, update the contents of individual lectures (mainly the
   files <nn>-<lecture title>/main.tex).
   Install the lectures
	# make install
   (run 'make help' for more options)
   Propagate changes to the course web site.

3(b). Recitations
   Configuration:
	# cd recitations
   Update the date of each to match your schedule (macro \mfcsdate)
   and, if desired, the questions themselves (in directory 'questions')
   	# emacs *.tex
   (for a very few recitations, you may need to change the macro
   called \why).
   Authenticate and install the recitations on AFS
	# klog
	# make install
   (run 'make help' for more options)
   Go to the Autolab web interface for this course instance and
   click on 'Install Assessment'.  Under 'Import from file system',
   click on each 'rec??' and for each do the following:
   - Click on 'Admin Option > Edit assessment'
   - Click on 'HANDIN'
   - Set all dates (Start at, Due at, End at, Grading deadline) to the
     date this recitation should be released (e.g., 9am the day it
     takes place).
   - Press 'SAVE'

3(c). Labs
   Go to directory 'labs' and follow the same steps as for
   recitations, with the following notes:
   - some labs (currently just 01) expect students to make Autolab submissions
     . Set the 'Due at' deadline later in the day (e.g., 7pm)

3(d). Written assignments
  Go to the directory 'written' and follow the same steps as for
  recitations, with the following notes:
  - Modify exercises as desired (many already come with variants)
  - On Autolab, set all dates to the start date of the assignment
    (students do not submit on Autolab)
  - On Gradescope,
    . create a new assignment, upload the PDF file, set the submission
      mode to 'students', set the start and end dates (and late date
      if desired), and set the submission mode ot 'PDF with fixed
      templates'.
    . Edit the outline
    . Disable 'Regrade requests'
    . Make a test submission
    . Use the rubric file generated during compilation to populate the
      rubrics of each task of the test submission.

3(e). Programming assignments
  Go to the directory 'prog' and follow the same steps as for
  recitations, with the following notes:
  - before running 'make install hw=<hw_name>', it is advisable to run
        # make test hw=<hw_name>
    This runs the autograder locally against the reference solution.
    You should be getting full score (except for 'c0vm', which is
    finicky about libraries, and 'huffman' for which only the
    uncompressed solution is tested).  If something goes wrong, the
    test directory <hw_name>/test_env is a good place to figure out
    what happened.
  - Once installed, make two Autolab submissions:
    . one with just the starter code (or empty files): you should get 0
    . one with the reference solution: you should get full marks
  - Assignment specific notes:
    . 'scavhunt' can be customized.  See its README.txt file.
    . 'pixels' comes in three versions.  See its README.txt file.
    . 'images' comes in two versions.  See its README.txt file.
    . 'editor' and 'c0vm' have a checkpoint.  See their README.txt
      file.
    . 'doslingos', 'exp', 'editor' and 'c0vm' contain tasks that need
      to be graded after the submission deadline.  See their README.txt
      file for how to configure the autograder.
    . 'bloom' comes with an ungraded test instance.  See its README.txt
      file.
    . 'pixels', 'bloom', 'bloomtest', 'editor', and 'c0vm' needs
       for 'make init hw=<hw_name>' to be executed before installation.
    . 'pixels', 'doslingos' and 'editor' have a manually graded component.
      See their README.txt file.
    . 'images' and 'editor' feature style grading.  See their README.txt
       file.
  - In Autolab 'Admin Options > Edit assessment > HANDIN', set the
    'End at' and 'Grading deadline' dates one day later than the 'Due at'
    date (to account for late days).
  - Update the SEMESTER variable in the andrew handin script
    /afs/andrew/course/15/122/bin/handin
  - Send email to autolab-help@andrew.cmu.edu and ask them to wipe out
    the contents of the directory
    	/afs/andrew.cmu.edu/scs/cs/autolabEmail/handin/

3(f). Quizzes
	# cd quiz
      Quizzes are administered electronically Google forms.  The
      files <nn>.pptx are backups for students for whom this modality
      does not work -- the questions are the same but the electronic
      version is typically multiple choice to allow automated grading.
      Updated quizzes as needed.

3(g). Exams
	# cd exams
      See README.txt therein.


4. Course web page (http://cs.cmu.edu/~15122)
	# cd /afs/andrew.cmu.edu/course/15/122
   Create link to the new web page in www-archive
   	# ln -s <AFS location of new web page> www-archive/<semester>
   Remove old web page
   	# rm www
   Link www to www-archive/<semester>
        # ln -s www-archive/<semester> www

   (Alternatively, create the course web page in www-archive/<semester>
   and do the last two steps).
