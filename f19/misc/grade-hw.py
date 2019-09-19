#!/usr/bin/python

'''
Script for grade entry for 122 homework
Depends on class roster in ids.txt
Creates or appends to hw<number>.csv
To run :
  % python grade-hw.py
  Begin entering scores. To quit, use Ctrl + C.
  >> hbovik 2

@author niveditc
'''

import sys
import itertools

# Calculate distance between ids
# Source: http://hetland.org/coding/python/levenshtein.py
# I didn't feel like writing my own...
def dist(a,b):
    n, m = len(a), len(b)
    if n > m:
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]

f2 = open('ids.txt', 'r')
ids = [line[:-1] for line in f2.readlines()]
f2.close();

if sys.argv[-1] == "-nochecksum":
  print "Checksum validation turned off"
  validate = False
else:
  print sys.argv[-1]
  validate = True

number = raw_input('Homework number: ')
max_grades = filter(lambda x: x != '', raw_input('Question totals (separated by a space): ').split(' '))
num_questions = len(max_grades)
f = open('hw' + number + '.csv', 'a')

print 'Begin entering scores. To quit, use Ctrl + C.'
while True :
  input = raw_input('>> ').strip().split(' ')
  if len(input) != num_questions + (2 if validate else 1) :
    print 'ERROR: Incorrect number of arguments. Please enter in the form "<andrew_id> <q1> <q2> ... <qn> ' + ('<total>"' if validate else '"')
  elif input[0] not in ids :
    print 'ERROR: ' + input[0] + ' is not in the class roster! Please check the spelling. To override, manually edit ' + 'hw' + number + '.csv'
    # Find likely matches
    distances = sorted(ids, key = lambda x: dist(x, input[0]))
    print "Possible matches:"
    for possible in distances[0:3]:
        print " -", possible
  else :
    total = 0
    valid = True
    for i in xrange(num_questions) :
      if (float(input[i + 1]) > float(max_grades[i])) or (float(input[i + 1]) < 0) :
        print 'ERROR: Score ' + input[i + 1] + ' is invalid for question ' + str(i + 1)
        valid = False
      total += float(input[i + 1])
    if validate and total != float(input[-1]) :
      print 'ERROR: Total should be ' + str(total) + ' with the given grades'
    elif valid :
      f.write(input[0] + '@andrew.cmu.edu,')
      if validate: f.write(','.join(input[1:-1]) + '\n')
      else: f.write(','.join(input[1:]) + '\n')
      f.flush()
      print 'Success!'

f.close()
