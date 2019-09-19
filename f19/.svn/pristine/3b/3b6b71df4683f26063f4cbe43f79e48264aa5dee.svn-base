# Bloom filters grader

from gradeC0 import *

# The flag UNOFFICIAL is set by the Makefile.
# It should be True for the test case checker (Task 1)
# It should be False for the full test suite
#UNOFFICIAL = True
#UNOFFICIAL = False

def performance(test):
   (code, score) = run_for_result(test, timeout=10)
   print("Test "+test+" gives performance score "+str(score))
   return score

def test_tests(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ", Part 1: finding bugs"

   if not expect_exists("bloom-bad1", "Test cases must compile"):
      return (None, None, None, None, None, 0.0)


   if not expect_successes([("bloom-worst", None),
                            ("bloom-expensive", None),
                            ("bloom-bad1", None),
                            ("bloom-bad2", None),
                            ("bloom-bad3", None),
                            ("bloom-bad4", None),
                            ("bloom-bad5", None),
                            ("bloom-meh1", None),
                            ("bloom-meh2", None),
                            ("bloom-meh3", None),
                            ("bloom-meh4", None),
                            ("bloom-ok1", None),
                            ("bloom-ok2", None),
                            ("bloom-ok3", None)],
                           "Test cases must run on " +\
                           "all correct implementations"):
      return (None, None, None, None, None, 0.0)

   errors_found = 0
   if expect_abort("bloom-broke1"): errors_found += 1
   if expect_abort("bloom-broke2"): errors_found += 1
   if expect_abort("bloom-broke3"): errors_found += 1
   if expect_abort("bloom-broke4"): errors_found += 1
   if expect_abort("bloom-broke5"): errors_found += 1
   if expect_abort("bloom-broke6"): errors_found += 1
   if expect_abort("bloom-broke7"): errors_found += 1
   if expect_abort("bloom-broke8"): errors_found += 1
   if expect_abort("bloom-broke9"): errors_found += 1
   if expect_abort("bloom-brokeA"): errors_found += 1
   if expect_abort("bloom-brokeB"): errors_found += 1
   if expect_abort("bloom-brokeC"): errors_found += 1
   if expect_abort("bloom-brokeD"): errors_found += 1
   if expect_abort("bloom-brokeE"): errors_found += 1
   if expect_abort("bloom-brokeF"): errors_found += 1
   errors_score = min(5.0*errors_found/16.0, 3.0)

   print "="*50
   print("Bugs found: "+str(errors_found)+" out of a possible 15")
   print("Bug finding score: "+str(errors_score)+" out of a possible 3.0")

   print "="*50
   print "Task " +str(tasknum)+ ", Part 2: performance"
   print "The 'bad' implementations all have very deep flaws."
   print "   None of them are Bloom filters as described in Tasks 2-5"
   print "The 'meh' implementations are worse than the Task 2 solution."
   print "   Either they have very bad hash functions or some other limitations"
   print "The 'ok' implementations are all substantially better than the Task 2 solution"
   print "-"*50

   worst = performance("bloom-worst")
   expensive = performance("bloom-expensive")
   bad1 = performance("bloom-bad1")
   bad2 = performance("bloom-bad2")
   bad3 = performance("bloom-bad3")
   bad4 = performance("bloom-bad4")
   bad5 = performance("bloom-bad5")
   meh1 = performance("bloom-meh1")
   meh2 = performance("bloom-meh2")
   meh3 = performance("bloom-meh3")
   meh4 = performance("bloom-meh4")
   ok1 = performance("bloom-ok1")
   ok2 = performance("bloom-ok2")
   ok3 = performance("bloom-ok3")

   print "-"*50
   print "Scoring:"

   score = 0.0
   print("Test bloom-worst has a score of 0 (.5pt)..."),
   if worst == 0:
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("All other scores > 0 (.5pt)..."),
   if min([expensive, bad1, bad2, bad3, bad4, bad5, meh1, meh2, meh3, meh4, ok1, ok2, ok3]) > 0:
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("Test bloom-expensive has a score of 100 (.5pt)..."),
   if (expensive == 100):
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("All other scores < 100 (.5pt)..."),
   if max([worst, bad1, bad2, bad3, bad4, bad5, meh1, meh2, meh3, meh4, ok1, ok2, ok3]) < 100:
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("Average 'bad' score less than average 'meh' scores (.5pt)..."),
   if sum([bad1, bad2, bad3, bad4, bad5])/5.0 < sum([meh1, meh2, meh3, meh4])/4.0:
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("All 'bad' scores less than all 'meh' scores (.5pt)..."),
   badmeh = None
   if max([bad1, bad2, bad3, bad4, bad5]) < min([meh1, meh2, meh3, meh4]):
      badmeh = min([meh1, meh2, meh3, meh4]) - max([bad1, bad2, bad3, bad4, bad5])
      print("yes, separation of "+str(badmeh))
      score += 0.5
   else: print("NO!")

   print("Average 'meh' score less than average 'ok' scores (.5pt)..."),
   if sum([meh1, meh2, meh3, meh4])/4.0 < sum([ok1, ok2, ok3])/3.0:
      print("yes.")
      score += 0.5
   else: print("NO!")

   print("All 'meh' scores less than all 'ok' scores (.5pt)..."),
   mehok = None
   if max([meh1, meh2, meh3, meh4]) < min([ok1, ok2, ok3]):
      mehok = min([ok1, ok2, ok3]) - max([meh1, meh2, meh3, meh4])
      print("yes, separation of "+str(mehok)+".")
      score += 0.5
   else: print("NO!")

   print("All 'bad' scores less than all 'ok' scores (.5pt)..."),
   badok = None
   if max([bad1, bad2, bad3, bad4, bad5]) < min([ok1, ok2, ok3]):
      badok = min([ok1, ok2, ok3]) - max([bad1, bad2, bad3, bad4, bad5])
      print("yes, separation of "+str(badok)+".")
      score += 0.5
   else: print("NO!")


   print "-"*50
   print("Total: "+str(score)+" (score capped at 3.0)")

   total_score = errors_score + min(3.0, score)
   if (score < 2.5):
      score = None
      badok = None
      badmeh = None
      mehok = None

   return (errors_found, score, badok, badmeh, mehok, total_score)

def test_bloom1(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (bloom1.c0)"

   if not (os.path.exists("bloom1-test") \
           and os.path.exists("bloom1") \
           and os.path.exists("bloom1-design")):
      print("*** WARNING: Compilation failure for task 2!")

   if UNOFFICIAL:
      print("*** Not running test suite for now (unofficial grader) ***")
      return (None, None)

   score = 0.0
   if expect_success("bloom1-test",
                     "Fails the test cases YOU wrote",
                     expected_return_value = None, timeout = 10): score += 1.0

   if expect_success("bloom1",
                     "This fails our test cases (which respect the interface)",
                     expected_return_value = None, timeout = 10):
      (code, outcome) = run_for_result("bloom1", timeout=10)
      if code == STATUS_SUCCESS() and code >= 0:
         score += 1.0
         if outcome == 46:
            score += 0.5
         else:
            print "*** PERFORMANCE SCORE: " + str(outcome)
            print "*** ERROR: this does not match what we expected!"
            print "*** This indicates something is wrong with your implementation."
      else:
         print "*** ERROR: Our (interface-respecting) tests cases failed."
         print "*** This suggests that you did not correctly implement the bloom filter interface!"

   if not os.path.exists("bloom1-design"): return score

   if expect_success("bloom1-design emptyadd",
                     "make sure your hash_mul31 algorithm accepts the " +\
                     "empty string \"\" and hashes it to 0"): score += 0.5

   if expect_success("bloom1-design invariant1",
                     "is_bloom(NULL) should return false"): score += 0.5

   if expect_success("bloom1-design invariant2",
                     "is_bloom(B) should return false if B->capacity " +\
                     "(and the length of B->data) is 0"): score += 0.75

   if expect_aborts(["bloom1-design invariant3",
                     "bloom1-design invariant4"],
                    "is_bloom tests, data array is wrong size"): score += 0.75

   if expect_aborts(["bloom1-design new-contracts1",
                     "bloom1-design new-contracts2",
                     "bloom1-design add-contracts1",
                     "bloom1-design add-contracts2",
                     "bloom1-design contains-contracts1",
                     "bloom1-design contains-contracts2"],
                    "checking preconditions of all functions"): score += 1.0

   if expect_success("bloom1-design new",
                     "bloom_new creates bloom_t with the requested capacity"):
      score += 1.0

   return score

def runhash(cmd):
   (code, outcome) = run_for_result("bloom2-hash "+cmd, timeout=20)
   longest = outcome >> 16
   empty = (outcome & 0xFF00) >> 8
   big = outcome & 0xFF

   print "-"*50
   print "Hash function "+cmd
   print "   longest chain (should be <15): "+str(longest)
   print "   empty buckets (should be <40%): "+str(empty)+"%"
   print "   buckets with 5 or more elements (should be <5%): "+str(big)+"%"

   return (longest, empty, big)

def test_hash(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (hash functions in bloom2.c0)"

   if not os.path.exists("bloom2-hash"):
      print("*** ERROR: Compilation failure for task 3!")
      return (0.0, [])
   if UNOFFICIAL:
      print("*** Not running test suite for now (unofficial grader) ***")
      return (None, [])

   print "We test your hash functions by adding 100000 random strings"
   print "to a hash table with size 65536"

   score = 0.0
   if not expect_successes([("bloom2-hash hash1", None),
                            ("bloom2-hash hash2", None),
                            ("bloom2-hash hash3", None)],
                           "Repeatedly hash different strings",
                           timeout = 10): return (score, [])

   (long1, empty1, big1) = runhash("hash1")
   (long2, empty2, big2) = runhash("hash2")
   (long3, empty3, big3) = runhash("hash3")

   long_ = max(long1, long2, long3)
   empty = max(empty1, empty2, empty3)
   big = max(big1, big2, big3)

   if (long_ > 2000): print("Longest chain is far too long (-1.0)")
   elif (long_ > 200):
      print("Longest chain is too long (-0.75)")
      score += 0.25
   elif (long_ > 15):
      print("Longest chain is a bit too long (-0.5)")
      score += 0.5
   else: score += 1.0

   if (empty > 67): print("More than two thirds of buckets are empty! (-1.0)")
   elif (empty > 50):
      print("More than half the buckets are empty! (-0.75)")
      score += 0.25
   elif (empty > 40):
      print("Almost half the buckets are empty! (-0.5)")
      score += 0.5
   else: score += 1.0

   if (big > 15): print("More than 15% of buckets are very full. (-1.0)")
   if (big > 5):
      print("High number of very full buckets. (-0.5)")
      score += 0.5
   else: score += 1.0

   return (score, [long_, empty + big])

def test_getset(tasknum):
   print "="*50
   print "Testing tasks " +str(tasknum)+ " (packing bits in bloom2.c0)"

   if not os.path.exists("bloom2-getset"):
      print("*** WARNING: Compilation failure for task 4!")
      return 0.0
   if UNOFFICIAL:
      print("*** Not running test suite for now (unofficial grader) ***")
      return None

   score = 0.0
   if expect_aborts(["bloom2-getset get-contracts1",
                     "bloom2-getset get-contracts2",
                     "bloom2-getset get-contracts3",
                     "bloom2-getset get-contracts4",
                     "bloom2-getset get-contracts5",
                     "bloom2-getset set-contracts1",
                     "bloom2-getset set-contracts2",
                     "bloom2-getset set-contracts3",
                     "bloom2-getset set-contracts4",
                     "bloom2-getset set-contracts5"],
                    "get_bit and set_bit need the specified contracts"):
      score += 0.5

   if expect_success("bloom2-getset range",
                     "get_bit and set_bit accept all in-range inputs"):
      score += 0.5
      if expect_success("bloom2-getset range",
                        "get_bit and set_bit work as the " +\
                        "specification expects (if you're failing this, " +\
                        "you need to write some test cases for get_bit and " +\
                        "set_bit!)"):
         score += 1.0

   return score

def test_bloom2(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (bloom2.c0)"

   if not (os.path.exists("bloom2-test") \
           and os.path.exists("bloom2") \
           and os.path.exists("bloom2-design")):
      print("*** WARNING: Compilation failure for task 5!")
   if UNOFFICIAL:
      print("*** Not running test suite for now (unofficial grader) ***")
      return (None, None)

   score = 0.0
   outcome = None

   if expect_success("bloom2-test",
                     "Fails the test cases YOU wrote",
                     expected_return_value = None, timeout = 10): score += 0.5

   if expect_success("bloom2",
                     "This fails our test cases (which respect the interface)",
                     expected_return_value = None, timeout = 10):
      score += 0.5

      (code, outcome) = run_for_result("bloom2", timeout=10)
      if code == STATUS_SUCCESS() and code >= 0:
         print "*** PERFORMANCE SCORE (USES OUR TESTS): "+str(outcome)
         if (outcome < 40):
            print "*** Score is < 40. This is worse than the first implementation (-1.5pts)"
            score += 0.5
         elif (outcome < 60):
            print "*** Score is in [40, 60). Barely better than the first implementation (-1pt)"
            score += 1.0
         elif (outcome < 75):
            print "*** Score is in [60, 75).  It's quite possible to do a bit better (-0.5 pts)"
            score += 1.5
         else:
            print "*** Score is >= 75.  Good job!"
            score += 2.0

   if not os.path.exists("bloom2-design"): return (score, outcome)

   if expect_success("bloom2-design invariant1",
                     "is_bloom(NULL) should return false"): score += 0.5

   if expect_success("bloom2-design invariant2",
                     "is_bloom(B) should return false if B->limit " +\
                     "(and the length of B->data) is 0"): score += 0.75

   if expect_aborts(["bloom2-design invariant3",
                     "bloom2-design invariant4"],
                    "is_bloom tests, data array is wrong size"): score += 0.75

   if expect_aborts(["bloom2-design new-contracts1",
                     "bloom2-design new-contracts2",
                     "bloom2-design add-contracts1",
                     "bloom2-design add-contracts2",
                     "bloom2-design contains-contracts1",
                     "bloom2-design contains-contracts2"],
                    "checking preconditions of all functions"): score += 1.0

   if expect_success("bloom2-design new",
                     "bloom_new creates bloom_t with the requested limit"):
      score += 1.0

   return (score, outcome)


def main():
   (errors_found, performance_score, badok, badmeh, mehok, actual_score) = test_tests(1)
   bloom1 = test_bloom1(2)
   (hash_score, hash_scoreboard) = test_hash(3)
   getset = test_getset(4)
   (bloom2, performance) = test_bloom2(5)

   okmsg = "Compiles, seems to respect interface. That's all for now!"
   badmsg = "ERROR: does not compile, check output!!!"

   print "\n"
   print '='*50
   if UNOFFICIAL:
      print_score("Task 1: ", actual_score, 6)
      print "Task 2: unused while assessing Bloom filter test cases"
      print "Task 3: unused while assessing Bloom filter test cases"
      print "Task 4: unused while assessing Bloom filter test cases"
      print "Task 5: unused while assessing Bloom filter test cases"
#      print "Task 2: "+(okmsg if bloom1 is 0 else badmsg)
#      print "Task 3: "+(okmsg if hash_score is 0 else badmsg)
#      print "Task 4: "+(okmsg if getset is 0 else badmsg)
#      print "Task 5: "+(okmsg if bloom2 is 0 else badmsg)
      total_score = actual_score
   else:
      print_score("Task 1: ", actual_score, 6)
      print_score("Task 2: ", bloom1,       7)
      print_score("Task 3: ", hash_score,   3)
      print_score("Task 4: ", getset,       2)
      print_score("Task 5: ", bloom2,       7)
      total_score = actual_score + bloom1 + hash_score + getset + bloom2

   print "*** TOTAL SCORE: "+str(total_score)+"\n"
   if UNOFFICIAL:
      print "Done.\n"
      print json.dumps({'scores': {'test': actual_score},
                        'scoreboard': [errors_found,
                                       performance_score,
                                       badok,
                                       badmeh,
                                       mehok]})
   else:
      print json.dumps({'scores': {'test': actual_score,
                                   'bloom1': bloom1,
                                   'hash': hash_score,
                                   'pack': getset,
                                   'bloom2': bloom2},
                        'scoreboard': [performance] + hash_scoreboard})

if __name__ == "__main__":
   print "TESTING..."
   main()
