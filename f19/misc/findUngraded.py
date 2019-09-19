import csv
import os

## USAGE:
#
# 1. From Gradescope's "Review grades", click export evaluations
# 2. Extract the archive
# 3. cd into it
# 4. run python path/to/findUngraded.py

def printIncomplete(path):
  r = csv.reader(file(path))

  # Change this if your Grading Complete field is named something else.
  gc = "GRADING COMPLETE"

  headers = map(lambda s: s.lower().strip(), r.next())

  index = headers.index(gc.lower())

  print "*** " + path + " ***"

  for line in r:
    if line == []: break
    if len(line) <= index:
      print("Error, malformed file")
      print line
      break
    if line[index] == "false":
      print line
  print "\n"

for path in sorted(os.listdir(os.getcwd())):
  if path.endswith(".csv"):
    printIncomplete(path)
