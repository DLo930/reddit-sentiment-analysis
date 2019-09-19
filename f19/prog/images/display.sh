#!/bin/sh

make
cp $1 images-handout
cp src/pixel-int.c0 images-handout
cd images-handout
tar xzvf $1
cc0 -w -o manip pixel-int.c0 imageutil.c0 mask.c0 manipulate.c0 manipulate-main.c0
./manip -i images/g5.png -o g5-my-manip.png
gthumb g5-my-manip.png
cd ..
