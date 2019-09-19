#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) < 2:
        print "Usage: %s foo.c0 bar.c0 baz.c0..." % sys.argv[0]
        return
    assert(len(sys.argv) >= 2)

    print "Checking given files. Errors are critical and MUST be fixed for"
    print "your code to be readable on Autolab.\n\n"
    print "NOTE: Having no errors does NOT mean your code has good"
    print "style. All it means is that your code does not have any lines that"
    print "are too long. You should still look at your code on Autolab after"
    print "you submit to ensure that it looks good.\n"

    names = sys.argv[1:] # file names to check
    for f in names:
        s = " Checking %s " % f
        # Use "=" to separate output from different files. Pad to length 80
        # so it is more likely to stand out from the output for each file
        num_equals = 80 - len(s)
        print "=" * (num_equals/2 + num_equals % 2) + s + "=" * (num_equals/2)
        try:
            current = open(f, 'r')
        except IOError as e:
            # Couldn't open file, so just skip it and keep going.
            print "Couldn't open file %s: %s" % (f, e.strerror)
            continue
        line_num = 0
        for line in current:
            line_num += 1
            cur_len = len(line.rstrip("\n"))
            if cur_len > 80:
                print (
                   "Line %d is too long (%d characters, should be at most 80)!"
                    % (line_num, cur_len))

        current.close()

    print "=" * 80

if __name__ == "__main__":
    main()
