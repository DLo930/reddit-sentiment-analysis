#!/bin/bash
#
# IMAGES BONUS PROBLEM GRADING SCRIPT
# 
# This script takes a path to a .tgz archive, extracts it, runs the student's 
# manipulate function, and copies the output (and source file) to the directory
# named "output". In order to run this, you should extract the images handout
# archive, copy this file and a correct pixel.c0 into it, and create the
# "output" directory.
#
# On macOS, you'll probably need to do
#     brew install coreutils
# to get the "gtimeout" command. If you're running Linux, you'll
# probably need to replace instances of "gtimeout" with "timeout" below.
#
# To run this script for all files in a directory, use the following command:
#     find path/to/submissions/directory -exec ./extract_manipulate.sh {} \;
#

rm -rf imageutil.c0 rotate.c0 mask.c0 images-test.c0 manipulate.c0 manipulate manipulate.dSYM *.png images/manipulate.png;
tar -xzvf $1 || tar -xvf $1;
ANDREWID=`echo $1 | sed -e 's/.*\///g' | sed -e 's/@.*$//g'`;

if [[ -f manipulate.c0 ]]; then
    cc0 -d -w -o manipulate pixel.c0 imageutil.c0 rotate.c0 mask.c0 manipulate.c0 manipulate-main.c0 &&
    if [[ -f manipulate.png ]]; then
        gtimeout 40 ./manipulate -i manipulate.png -o $ANDREWID"_output.png"
        cp manipulate.png "output/"$ANDREWID"_input.png"
    elif [[ -f images/manipulate.png ]]; then
        gtimeout 40 ./manipulate -i images/manipulate.png -o $ANDREWID"_output.png"
        cp images/manipulate.png "output/"$ANDREWID"_input.png"
    else
        gtimeout 40 ./manipulate -i images/g5.png -o $ANDREWID"_output.png"
    fi &&
    cp $ANDREWID"_output.png" output/ &&
    cp manipulate.c0 "output/"$ANDREWID"_manipulate.c0"
fi
