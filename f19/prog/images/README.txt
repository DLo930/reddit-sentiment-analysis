This homework features style grading.  The rubric can be found in
      rubrics/style-grading-rubric.txt


NOTE: the image lab was retired in S18.

The Images programming assignment is currently intended to be put together
in one of two ways: as rotate+mask, or reflect+blur. There's a lab
that pairs with this assignment.  I think rotate is a little bit harder
than reflect, blur is a little bit harder than mask, and between the
two assignments I feel like it hits most of the notes.

 * rotate+mask:  s19 s18 s17 s16 s15 f14
 * reflect+blur: f18 f17 f16 f15 m15

Things that need to be changed to swap between assignments:
 - Two (un)commented lines at the top of config.mk
   (the lab component is not used any more, so you can ignore the
   variable LAB -- the name of Autolab directory of the lab that used
   to go with this assignment)
 - Two (un)commented lines at the top of writeup/main.tex
 - A single (un)commented line at the top of src/grader.py
 - A single (un)commented line in autograde-Makefile
 - A single (un)commented line in .../labs/questions/images/main.tex
 - A single (un)commented line in solution/images-test.c0
   (only if you plan to test that the lab Autograder works correctly).

From prog/, run
  make readme hw=images
  make lab hw=images
to propagate updates to the README.txt file and to the lab


The listing below is finer-grained, and stops in f14
====================================================

PROBLEM 1: imageutil
  * imageutil - pretty much always

PROBLEM 2: per-pixel manipulations (moved to prog1 in f13)
  * quantize - s11 r11 f11 s12 m12
  * invert - f12

PROBLEM 3: image transforms
    warhol (easier, also does per-pixel manipulation) - f10 m14
    stretch - r11
  * reflect - f12 s13 m13 m14
  * rotate - s11 f11 s12 m12 f13 s14 f14

PROBLEM 4: edge cases. literally, edge cases.
    pixellate (easier) - f10
    edge - f10
  * blur - s11 r11 f11 s12 m12 f13 s14
  * mask - f12 s13 m13 m14 f14

BONUS:
  * manipulate - pretty much always
