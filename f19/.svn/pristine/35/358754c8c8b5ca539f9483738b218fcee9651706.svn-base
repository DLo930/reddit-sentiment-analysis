# [lightsout] grader

from gradeC0 import *

failed_solutions = 0

def board(executable,
          board,
          expected_outcome,
          timeout):
   global failed_solutions

   print "-"*50
   print "Test "+executable+" on "+board
   try:
      proc_id = subprocess.Popen("./"+executable+" "+board,
                                 stderr=open("/dev/null", "w"),
                                 stdout=open(".tmp.output", "w"),
                                 shell=True)
      if timeout <> -1:
         signal.alarm(timeout)
      proc_id.wait()
      output = normalize(proc_id.returncode);
   except Alarm:
      output = STATUS_TIMEOUT()
      proc_id.kill();
      proc_id.wait();

   if (expected_outcome):
      if (output == 0):
         try:
            proc_id = subprocess.Popen("./loplayer "+board+" < .tmp.output",
                                       stdout=open("/dev/null", "w"),
                                       stderr=open("/dev/null", "w"),
                                       shell=True)
            proc_id.wait()
            if timeout <> -1:
               signal.alarm(timeout)
            proc_id.wait()
            output2 = normalize(proc_id.returncode);
         except Alarm:
            output2 = STATUS_TIMEOUT()
            proc_id.kill();
            proc_id.wait();

#         proc_id = subprocess.Popen("./loplayer "+board+" < .tmp.output",
#                                    stdout=open("/dev/null", "w"),
#                                    stderr=open("/dev/null", "w"),
#                                    shell=True)
#         proc_id.wait()
#         if (normalize(proc_id.returncode) == 0):
         if (output2 == 0):
            print "Test on solvable board passed!"
            return True
         elif failed_solutions == 0:
            print "*** Test correctly indicated a solvable board (Task 5)"
            print "*** HOWEVER, the test did NOT produce output that was"
            print "*** accepted as valid by the loplayer (Task 6)."
            print ""
            failed_solutions += 1
            return True
         else:
            print "Test on solvable board passed! (Output was not accepted by loplayer.)"
            failed_solutions += 1
            return True
      elif (output == 1):
         print "*** TEST FAILED! Program reported failure (returned 1),"
         print "*** was expected to report success (return 0)"
         return False
      else:
         print "*** TEST FAILED! Instead of returning 0 (success) as expected"
   else:
      if (output == 1):
         print "Test on board with no solution passed!"
         return True
      elif (output == 0):
         print "*** TEST FAILED! Program reported success (returned 0),"
         print "*** was expected to report failure (return 1)"
         return False
      else: print "*** TEST FAILED! Instead of returning 1 as expected"

   if output == STATUS_TIMEOUT():
      print "*** the autograder timed out after "+str(timeout)+" seconds."
   elif output == STATUS_NOTHING():
      print "*** the file seemse to have not compiled."
   elif output == STATUS_SEGV():
      print "*** a segfault seemes to have occured."
   elif output == STATUS_ABRT():
      print "*** a contract or assertion failed."
   else:
      print "*** The program returned with status code "+str(output)

   return False


def test_bitvector(tasks):
   print "="*50
   print "Testing Tasks " +tasks+ " (bitvector.c)"
   if not expect_exists("bitvector-grade",
                        "Skipping tasks " +tasks+ " (test did not compile w/o -DDEBUG)"):
      return 0
   if not expect_exists("bitvector-grade-d",
                        "Skipping tasks " +tasks+ " (test did not compile w/ -DDEBUG)"):
      return 0

   score = 0.0

   if expect_aborts(["bitvector-grade-d toobig1",
                     "bitvector-grade-d toobig2"],
                    "Precondition tests for bitvector.c"):
      score += 1.5

   if expect_successes(["bitvector-grade stress",
                        "bitvector-grade-d stress"],
                       "Correctness tests for bitvector.c"):
      score += grind_deductions(["bitvector-grade-d stress"],
                                score = 3.5,
                                safety = 1,
                                leaky = 1,
                                timeout = 30,
                                expected_return_value = None)

   if expect_aborts(["bitvector32-small toobig1",
                     "bitvector32-small toobig2",
                     "bitvector32-big toobig1",
                     "bitvector32-big toobig2"],
                    "Precondition tests, Task 2"):
      if expect_successes(["bitvector32-small stress",
                           "bitvector32-big stress"],
                          "Correctness tests, task 2"):
         score += 1.5

   if expect_aborts(["bitvector-tiny toobig1",
                     "bitvector-tiny toobig2",
                     "bitvector-small toobig1",
                     "bitvector-small toobig2",
                     "bitvector-big toobig1",
                     "bitvector-big toobig2"],
                    "Precondition tests, Task 3"):
      if expect_successes(["bitvector-tiny stress",
                           "bitvector-small stress",
                           "bitvector-big stress"],
                          "Correctness tests, task 3"):
         score += 1.5

   return score


def test_ba_ht(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (board-ht.c)"
   if not expect_exists("board-ht-grade",
                        "Skipping task " +str(tasknum)+ " (test did not compile w/o -DDEBUG)"):
      return 0
   if not expect_exists("board-ht-grade-d",
                        "Skipping task " +str(tasknum)+ " (test did not compile w/ -DDEBUG)"):
      return 0

   score = 0.0

   if expect_successes(["board-ht-grade createdestroy",
                        "board-ht-grade-d createdestroy",
                        "board-ht-grade lookup_empty",
                        "board-ht-grade-d lookup_empty"],
                       "Simple tests: just create and free a table (createdestroy), and do lots of lookups on an empty table (lookup_empty)"):
      score += grind_deductions(["board-ht-grade createdestroy",
                                 "board-ht-grade lookup_empty"],
                                score = 1.0,
                                safety = 1.0,
                                leaky = 1.0,
                                timeout = 30,
                                expected_return_value = None)

   if expect_successes(["board-ht-grade add_one_lookup",
                        "board-ht-grade-d add_one_lookup"],
                       "Add one element to the hashtable and do lookups"):
      score += grind_deductions(["board-ht-grade add_one_lookup"],
                                score = 0.5,
                                safety = 0.5,
                                leaky = 0.5,
                                timeout = 30,
                                expected_return_value = None)

   if expect_successes(["board-ht-grade add_two_lookup",
                        "board-ht-grade-d add_two_lookup"],
                       "Add two elements to the hashtable and do lookups"):
      score += grind_deductions(["board-ht-grade add_two_lookup"],
                                score = 0.75,
                                safety = 0.75,
                                leaky = 0.75,
                                timeout = 30,
                                expected_return_value = None)

   if expect_aborts(["board-ht-grade-d add_repeated1",
                     "board-ht-grade-d add_repeated2",
                     "board-ht-grade-d add_repeated3"],
                    "Tests that ht_insert fails if you add a struct containing a board already in the table"):
      score += 0.75

   if expect_successes(["board-ht-grade add_many",
                        "board-ht-grade-d add_many"],
                       "Adds ~100 elements to the hash table"):
      score += grind_deductions(["board-ht-grade add_two_lookup"],
                                score = 1.0,
                                safety = 1.0,
                                leaky = 1.0,
                                timeout = 30,
                                expected_return_value = None)

   if expect_successes(["board-ht-grade add_many_change_test",
                        "board-ht-grade-d add_many_change_test",
                        "board-ht-grade add_many_same_test",
                        "board-ht-grade-d add_many_same_test"],
                       "Adds many structs where the test value happens to be the same"):
      score += 0.5

   if (score >= 1.5):
      if expect_successes(["board-ht-small-grade add_many",
                           "board-ht-small-grade add_many_change_test",
                           "board-ht-small-grade add_many_same_test",
                           "board-ht-big-grade add_many",
                           "board-ht-big-grade add_many_change_test",
                           "board-ht-big-grade add_many_same_test"],
                          "Runs earlier tests on implementations of bitvectors that use uint8_t and uint64_t instead of uint32_t"):
         score += 0.75

      if expect_successes(["board-ht-array-grade add_many",
                           "board-ht-array-grade add_many_change_test",
                           "board-ht-array-grade add_many_same_test"],
                          "Runs earlier tests on a representation of " +\
                          "bitvectors as arrays of boolean values\n" +\
                          "*** Likely to fail if you use == instead of " +\
                          "bitvector_equal() to check for equality anywhere,\n" +\
                          "*** or otherwise violate the interface."):
         score += 0.75

   return score


def test_lightsout(tasks):
   print "="*50
   print "Testing Task " +tasks+ " (lightsout.c)"
   if not expect_exists("lightsout",
                        "Skipping tasks " +tasks+ " (test did not compile w/o -DDEBUG)"):
      return 0.0
   if not expect_exists("lightsout-d",
                        "Skipping tasks " +tasks+ " (test did not compile w/ -DDEBUG)"):
      return 0.0

   score = 0.0
   global failed_solutions

   # Basic:
   if board("lightsout", "boards/2x2-0.txt", True, 5) and\
      board("lightsout", "boards/2x2-1.txt", True, 5) and\
      board("lightsout", "boards/2x2-2.txt", True, 5) and\
      board("lightsout", "boards/2x2-3.txt", True, 5) and\
      board("lightsout", "boards/2x2-4.txt", True, 5) and\
      board("lightsout", "boards/2x2-5.txt", True, 5) and\
      board("lightsout", "boards/2x2-6.txt", True, 5) and\
      board("lightsout", "boards/2x2-D.txt", True, 5) and\
      board("lightsout", "boards/2x2-E.txt", True, 5) and\
      board("lightsout", "boards/2x2-F.txt", True, 5) and\
      board("lightsout-d", "boards/3x2-00.txt", True, 10) and\
      board("lightsout",   "boards/3x2-00.txt", True, 10) and\
      board("lightsout-d", "boards/3x2-31.txt", True, 10) and\
      board("lightsout",   "boards/3x2-31.txt", True, 10) and\
      board("lightsout-d", "boards/3x2-3F.txt", True, 10) and\
      board("lightsout",   "boards/3x2-3F.txt", True, 10) and\
      board("lightsout-d", "boards/3x2-12.txt", True, 10) and\
      board("lightsout",   "boards/3x2-12.txt", True, 10) and\
      board("lightsout",   "boards/3x2-34.txt", True, 10):
      successes = True
      if failed_solutions == 0: score += 2.0
      if board("lightsout-d", "boards/3x2-2F.txt", False, 20) and\
         board("lightsout",   "boards/3x2-2F.txt", False, 15) and\
         board("lightsout-d", "boards/3x2-10.txt", False, 20) and\
         board("lightsout",   "boards/3x2-10.txt", False, 15):
         score += grind_deductions(["lightsout boards/3x2-10.txt",
                                    "lightsout boards/2x2-F.txt",
                                    "lightsout boards/3x2-12.txt",
                                    "lightsout boards/3x2-00.txt"],
                                   score = 2.5,
                                   safety = 1.0,
                                   leaky = 1.0,
                                   timeout = 30,
                                   expected_return_value = None)

         # Error conditions:
         if expect_errors(["lightsout-d",
                           "lightsout",
                           "lightsout-d not-a-real-board.txt",
                           "lightsout not-a-real-board.txt"],
                          "Make sure to 'return 1' on error conditions"):
            score += grind_deductions(["lightsout",
                                       "lightsout not-a-real-board.txt"],
                                      score = 1.0,
                                      safety = 1.0,
                                      leaky = 1.0,
                                      timeout = 5,
                                      expected_return_value = None)

   # Additional unseen boards:
   if board("lightsout", "boards/4x4-other-7.txt", True, 10) and\
      board("lightsout", "boards/4x4-other-no.txt", False, 10):
      score += 0.5
      if failed_solutions == 0: score += 1.0
      if board("lightsout", "boards/3x4-manysteps.txt", True, 10) and\
         board("lightsout", "boards/5x5-5moves.txt", True, 10):
         score += 0.5
         if failed_solutions == 0: score += 1.0


   print '-'*50
   print 'Testing a 5x6 board with alternate 32-bit bitvectors'
   print 'Testing for respecting the interface!'
   if board("lightsout2", "boards/5x6-3moves.txt", True, 10) and\
      board("lightsout2", "boards/3x2-10.txt", False, 15) and\
      board("lightsout2-d", "boards/3x2-10.txt", False, 15) and\
      board("lo-small", "boards/2x2-D.txt", True, 5) and\
      board("lo-large", "boards/7x6.txt", True, 5) and\
      board("lo-large", "boards/3x2-10.txt", False, 15):
      score += 1.0

      if board("lightsout-bitvec-is-bool-arr",
               "boards/3x2-12.txt", True, 15) and\
         board("lightsout-bitvec-is-bool-arr",
               "boards/3x2-34.txt", True, 15) and\
         board("lightsout-bitvec-is-bool-arr",
               "boards/3x2-22.txt", False, 30):
         score += 0.75

      if failed_solutions == 0: score += 0.75

   return score

def challenge():
   print "="*50
   print "Challenge boards!"
   score = 0

   tot = 0.0
   thistime = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if board("lightsout", "boards/5x4-verymany.txt", True, 40):
      score += 1
      tot += resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - thistime
   thistime = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if board("lightsout", "boards/board0.txt", False, 40):
      score += 1
      tot += resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - thistime
   thistime = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if board("lightsout", "boards/board2.txt", True, 40):
      score += 1
      tot += resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - thistime
   thistime = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if board("lightsout", "boards/board1.txt", True, 40):
      score += 1
      tot += resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - thistime
   thistime = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if board("lightsout", "boards/board3.txt", True, 40):
      score += 1
      tot += resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - thistime

   if failed_solutions > 0: return ("*","*")
   if tot > 0.0 and tot < 0.05: tot = 0.05
   return (score, tot)


def main():
   bitvector_grade = test_bitvector("1-3")
   ba_ht_grade = test_ba_ht(4)
   lightsout_grade = test_lightsout("5-6")

   print '='*50
   print_score("Tasks 1-3: ", bitvector_grade,  8)
   print_score("Task 4:    ", ba_ht_grade,      6)
   print_score("Tasks 5-6: ", lightsout_grade, 11)
   score = bitvector_grade + lightsout_grade + ba_ht_grade
   scoreboard = (1 if bitvector_grade == 8.0 else 0) +\
                (1 if ba_ht_grade == 6.0 else 0) +\
                (1 if lightsout_grade == 11.0 else 0)

   if score == 25: (bonusboards, totaltime) = challenge()
   else: (bonusboards, totaltime) = ("*", "*")

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: "+str(score)

   # Print JSON results and exit
   print json.dumps({'scores': {'bitvectors': bitvector_grade,
           'hashtable': ba_ht_grade,
           'lightsout': lightsout_grade},
           'scoreboard': [scoreboard, bonusboards, totaltime]})

if __name__ == "__main__":
   print "TESTING..."
   main()
