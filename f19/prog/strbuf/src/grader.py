# [strbuf] grader

from gradeC0 import *


def test_is_strbuf(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_strbuf)"
   if not expect_exists("strbuf0-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0

   rawscore = 0
   if expect_success("strbuf0-grade is_strbuf",
                     "Basic is_strbuf tests fail"):
      rawscore += 1
   if expect_success("strbuf0-grade is_strbuf_contiguous",
                     "is_strbuf doesn't check for the presence of another " +\
                     "NUL terminator to the left of sb->len"):
      rawscore += 1
   if expect_success("strbuf0-grade is_strbuf_tougher",
                     "is_strbuf tests designed to cause segfaults " +\
                     "or assertion errors when returning false was possible"):
      rawscore += 1
   if expect_success("strbuf0-grade is_strbuf-bogus-limit-too-small-and-wrong",
                     "if given an obviously-too-small limit, is_strbuf " +\
                     "should return 'false' rather than aborting"):
      rawscore += 1
   if expect_success("strbuf0-grade is_strbuf_overly_strict",
                     "is_strbuf fails valid string buffers, likely " +\
                     "because it requires something particular to the " +\
                     "right of sb->len"):
      rawscore += 1
   if expect_abort("strbuf0-grade is_strbuf_limit1",
                   "array length checks"):
      rawscore += 1
   if expect_abort("strbuf0-grade is_strbuf_limit2",
                   "array length checks"):
      rawscore += 1

   if rawscore == 7: return 4
   elif rawscore >= 5: return 3
   elif rawscore >= 3: return 2
   elif rawscore >= 1: return 1
   else: return 0


def test_strbuf_basic(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (strbuf_new, strbuf_str)"
   if not expect_exists("strbuf0-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0

   rawscore = 0
   if expect_successes(["strbuf0-grade strbuf_new3",
                        "strbuf0-grade strbuf_new1"],
                       "strbuf_new doesn't seem to work on valid inputs"):
      rawscore += 1

   if expect_aborts(["strbuf0-grade strbuf_new-1",
                     "strbuf0-grade strbuf_new0"],
                    "strbuf_new seems to have insufficient preconditions"):
      rawscore += 1

   if expect_success("strbuf0-grade strbuf_str",
                     "Basic strbuf_str tests"):
      rawscore += 1

   if expect_success("strbuf0-grade strbuf_str-size",
                     "Checking for minimal memory usage by strbuf_str"):
      rawscore += 1

   if expect_abort("strbuf0-grade strbuf_strnull",
                   "Invalid inputs to strbuf_str"):
      rawscore += 1

   if rawscore == 5: return 3
   elif rawscore >= 3: return 2
   elif rawscore >= 1: return 1
   else: return 0


def test_strbuf_add(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (strbuf_add, strbuf_addstr)"
   if not expect_exists("strbuf0-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0

   score = 0
   if expect_aborts(["strbuf0-grade strbuf_add1",
                     "strbuf0-grade strbuf_add2",
                     "strbuf0-grade strbuf_add3",
                     "strbuf0-grade strbuf_add4",
                     "strbuf0-grade strbuf_add5",
                     "strbuf0-grade strbuf_addstr1"],
                    "strbuf_add and strbuf_addstr seem to have insufficent "+\
                    "preconditions"):
      score += 1

   if expect_success("strbuf0-grade strbuf_add", "strbuf_add tests"):
      score += 1

   if expect_success("strbuf0-grade strbuf_addstr", "strbuf_addstr tests"):
      score += 1

   if score < 3: return score

   # Performance testing add

   time1000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_add 1000",
                         "Stress test at 1000 failed, perf. bug",
                         timeout = 10):
      return score
   time1000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   time2000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_add 2000",
                         "Stress test at 2000 failed, perf. bug",
                         timeout = 20):
      return score
   time2000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   time4000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_add 4000",
                         "Stress test at 4000 failed, perf. bug",
                         timeout = 40):
      return score
   time4000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   FUDGE = 0.01
   if time1000_end - time1000_start < 0.0002:
      ratio1 = 1
   else:
      ratio1 = float(time2000_end - time2000_start - FUDGE) / \
               float(time1000_end - time1000_start + FUDGE)

   if time2000_end - time2000_start < 0.0002:
      ratio2 = 1
   else:
      ratio2 = float(time4000_end - time4000_start - FUDGE) / \
               float(time2000_end - time2000_start + FUDGE)

   if (ratio1 <= 2.5 and ratio2 <= 2.5):
      print "Experimentally confirmed amortized linear-time strbuf_add"
      print "stress 1000: "+\
         str(time1000_end - time1000_start).rjust(10)+\
         "seconds"
      print "stress 2000: "+\
         str(time2000_end - time2000_start).rjust(10)+\
         "seconds"
      print "stress 4000: "+\
         str(time4000_end - time4000_start).rjust(10)+\
         "seconds"
      score += 1
   else:
      print "Unable to confirm amortized linear-time strbuf_add"
      print "stress 1000: "+\
         str(time1000_end - time1000_start).rjust(10)+\
         "seconds"
      print "stress 2000: "+\
         str(time2000_end - time2000_start).rjust(10)+\
         "seconds"
      print "stress 4000: "+\
         str(time4000_end - time4000_start).rjust(10)+\
         "seconds"
      return score

   # Performance testing addstr

   time1000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_addstr 1000",
                         "Stress test at 1000 failed, perf. bug",
                         timeout = 10):
      return score
   time1000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   time2000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_addstr 2000",
                         "Stress test at 2000 failed, perf. bug",
                         timeout = 20):
      return score
   time2000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   time4000_start = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if not expect_success("strbuf0-fast stress_addstr 4000",
                         "Stress test at 4000 failed, perf. bug",
                         timeout = 40):
      return score
   time4000_end = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime

   # Allow for .02 seconds of measurment error

   if time1000_end - time1000_start < 0.0002:
      ratio1 = 1
   else:
      ratio1 = float(-0.03 + time2000_end - time2000_start) / \
               float(0.03 + time1000_end - time1000_start)

   if time2000_end - time2000_start < 0.0002:
      ratio2 = 1
   else:
      ratio2 = float(-0.03 + time4000_end - time4000_start) / \
               float(0.03 + time2000_end - time2000_start)

   if (ratio1 <= 2.2 and ratio2 <= 2.2):
      print "Experimentally confirmed amortized linear-time strbuf_addstr"
      print "stress 1000: "+\
         str(time1000_end - time1000_start).rjust(10)+\
         "seconds"
      print "stress 2000: "+\
         str(time2000_end - time2000_start).rjust(10)+\
         "seconds"
      print "stress 4000: "+\
         str(time4000_end - time4000_start).rjust(10)+\
         "seconds"
      score += 1

   else:
      print "Unable to confirm amortized linear-time strbuf_addstr"
      print "stress 1000: "+\
         str(time1000_end - time1000_start).rjust(10)+\
         "seconds"
      print "stress 2000: "+\
         str(time2000_end - time2000_start).rjust(10)+\
         "seconds"
      print "stress 4000: "+\
         str(time4000_end - time4000_start).rjust(10)+\
         "seconds"

   return score

def test_strbuf0_tests(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (C0 test cases)"
   if not expect_exists("strbuf0-nobug1",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return (0, "*")

   if not expect_successes([("strbuf0-nobug1", None),
                            ("strbuf0-nobug2", None)],
                           "Unit tests fail on a valid implementation"):
      print "\n******** Errors from incorrectly failed test ********\n"
      f = open('.tmp.output', 'r')
      print f.read()
      return (0, "**")

   score = 0
   rawscore = 0
   if expect_abort("strbuf0-bug2", "is_strbuf bug [this one's graded]"):
      # is_strbuf doesn't check length of string
      rawscore += 1
      score += 1

   if expect_abort("strbuf0-bug3", "strbuf_new bug"):
      # strbuf_new doesn't return an empty string
      rawscore += 1

   if expect_abort("strbuf0-bug5", "strbuf_str bug [this one's graded]"):
      # strbuf_str returns the internal array
      rawscore += 1
      score += 1

   if expect_abort("strbuf0-bug6", "strbuf_str bug"):
      # strbuf_str returns a shorter string
      rawscore += 1

   if expect_aborts(["strbuf0-bug7",
                     "strbuf0-bug7b"],
                    "strbuf_add(str) bug"):
      # strbuf_add(str) never resizes
      rawscore += 1

   if expect_aborts(["strbuf0-bug7",
                     "strbuf0-bug7b"],
                    "strbuf_add(str) bug [this one's graded]"):
      # strbuf_add(str) writes to beginning
      rawscore += 1
      score += 1

   if expect_abort("strbuf0-bug9",
                   "Our implementation has an bug in strbuf_new. "+\
                   "Your test cases pass on this buggy implementation."):
      # strbuf_new ignores argument, picks size 13
      rawscore += 1

   if expect_abort("strbuf0-bugA",
                   "Our implementation has an bug in strbuf_str. "+\
                   "Your test cases pass on this buggy implementation."):
      # strbuf_str returns too much string
      rawscore += 1

   if expect_abort("strbuf0-bugB",
                   "Our implementation has an bug in is_strbuf. "+\
                   "Your test cases pass on this buggy implementation."):
      # is_strbuf basically just returns true
      rawscore += 1

   if expect_abort("strbuf0-bugC",
                   "Our implementation has an bug in is_strbuf. "+\
                   "Your test cases pass on this buggy implementation."):
      # is_strbuf requires buffer to be empty
      rawscore += 1

   if expect_abort("strbuf0-bugD",
                   "Our buggy is_strbuf implementation aborts when it " +\
                   "could have returned false. "+\
                   "Your test cases pass on this buggy implementation."):
      # is_strbuf aborts when it could have returned false
      rawscore += 1

   if expect_abort("strbuf0-bugE",
                   "Our strbuf_add implementation has too strict of a " +\
                   "precondition, and would fail if you passed as the " +\
                   "second argument the char array represented " +\
                   "on page 2. "+\
                   "Your test cases pass on this buggy implementation."):
      # strbuf_add requires the length of the array to be something specific
      rawscore += 1

   if expect_abort("strbuf0-bugF",
                   "Another strbuf_add(str) bug [this one's graded]"):
#                   "Our strbuf_add implementation assumes that the " +\
#                   "unspecified portion of sb->buf contains only '\\0's "+\
#                   "(see note at the end of Section 2). " +\
#                   "Your test cases pass on this buggy implementation."):
      # strbuf_add doesn't write the terminating NUL character
      rawscore += 1
      score += 1

   return (score, str(rawscore))

def test_dealloc(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (strbuf_dealloc)"
   if not expect_exists("strbuf-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0

   if not expect_abort("strbuf-grade strbuf_dealloc_bad",
                       "strbuf_dealloc preconditions"):
      return 0

   if expect_success("strbuf-grade strbuf_dealloc", "strbuf_dealloc"):
      return grind_deductions(["strbuf-grade strbuf_dealloc"],
                              score = 2,
                              safety = 2,
                              leaky = 2)
   return 0

def test_c_impl(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (C implementation)"
   if not expect_exists("strbuf-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0

   rawscore = 0
   if expect_successes(["strbuf-grade is_strbuf",
                        "strbuf-grade is_strbuf_contiguous",
                        "strbuf-grade is_strbuf_tougher",
                        "strbuf-grade is_strbuf_overly_strict",
                        "strbuf-grade is_strbuf_c_specific_bugs"],
                       "is_strbuf translation tests"):
      rawscore += 1

   if expect_aborts(["strbuf-grade strbuf_new0",
                     "strbuf-grade strbuf_strnull"],
                    "strbuf_new seems to have insufficient preconditions"):
      if expect_successes(["strbuf-grade strbuf_new3",
                           "strbuf-grade strbuf_new1",
                           "strbuf-grade strbuf_str"],
                          "strbuf_new and strbuf_str"):
         rawscore += grind_deductions(["strbuf-grade strbuf_new3",
                                       "strbuf-grade strbuf_new1",
                                       "strbuf-grade strbuf_str"],
                                      score = 2,
                                      safety = 2,
                                      leaky = 2)

   if expect_aborts(["strbuf-grade strbuf_add1",
                     "strbuf-grade strbuf_add2",
                     "strbuf-grade strbuf_add3",
                     "strbuf-grade strbuf_add4",
                     "strbuf-grade strbuf_add5",
                     "strbuf-grade strbuf_addstr1",
                     "strbuf-grade strbuf_add1_c_specific",
                     "strbuf-grade strbuf_add2_c_specific",
                     "strbuf-grade strbuf_add3_c_specific",
                     "strbuf-grade strbuf_addstr_c_specific"],
                    "strbuf_add and strbuf_addstr seem to have insufficient "+\
                    "preconditions"):
      if expect_successes(["strbuf-grade strbuf_add",
                           "strbuf-grade strbuf_addstr"],
                          "strbuf_add and strbuf_addstr"):
         rawscore += grind_deductions(["strbuf-grade strbuf_add",
                                       "strbuf-grade strbuf_addstr"],
                                      score = 2,
                                      safety = 2,
                                      leaky = 2)

   return rawscore

# =======
#    score = 0
#    if expect_success("strbuf-fg contracts",
#                      "Translated code appears to lack contracts "+\
#                      "(note: new contracts are neccessary!)"):
#       score += 1
# >>>>>>> .r3771

# def test_c_impl():
#    print "="*50
#    print "Testing Task 5-6 (C implementation)"
#    if not expect_exists("strbuf-dg",
#                         "Skipping task 5/6 (tests did not compile w/ -DDEBUG)"):
#       return 0

#    if not expect_exists("strbuf-g",
#                         "Skipping task 5/6 (tests did not compile w/o -DDEBUG)"):
#       return 0

#    score = 0
#    if expect_success("strbuf-fg contracts",
#                      "Translated code appears to lack contracts "+\
#                      "(note: new contracts are neccessary!)"):
#       score += 1

#    trans = 0
#    if expect_success("strbuf-dg task1",
#                      "Code translation for task1 (is_strbuf)"):
#       trans += 1

#    if expect_success("strbuf-dg task2",
#                      "Code translation for task 2 (strbuf_str, strbuf_new) as well as strbuf_dealloc"):
#       trans += 1

#    if expect_success("strbuf-dg task3",
#                      "Code translation for task3 (strbuf_add, strbuf_addstr)"):
#       trans += 1

#    if trans == 3:
#       score += grind_deductions(["strbuf-dg task1",
#                                  "strbuf-dg task2",
#                                  "strbuf-dg task3"],
#                                 score = 6,
#                                 safety = 3,
#                                 leaky = 3,
#                                 timeout = 30)
#    else:
#       print "-"*50
#       print "*** Must finish C translation before we grade this with valgrind"

#    return score

def test_strbufc_tests(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (C Unit Tests)"
   if not expect_exists("strbuf-bugok1",
                        "Skipping C unit tests (tests did not compile without -DDEBUG)"):
      return (0, "*")

   if not expect_exists("strbuf-bugok2",
                        "Skipping C unit tests (tests did not compile with -DDEBUG)"):
      return (0, "*")

   if not expect_successes(["strbuf-bugok1",
                            "strbuf-bugok2"],
                         "C Unit tests fail on a valid implementation (make sure your main function returns 0)",
                         expected_return_value = None):
      return (0, "**")

   rawscore = 0
   if expect_abort("strbuf-bug1"):
      rawscore += 1
   if expect_abort("strbuf-bug2"):
      rawscore += 1
   if expect_abort("strbuf-bug3"):
      rawscore += 1
   if expect_abort("strbuf-bug4"):
      rawscore += 1
   #removed because it can segfault/undefined
   #if expect_abort("strbuf-bug5"):
   #   rawscore += 1
   if expect_abort("strbuf-bug6"):
      rawscore += 1
   if expect_abort("strbuf-bug7"):
      rawscore += 1
   if expect_abort("strbuf-bug8"):
      rawscore += 1
   if expect_abort("strbuf-bug9"):
      rawscore += 1
   if expect_abort("strbuf-bugA"):
      rawscore += 1

   if rawscore > 7: score = 2
   elif rawscore > 4: score = 1
   else: score = 0

   return (score, str(rawscore))

def main():
   is_strbuf_grade            = test_is_strbuf(1)
   strbuf_basic_grade         = test_strbuf_basic(2)
   strbuf_add_grade           = test_strbuf_add(3)
   (strbuf_test0_grade, raw0) = test_strbuf0_tests(4)
   translate_grade            = test_c_impl(5)
   dealloc_grade              = test_dealloc(6)
   (strbufc_test_grade, rawc) = test_strbufc_tests(7)

   print '='*50
   print_score("Task 1: ", is_strbuf_grade,    4)
   print_score("Task 2: ", strbuf_basic_grade, 3)
   print_score("Task 3: ", strbuf_add_grade,   5)
   print_score("Task 4: ", strbuf_test0_grade, 4,
               extra=" (found "+raw0+" bugs)")
   print_score("Task 5: ", translate_grade,    5)
   print_score("Task 6: ", dealloc_grade,      2)
   print_score("Task 7: ", strbufc_test_grade, 2,
               extra =" (found "+str(rawc)+" bugs)")

   c_score = translate_grade + dealloc_grade + strbufc_test_grade
   score = is_strbuf_grade+strbuf_basic_grade+strbuf_add_grade+\
           strbuf_test0_grade+c_score
   scoreboard = (1 if is_strbuf_grade    == 4 else 0) +\
                (1 if strbuf_basic_grade == 3 else 0) +\
                (1 if strbuf_add_grade   == 5 else 0) +\
                (1 if strbuf_test0_grade == 4 else 0) +\
                (1 if translate_grade    == 5 else 0) +\
                (1 if dealloc_grade      == 2 else 0) +\
                (1 if strbufc_test_grade == 2 else 0) +\
                0

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: "+str(score)
   print json.dumps({'scores': {'is_strbuf': is_strbuf_grade,
                                'strbuf_basic': strbuf_basic_grade,
                                'strbuf_add': strbuf_add_grade,
                                'unit_tests': strbuf_test0_grade,
                                'translation': c_score},
                     'scoreboard': [scoreboard, raw0, rawc]})

if __name__ == "__main__":
   print "TESTING..."
   main()
