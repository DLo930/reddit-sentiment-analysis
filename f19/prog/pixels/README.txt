This homework has a manually graded component.  The rubric can be
found in
      rubrics/manual-grading-rubric.txt



The Pixels programming assignment is currently intended to be put together
in one of three ways: as opacify+histogram, as remove_red+count_zeroes
or as remove_green+summarize.

Things that need to be changed to swap between assignments:
 - A single (un)commented lines at the top of config.mk
 - A single (un)commented line at the top of writeup/main.tex
 - A single (un)commented line at the top of src/grader.py

From prog/, run
	make init hw=pixels
to select the hw variant, and then use make as usual
