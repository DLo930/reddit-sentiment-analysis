# [doslingos] grader

import shutil
from gradeC0 import *

# The following flag should be False before we close handins, True after (then regrade)
#FINAL = True
FINAL = False

def test_sort_by_freq(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (sort_by_freq)"
   score = 0

   if not expect_exists("dos-sf-d", "sort_by_freq() does not compile"):
      return (0 if FINAL else -1)

   if not FINAL: return 0

   if expect_success("dos-sf-d example-in-handout",
                     "Exactly the sort example given in the handout"):
      score += 0.5

   if expect_success("dos-sf-d unsorted-vocab",
                     "Sort example give in the handout, but with the vocab changed so that it's not in alphabetical order initially, which wasn't required"):
      score += 1.0

   if expect_success("dos-sf-d ex-zeroes",
                     "Sort example given in the handout, all frequencies are zero"):
      score += 1.0

   if expect_success("dos-sf-d ex-negated",
                     "Sort example given in the handout, but with all the frequencies negated (positive frequencies weren't required by the problem specification)"):
      score += 1.0

   if expect_successes(["dos-sf-d ex-forward",
                        "dos-sf-d ex-backwards",
                        "dos-sf-d ex-split",
                        "dos-sf-d ex-stride"],
                       "Example from the handout, but with various combinations of (all unique) frequencies"):
      score += 1.0

   if expect_success("dos-sf-d shorties", "Unit tests with length 0, 1, and 2"):
      score += 1.0

   if expect_success("dos-sf longarray-randomtest",
                     "Random tests on an array of length half a million",
                     timeout = 15):
      score += 1.5

   return score

def test_count_vocab(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (count_vocab)"
   score = 0

   if not expect_exists("dos-cv", "count_vocab() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["dos-cv-d a1",
                         "dos-cv-d a2",
                         "dos-cv-d a3",
                         "dos-cv-d a4"],
                        "Preconditions wrong on count_vocab"):
      return (0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["dos-cv-d example-from-handout-linsearch",
                        "dos-cv example-from-handout-linsearch",
                        "dos-cv-d example-from-handout-binsearch",
                        "dos-cv example-from-handout-binsearch"],
                       "count_vocab did not behave as expected on the\n" + \
                          "*** small example (Scott Harbaugh's tweet) " + \
                          "from the handout."):
      score += 0.5

   if expect_successes(["dos-cv-d haha-lol",
                        "dos-cv haha-lol"],
                       "count_vocab did not behave as expected on the " + \
                          "tweet 'ha ha ha LOL LOL'."):
      score += 0.5

   if expect_success("dos-cv news_vocab",
                     "count_vocab did not behave as expected when given\n" + \
                        "*** news vocab and 1K of tweets"):
      score += 1.0

   if expect_successes(["dos-cv-d scott-thrice-1",
                        "dos-cv scott-thrice-1",
                        "dos-cv-d scott-thrice-2",
                        "dos-cv scott-thrice-2"],
                       "count_vocab did not behave as expected " + \
                          "on corner cases"):
      score += 1.0

   if expect_successes(["dos-cv-d tiny1",
                        "dos-cv tiny1",
                        "dos-cv-d tiny2",
                        "dos-cv tiny2",
                        "dos-cv-d tiny3",
                        "dos-cv tiny3",
                        "dos-cv-d tiny4",
                        "dos-cv tiny4"],
                       "count_vocab did not behave as expected " + \
                          "on corner cases"):
      score += 1.0

   return score

def test_analysis(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (analysis)"
   if expect_success("analyze texts/news_vocab_sorted.txt texts/shakespeare.txt",
                     expected_return_value = None,
                     timeout = 25 if FINAL else 12):
      with open (".tmp.stdout", "r") as myfile:
         string = myfile.read()

      if FINAL:
         expect_success("analyze texts/news_vocab_sorted.txt texts/sekret/twitter_200k.txt",
                        expected_return_value = None,
                        timeout = 25)
         with open (".tmp.stdout", "r") as myfile:
            string += "\n\n===== WITH TWITTER CORPUS: =====\n\n"
            string += myfile.read()

      return string

   return None

def test_doslingos_tests(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ ", tests for tasks 1 and 2 (doslingos-test.c0)"

   """STEP 1: CHECK WHETHER THINGS EVEN COMPILED"""

   if not os.path.exists("dos-our-impl"):
      if os.path.exists("dos-stu-impl"):
         print "*"*50
         print "There is an unexpected error, causing your tests to compile"
         print "against your implementation, but not against our"
         print "implementation. Either this means we did something wrong,"
         print "in the autograder, or it means that your implementation (and"
         print "tests) use the wrong arguments. You may want to see a TA for"
         print "help here."
         print "*"*50
         return (False, True, 0, 0, 0)
      else:
         print "*"*50
         print "Your test cases don't compile correctly!"
         print "Check the compilation error messages above."
         print "*"*50
         return (False, False, 0, 0, 0)

   """STEP 2: CHECK WHETHER CORRECT TESTS RUN CORRECTLY"""

   dos_ok = expect_success("dos-our-impl",
                           "Your test cases do not run against a " +\
                           "valid implementation of doslingos.c0",
                           timeout=20,
                           expected_return_value=None)
   if not dos_ok:
      print "\n******** Errors from incorrectly failed test ********\n"
      f = open('.tmp.output', 'r')
      print f.read()

   dos_yours = expect_success("dos-stu-impl",
                              "Your unit tests do not run against your code",
                              timeout=20,
                              expected_return_value=None)
   if not dos_yours:
      print "\n******** Errors from failed test ********\n"
      f = open('.tmp.output', 'r')
      print f.read()

   # Shortcut out if the test cases don't work
   if not dos_ok:
      return (dos_ok, dos_yours, 0, 0, 0)

   """ STEP 3: TEST BUGGY count_vocab IMPLEMENTATIONS"""

   cv_raw = 0
   if expect_abort("dos-cv-bug1", None):  cv_raw += 1
   if expect_abort("dos-cv-bug1b", None): cv_raw += 1
   if expect_abort("dos-cv-bug2", None):  cv_raw += 1
   if expect_abort("dos-cv-bug2b", None): cv_raw += 1
   if expect_abort("dos-cv-bug3", None):  cv_raw += 1
   if expect_abort("dos-cv-bug4", None):  cv_raw += 1
   if expect_abort("dos-cv-bug5", None):  cv_raw += 1
   if expect_abort("dos-cv-bug6", None):  cv_raw += 1
   if expect_abort("dos-cv-bug7", None):  cv_raw += 1
   if expect_abort("dos-cv-bug8", None):  cv_raw += 1
   if expect_abort("dos-cv-bug9", None):  cv_raw += 1
   if expect_abort("dos-cv-bugA", None):  cv_raw += 1
   if expect_abort("dos-cv-bugB", None):  cv_raw += 1
   if expect_abort("dos-cv-bugC", None):  cv_raw += 1
   if expect_abort("dos-cv-bugD", None):  cv_raw += 1
   if expect_abort("dos-cv-bugDb", None): cv_raw += 1
   if expect_abort("dos-cv-bugE", None):  cv_raw += 1
   if expect_abort("dos-cv-bugEb", None): cv_raw += 1
   cv_score_part = (cv_raw * 6.0) / 18.0

   """ STEP 4: TEST BUGGY sort_by_freq IMPLEMENTATIONS"""

   sf_raw = 0
   if expect_abort("dos-sf-bug1", None):  sf_raw += 1
   if expect_abort("dos-sf-bug1b", None): sf_raw += 1
   if expect_abort("dos-sf-bug1c", None): sf_raw += 1
   if expect_abort("dos-sf-bug2", None):  sf_raw += 1
   if expect_abort("dos-sf-bug3", None):  sf_raw += 1
   if expect_abort("dos-sf-bug4", None):  sf_raw += 1
   if expect_abort("dos-sf-bug5", None):  sf_raw += 1
   if expect_abort("dos-sf-bug5b", None): sf_raw += 1
   if expect_abort("dos-sf-bug5c", None): sf_raw += 1
   if expect_abort("dos-sf-bug5d", None): sf_raw += 1
   if expect_abort("dos-sf-bug6", None):  sf_raw += 1
   if expect_abort("dos-sf-bug7", None):  sf_raw += 1
   if expect_abort("dos-sf-bug8", None):  sf_raw += 1
   sf_score_part = (sf_raw * 6.0) / 13.0

   """ DONE """

   print "="*50
   print "Tests for task 1: "+str(cv_raw)+" bugs caught, "+str(cv_score_part)+" points"
   print "Tests for task 2: "+str(sf_raw)+" bugs caught, "+str(sf_score_part)+" points"

   if cv_score_part + sf_score_part < 8.0:
      score = round((cv_score_part + sf_score_part) * 32.0) / 32.0
      print "Score for task 3: "+str(score)
   else:
      score = 8
      print "Max score for Task 3, 8 points, reached"

   return (dos_ok, dos_yours, cv_raw, sf_raw, score)

def main():
   # Prettyprint a score post-release, signals failed compilation pre-release
   okmsg = "Compiles and the contracts check. That's all for now!"
   badmsg = "ERROR: does not compile or has bad contracts, check output!!!"
   nc_signal = -0.1    # scores that signals a failed compilation pre-release
   def print_final(task, score, max):
      if FINAL:
         print_score(task, score, max)
      else:
         print task+(okmsg if score is 0 else badmsg)

   count_vocab_score = test_count_vocab(1)
   sort_by_freq_score = test_sort_by_freq(2)
   (dos_ok, dos_yours, cv_tests, sf_tests, unit_tests_score) = test_doslingos_tests(3)
   analysis_result = test_analysis(4)

   if analysis_result is not None:
      print "Output of task 4:"
      print '-'*40
      print analysis_result
      print '-'*40
   print "\n"
   print '='*50
   print_final("Task 1: ", count_vocab_score,  4)
   print_final("Task 2: ", sort_by_freq_score, 7)
   print_score("Task 3: ", unit_tests_score,   8)
   if analysis_result is None:
      print_score("Task 4: ", 0, 6)
   else:
      print "Task 4: 6 points graded by hand based on above output."
      #print analysis_result
   total_score = unit_tests_score
   if FINAL:
      total_score += count_vocab_score + sort_by_freq_score

   print "\n",
   print '='*50

   if not dos_ok:
      print ("*** ERROR: YOUR TEST CASES DO NOT PASS A CORRECT UNIT TEST")
   if not dos_yours:
      print ("*** WARNING: YOUR OWN CODE DOESN'T WORK WITH YOUR UNIT TESTS")

   print "*** TOTAL SCORE: "+str(total_score)+"\n"
   scoreboard = [cv_tests + sf_tests, cv_tests, sf_tests]
   if FINAL:
      scores = {'count_vocab':  count_vocab_score,
                'sort_by_freq': sort_by_freq_score,
                'unit_tests':   unit_tests_score}
   else:
      scores = {'unit_tests':   unit_tests_score}
      if (count_vocab_score  != 0): scores['count_vocab']  = nc_signal
      if (sort_by_freq_score != 0): scores['sort_by_freq'] = nc_signal

   print json.dumps({'scores': scores,
                     'scoreboard': scoreboard})

if __name__ == "__main__":
   print "TESTING..."
   main()
