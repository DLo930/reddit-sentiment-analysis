This directory contains the written homeworks of 15-122.

Organization:
-------------
README.txt		   This file
Makefile		   Shortcuts -- run 'make' for an overview
<num>.tex		   Written hw numbered <num>
questions/		   Directory of hw questions
questions/<name>.tex	   Writeup for self-contained question
questions/<name>/	   Directory for multi-file question
questions/<name>/main.tex  Writeup for multi-file question
questions/<name>/code.c0   Code file for multi-file question
questions/<name>/img/	   Image directory for multi-file question
common/			   Utilities shared by all hw
common/preamble.tex	   Imported packages, etc
common/frontmatter.tex	   Common homework parts before all questions
common/backmatter.tex	   Common homework parts after all questions


Creating a homework:
--------------------
A written hw is created by picking individual questions from the question
directory and \input'ing them between \begin{questions} and
\end{questions}.  See examples


Homework macros:
----------------
\hwnumber		The number of the homework
\duedate		Due date
\shortdesc		A short description of what the homework is about
\specialInstructions	Redefine to append text to the default instructions
\useEditablePDF		Define is wanting to use editable forms


Creating a new question:
--------------------
Create a question called <name> in the question directory.  If it is
self-contained (i.e., if it consists of a single file), simply call it
<name>.tex .  Otherwise, create a subdirectory called <name> and call
it <name>/main.tex .  Define other files as you see fit (e.g.,
<name>/img/ for images).

Question macros:
------------
\Question[pt]{title}	   Use this instead of \question to set the
			   question title (and points)
\answer{len}{sol}          Space for a line answer of length len with
                           solution sol in 'answer' mode
\uanswer{len}{sol}         Space for an underlined line answer of length
                           len with solution sol in 'answer' mode
\RUBRIC
<any multiline text
(including \, #, %,
whatever)>
ENDRUBRIC		   Rubric for an individual task within a
			   question.  ENDRUBRIC (not \ENDRUBRIC)
			   should be on a line by itself.

Rubrics:
--------
Compiling homework <num>.tex creates the file <num>.rubric which
collates the rubrics for all questions (defined between \RUBRIC and
ENDRUBRIC).
