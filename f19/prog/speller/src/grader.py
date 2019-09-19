# [speller] grader

import shutil
from gradeC0 import *
import time

# The following flag should be False before we close handins, True after (then regrade)
#FINAL = True
FINAL = False

def test_check_word(tasknum):
   print "="*50
   print "Testing Task "+str(tasknum)+" (check_word)"
   score = 0.0

   if not expect_exists("spl", "check_word() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["spl-d cw-prec1a",
                         "spl-d cw-prec1b",
                         "spl-d cw-prec2",
                         "spl-d cw-prec3"],
                        "Preconditions wrong on check_word"):
      return (0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["spl-d cw-scott1",
                        "spl   cw_scott1",
                        "spl-d cw-scott2",
                        "spl   cw_scott2",
                        "spl-d cw-scott3",
                        "spl   cw_scott3"],
                       "check_word did not behave as expected on the\n" + \
                          "*** small dictionary (from Scott Harbaugh's tweet) " + \
                          "from the handout."):
      score += 0.5

   if expect_successes(["spl-d cw-sloth1",
                        "spl   cw_sloth1",
                        "spl-d cw-sloth2",
                        "spl   cw_sloth2"],
                       "check_word did not behave as expected on the\n" + \
                          "*** medium dictionary (from the sloth text) " + \
                          "from the handout."):
      score += 0.5

   if expect_success("spl cw-large",
                    "check_word did not behave as expected on a\n" + \
                       "*** large dictionary of English words"):
      score += 0.5

   if expect_successes(["spl-d cw-empty",
                        "spl   cw-empty",
                        "spl-d cw-num",
                        "spl   cw-num",
                        "spl-d cw-class",
                        "spl   cw-class",
                        "spl-d cw-nonalpha",
                        "spl   cw-nonalpha",
                        "spl-d cw-none",
                        "spl   cw-none"],
                       "check_word did not behave as expected " + \
                          "on corner cases"):
      score += 0.5

   return score


def test_check_text_or_better(version, tasknum):
   if version=="fast":
      function = "check_text_better"
   else:
      function = "check_text_naive"

   print "="*50
   if version == "":
      print "Testing Task "+str(tasknum)+" ("+function+")"
   else:
      print "Testing Task "+str(tasknum)+" ("+function+")"
   score = 0.0

   if not expect_exists("spl", function+"() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["spl-d "+version+"spell-prec1",
                         "spl-d "+version+"spell-prec2",
                         "spl-d "+version+"spell-prec3",
                         "spl-d "+version+"spell-prec4",
                         "spl-d "+version+"spell-prec5"],
                        "Preconditions wrong on "+function):
      return (0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["spl-d "+version+"spell-small",
                        "spl   "+version+"spell-small",
                        "spl-d "+version+"spell-medium",
                        "spl   "+version+"spell-medium"],
                       function+" did not behave as expected on the\n" + \
                          "*** small/medium dictionaries and texts."):
      score += 0.5

   if expect_successes(["spl   "+version+"spell-large-text",
                        "spl   "+version+"spell-large-dict",
                        "spl   "+version+"spell-large"],
                       function+" did not behave as expected on a\n" + \
                          "*** large dictionary or a large text.",
                       timeout=20 if version=="fast" else 180):
      score += 0.5

   if expect_successes(["spl   "+version+"spell-self-small",
                        "spl   "+version+"spell-self-medium",
                        "spl   "+version+"spell-self-large"],
                       function+" did not behave as expected on\n" + \
                          "*** self-spelling a dictionary.",
                       timeout=20):
      score += 0.5

   if expect_successes(["spl-d "+version+"spell-dict0",
                        "spl   "+version+"spell-dict0",
                        "spl-d "+version+"spell-dict1",
                        "spl   "+version+"spell-dict1",
                        "spl-d "+version+"spell-text0",
                        "spl   "+version+"spell-text0",
                        "spl-d "+version+"spell-text1",
                        "spl   "+version+"spell-text1"],
                       function+" did not behave as expected on\n" + \
                          "*** corner cases."):
      score += 0.5

   return score


def test_check_sorted(tasknum):
   print "="*50
   print "Testing Task "+str(tasknum)+" (check_sorted_text)"
   score = 0.0

   if not expect_exists("spl", "check_sorted_text() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["spl-d sorted-spell-prec1",
                         "spl-d sorted-spell-prec2",
                         "spl-d sorted-spell-prec3",
                         "spl-d sorted-spell-prec4",
                         "spl-d sorted-spell-prec5",
                         "spl-d sorted-spell-prec6",
                         "spl-d sorted-spell-prec7"],
                        "Preconditions wrong on check_sorted_text"):
      return (0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["spl-d sorted-spell-small",
                        "spl   sorted-spell-small",
                        "spl-d sorted-spell-medium",
                        "spl   sorted-spell-medium"],
                       "check_sorted_text did not behave as expected on the\n" + \
                          "*** small/medium dictionaries and texts."):
      score += 1.0

   if expect_successes(["spl   sorted-spell-large-text",
                        "spl   sorted-spell-large-dict",
                        "spl   sorted-spell-large"],
                       "check_sorted_text did not behave as expected on a\n" + \
                          "*** large dictionary or a large text.",
                       timeout=20):
      score += 1.0

   if expect_successes(["spl   sorted-spell-self-small",
                        "spl   sorted-spell-self-medium",
                        "spl   sorted-spell-self-large"],
                       "check_sorted_text did not behave as expected on\n" + \
                          "*** self-spelling a dictionary.",
                       timeout=20):
      score += 1.0

   if expect_successes(["spl-d sorted-spell-dict0",
                        "spl   sorted-spell-dict0",
                        "spl-d sorted-spell-dict1",
                        "spl   sorted-spell-dict1",
                        "spl-d sorted-spell-text0",
                        "spl   sorted-spell-text0",
                        "spl-d sorted-spell-text1",
                        "spl   sorted-spell-text1"],
                       "check_sorted_text did not behave as expected on\n" + \
                          "*** corner cases."):
      score += 1.0

   return score

def test_merge(tasknum):
   print "="*50
   print "Testing Task "+str(tasknum)+" (merge)"
   score = 0.0

   if not expect_exists("spl", "merge() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["spl-d merge-prec1a",
                         "spl-d merge-prec1b",
                         "spl-d merge-prec1bb",
                         "spl-d merge-prec1c",
                         "spl-d merge-prec1d",
                         "spl-d merge-prec1dd",
                         "spl-d merge-prec1e",
                         "spl-d merge-prec2",
                         "spl-d merge-prec3",
                         "spl-d merge-prec4",
                         "spl-d merge-prec5"],
                        "Preconditions wrong on merge"):
      return (0.0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["spl-d merge-small",
                        "spl   merge-small"],
                       "merge did not behave as expected on the\n" + \
                          "*** small arrays."):
      score += 1.0

   if expect_successes(["spl-d merge-medium",
                        "spl   merge-medium"],
                       "merge did not behave as expected on the\n" + \
                          "*** medium-sized arrays."):
      score += 1.0

   if expect_successes(["spl   merge-large"],
                       "merge did not behave as expected on a\n" + \
                          "*** large dictionary or a large text.",
                       timeout=60):
      score += 1.0

   if expect_successes(["spl-d merge-singleton",
                        "spl   merge-singleton"],
                       "merge did not behave as expected on\n" + \
                          "*** corner cases."):
      score += 2.0

   return score


def test_mergesort(tasknum):
   print "="*50
   print "Testing Task "+str(tasknum)+" (mergesort)"
   score = 0.0

   if not expect_exists("spl", "mergesort() does not compile"):
      return (0 if FINAL else -1)

   if not expect_aborts(["spl-d ms-prec1",
                         "spl-d ms-prec2",
                         "spl-d ms-prec3"],
                        "Preconditions wrong on mergesort"):
      return (0.0 if FINAL else -1)

   if not FINAL: return 0

   if expect_successes(["spl-d ms-small",
                        "spl   ms-small"],
                       "mergesort did not behave as expected on the\n" + \
                          "*** small arrays."):
      score += 0.5

   if expect_successes(["spl-d ms-medium",
                        "spl   ms-medium"],
                       "mergesort did not behave as expected on the\n" + \
                          "*** medium-sized arrays."):
      score += 0.5

   if expect_successes(["spl   ms-large"],
                       "mergesort did not behave as expected on a\n" + \
                          "*** large dictionary or a large text.",
                       timeout=60):
      score += 1.0

   if expect_successes(["spl-d ms-empty",
                        "spl   ms-empty",
                        "spl-d ms-singleton",
                        "spl   ms-singleton",
                        "spl-d ms-nowidth",
                        "spl   ms-nowidth"],
                       "mergesort did not behave as expected on\n" + \
                          "*** corner cases."):
      score += 1.0

   return score


def test_speller_tests(tasknum):
   max_score = 4.0                     # number of points a student can earn
   available_points = 1.5 * max_score  # number of points a student can rake

   print "="*50
   print "Testing Task "+str(tasknum)+", tests for tasks 1 and 5 (speller-test.c0)"

   """STEP 1: CHECK WHETHER THINGS EVEN COMPILED"""

   if not os.path.exists("spl-our-impl"):
      if os.path.exists("spl-stu-impl"):
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

   spl_ok = expect_success("spl-our-impl",
                           "Your test cases do not run against a " +\
                           "valid implementation of speller.c0",
                           timeout=20,
                           expected_return_value=None)
   if not spl_ok:
      print "\n******** Errors from incorrectly failed test ********\n"
      f = open('.tmp.output', 'r')
      print f.read()

   spl_yours = expect_success("spl-stu-impl",
                              "Your unit tests do not run against your code",
                              timeout=20,
                              expected_return_value=None)
   if not spl_yours:
      print "\n******** Errors from failed test ********\n"
      f = open('.tmp.output', 'r')
      print f.read()

   # Shortcut out if the test cases don't work
   if not spl_ok:
      return (spl_ok, spl_yours, 0, 0, 0)

   """ STEP 3: TEST BUGGY check_word IMPLEMENTATIONS"""

   cw_raw = 0

   cw = 1.0  # number of tests for check_word
   if expect_abort("spl-cw-bug0", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug1", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug2", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug3", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug4", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug5", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug6", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug7", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug8", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bug9", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugA", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugB", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugC", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugD", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugE", None):  cw_raw += 1
   cw += 1.0
   if expect_abort("spl-cw-bugF", None):  cw_raw += 1
   cw_score_part = (cw_raw * available_points/2.0) / cw

   """ STEP 4: TEST BUGGY check_better IMPLEMENTATIONS"""

   cb_raw = 0

   cb = 1.0 # number of tests for check_better
   if expect_abort("spl-cb-bug0", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug1", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug2", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug3", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug4", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug5", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug6", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug7", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug8", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bug9", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugA", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugB", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugC", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugD", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugE", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugF", None):  cb_raw += 1
   cb += 1.0
   if expect_abort("spl-cb-bugG", None):  cb_raw += 1
   cb_score_part = (cb_raw * available_points/2.0) / cb

   """ DONE """

   print "="*50
   print "Tests for task 1: "+str(cw_raw)+" bugs caught, "+str(cw_score_part)+" points"
   print "Tests for task 5: "+str(cb_raw)+" bugs caught, "+str(cb_score_part)+" points"

   if cw_score_part + cb_score_part < max_score:
      score = round((cw_score_part + cb_score_part) * 32.0) / 32.0
      print "Score for task 6: "+str(score)
   else:
      score = max_score
      print "Max score for Task 6, "+str(max_score)+" points, reached"

   return (spl_ok, spl_yours, cw_raw, cb_raw, score)


def test_analysis(tasknum):
   print "="*50
   print "Testing Task "+str(tasknum)+" (analysis)"
   if expect_success("analyze texts/dict.txt texts/shakespeare.txt",
                     expected_return_value = None,
                     timeout = 25 if FINAL else 12):
      with open (".tmp.stdout", "r") as myfile:
         string = myfile.read()

      if FINAL:
         expect_success("analyze texts/news_vocab_sorted.txt texts/twitter_200k.txt",
                        expected_return_value = None,
                        timeout = 25)
         with open (".tmp.stdout", "r") as myfile:
            string += "\n\n===== WITH TWITTER CORPUS: =====\n\n"
            string += myfile.read()

      return string

   return None


def main():
   # Prettyprint a score post-release, signals failed compilation pre-release
   okmsg = "Compiles and the contracts check. That's all for now!"
   badmsg = "ERROR: does not compile or has bad contracts, check output!!!"
   nc_signal = -0.1    # scores that signals a failed compilation pre-release
   def print_final(task, score, max):
      if FINAL:
         print_score(task, score, max)
      else:
         print task+(badmsg if score is -1 else okmsg)

   check_word_score = test_check_word(1)
   check_naive_score = test_check_text_or_better("", 2)
   check_sorted_score = test_check_sorted(3)
   merge_score = test_merge(4)
   mergesort_score = test_mergesort(5)
   check_better_score = test_check_text_or_better("fast", 6)
   (spl_ok, spl_yours, cw_tests, cb_tests, unit_tests_score) = test_speller_tests(7)
   analysis_result = test_analysis(8)

   naive_score      = check_word_score + check_naive_score
   sorting_score    = merge_score + mergesort_score

   print "\n"
   print '='*50
   print_final("Task 1: ", check_word_score,   2)
   print_final("Task 2: ", check_naive_score,  2)
   print_final("Task 3: ", check_sorted_score, 4)
   print_final("Task 4: ", merge_score,        5)
   print_final("Task 5: ", mergesort_score,    3)
   print_final("Task 6: ", check_better_score, 2)
   print_score("Task 7: ", unit_tests_score,   4)
   if analysis_result is None:
      print "Task 8: 0.0/3 points"
   else:
      print "Task 8: 3 points graded by hand based on this output"
      print "******  and other tests:\n"
      print analysis_result
   total_score = unit_tests_score
   if FINAL:
      total_score += naive_score + check_sorted_score + sorting_score + check_better_score

   print "\n",
   print '='*50

   if not spl_ok:
      print ("*** ERROR: YOUR TEST CASES DO NOT PASS A CORRECT UNIT TEST")
   if not spl_yours:
      print ("*** WARNING: YOUR OWN CODE DOESN'T WORK WITH YOUR UNIT TESTS")

   print "*** TOTAL SCORE: "+str(total_score)+"\n"
   scoreboard = [cw_tests + cb_tests, cw_tests, cb_tests]
   if FINAL:
      scores = {'spell_naive' : naive_score,
                'spell_sorted': check_sorted_score,
                'sorting'     : sorting_score,
                'spell_better': check_better_score,
                'unit_tests'  : unit_tests_score}
   else:
      scores = {'unit_tests': unit_tests_score}
      if (naive_score        != 0): scores['spell_naive']  = nc_signal
      if (check_sorted_score != 0): scores['spell_sorted'] = nc_signal
      if (sorting_score      != 0): scores['sorting']      = nc_signal
      if (check_better_score != 0): scores['spell_better'] = nc_signal

   print json.dumps({'scores':     scores,
                     'scoreboard': scoreboard})

if __name__ == "__main__":
   print "TESTING..."
   main()
