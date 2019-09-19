from gradeC0 import *
from grader import test_tests

def main():
   score = 0
   if expect_exists("correct_impls", "tests did not compile"):
      score = test_tests()
      print '='*50
      print "You caught "+str(score)+" of the buggy programs with your tests"
      if score == 0: print "You need better tests to get extra lab credit"
      elif score <= 7: print "That's enough for lab credit; can you do better?"
      elif score <= 16: print "Very good work!"
      else: print "Extraordinary work!"
      print '='*50
      print open('images-test.c0', 'r').read()
      print '='*50
   print '\n\n\n'
   print json.dumps({'scores': {'passed_tests': score}})

if __name__ == "__main__":
   print "TESTING..."
   main()
