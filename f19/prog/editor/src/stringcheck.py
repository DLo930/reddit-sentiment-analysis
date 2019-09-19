# String hash checker for 15-122 Theory 4 Question 3
# Isaac Lim (idl)

import os,sys,math

tblSize = 4126

def hash(s):
    length = len(s)
    res = 0
    for i in xrange(0, length):
        res += ord(s[i]) * 31**(length-i-1) 

    return res % (2**32)

def main():
    print("String checker with hash table of size " + str(tblSize) + ".")
    print("If nothing is printed, then the strings collide.\n")

    # REPL-like checker
    while (True):
        str1 = raw_input("String 1: ")
        str2 = raw_input("String 2: ")

        h1 = hash(str1)
        h2 = hash(str2)

        h1m = h1 % tblSize
        h2m = h2 % tblSize

        if h1m != h2m:
            print("STRINGS DON'T COLLIDE!")
            print("Hash of str1: " + str(h1) + " (" + str(h1m) + ")")
            print("Hash of str2: " + str(h2) + " (" + str(h2m) + ")")

        print

if __name__ == '__main__':
    main()