#!/usr/bin/env python

import sys

def indent_style(line):
    assert(isinstance(line, str))
    leading = line[:len(line) - len(line.lstrip())]
    tabs = '\t' in leading
    spaces = ' ' in leading
    if tabs and spaces:
        if line[0] == '\t':
            return ("TABS", "SPACES")
        else:
            return ("SPACES", "TABS")
    elif spaces:
        return "SPACES"
    elif tabs:
        return "TABS"
    else:
        return "NONE"

def check_style(global_style, line_style):
    assert(isinstance(global_style, str) and isinstance(line_style, str))
    return global_style in ["", line_style]

def main():
    if len(sys.argv) < 2:
        print "Usage: %s foo.c0 bar.c0 baz.c0..." % sys.argv[0]
        return
    assert(len(sys.argv) >= 2)

    print "Checking given files. Errors are critical and MUST be fixed for"
    print "your code to be readable on Autolab. Warnings should probably be"
    print "fixed but if you check on Autolab and the indentation looks OK"
    print "then it's not as important.\n\n"
    print "NOTE: Having no errors or warnings does NOT mean your code has good"
    print "style or even that its indentation is good. All it means is that"
    print "your code does not have mixed tabs and spaces. You should still"
    print "look at your code on Autolab after you submit to ensure that it"
    print "looks good.\n"

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
        doc_style = ""
        for line in current:
            line_num += 1
            line_style = indent_style(line)
            assert(line_style in [("SPACES", "TABS"), ("TABS", "SPACES"),
                                   "SPACES", "TABS", "NONE"])
            if line_style != "NONE":
                if isinstance(line_style, tuple):
                    print (
                       "Warning: line %d has tabs and spaces at the beginning."
                            % line_num)
                    line_style = line_style[0]
                if check_style(doc_style, line_style):
                    doc_style = line_style
                else:
                    print (("Error: line %d has %s while the rest of the" +
                           " document has %s.")
                           %(line_num, line_style.lower(), doc_style.lower()))
        current.close()

    print "=" * 80

if __name__ == "__main__":
    main()
