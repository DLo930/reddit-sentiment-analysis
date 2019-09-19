# [clac] grader

from gradeC0 import *

def test_arith(tasknum):
   print "-"*50
   print "Testing Task " +str(tasknum)+ " (arithmetic expressions)"

   score = 0.0

   # in case of expect success, run demo-d (not demo)
   # 23 42 81 9 3 -5 + * / % -

   # 1 2 3 print print print 0
   # 837 39 % quit 39 *
   if expect_success("clac-d grade/demo-s5.clac", "Print failed", 0) and \
          expect_success("clac-d grade/demo-s6.clac", "Quit failed", 18):
      score += 0.75

   # -1948459 -1948459 -1948459 -1948459 * * *
   # -2000000000 1000000000 -
   # 2000000000 1000000000 +
   if expect_successes([("clac-d grade/demo-s2.clac", 1957408433),
                        ("clac-d grade/demo-s2b.clac", 1294967296),
                        ("clac-d grade/demo-s2c.clac", -1294967296),
                        ("clac-d grade/demo-s2d.clac", -825430623)],
                       "Tests for modular arithmetic (+, -, *, **)"):
      score += 1.5

   if expect_successes([("clac-d grade/divmod-s1.clac", -2147483647),
                        ("clac-d grade/divmod-s2.clac", 0),
                        ("clac-d grade/divmod-s3.clac", 2147483647),
                        ("clac-d grade/divmod-s4.clac", 0),
                        ("clac-d grade/divmod-s5.clac", -2147483648),
                        ("clac-d grade/divmod-s6.clac", 0),
                        ("clac-d grade/divmod-s7.clac", 0),
                        ("clac-d grade/divmod-s8.clac", 0)],
                       "Division and modulo"):
      score += 1.5

   if expect_success("clac-d grade/demo-s1.clac",
                     "23 42 81 9 3 -5 + * / % -", 21):
      score += 1.5

   if expect_successes([("clac-d grade/demo-s3b.clac", 1),
                        ("clac-d grade/demo-s3c.clac", 0),
                        ("clac-d grade/demo-s3d.clac", 0),
                        ("clac-d grade/demo-s3e.clac", 1),
                        ("clac-d grade/demo-s3f.clac", 0)],
                       "Comparison operation (<)"):
      score += 0.75

   # -13 14 < 100 * 12 -15 < 10 * + 45 45 < 1 - +
   if expect_success("clac-d grade/demo-s3.clac",
                     "Comparison operation (<) in combination with arithmetic",
                     99):
      score += 0.75

   # only test failure cases if score is at least 1 at this point
   if score >= .7:
      if expect_errors(["clac grade/demo-f1.clac",
                        "clac-d grade/demo-f1.clac"],
                       "Arithmetic on short stack did not signal error"):
         score += 0.75

      if expect_errors(["clac grade/demo-f4.clac",
                        "clac-d grade/demo-f4.clac"],
                       "Out of range integer did not signal error"):
         score += 0.75

      if expect_errors(["clac grade/demo-f5.clac",
                        "clac-d grade/demo-f5.clac",
                        "clac grade/demo-f6.clac",
                        "clac-d grade/demo-f6.clac"],
                       "Division/modulo did not signal an error"):
         score += 0.75

   return score

def test_manip(tasknum):
   print "-"*50
   print "Testing Task " +str(tasknum)+ " (stack manipulations and conditionals)"

   score = 0

   if expect_successes([("clac-d grade/demo-s7.clac", 1),
                        ("clac-d grade/demo-s7b.clac", 1),
                        ("clac-d grade/demo-s7c.clac", 4)],
                       "Tests for drop (uses some arithmetic)"):
      score += 0.5

   if expect_successes([("clac-d grade/demo-s8.clac", 2),
                        ("clac-d grade/demo-s8b.clac", 3),
                        ("clac-d grade/demo-s8c.clac", -5),
                        ("clac-d grade/demo-s8d.clac", 5)],
                       "Tests for swap (uses some arithmetic)"):
      score += 0.5

   if expect_successes([("clac-d grade/demo-s9.clac", -5),
                        ("clac-d grade/demo-s9b.clac", 21),
                        ("clac-d grade/demo-s9c.clac", -3)],
                       "Tests for rot (uses some arithmetic)"):
      score += 0.5

   # 1 7 13 1 pick rot - rot drop swap -
   if expect_success("clac-d grade/demo-s4.clac",
                     "1 7 13 1 pick rot - rot drop swap -", -7):
      score += 0.5

   if score > .7:
      if expect_errors(["clac grade/demo-f2.clac",
                        "clac-d grade/demo-f2.clac",
                        "clac grade/demo-f2b.clac",
                        "clac-d grade/demo-f2b.clac",
                        "clac grade/demo-f2c.clac",
                        "clac-d grade/demo-f2c.clac"],
                       "Stack operations on short stack did not signal error"):
         score += 0.5


      if expect_errors(["clac grade/demo-f3.clac",
                        "clac-d grade/demo-f3.clac"],
                       "Undefined symbol did not signal error"):
         score += 0.5

      if expect_successes([("clac-d grade/skip-s1.clac", 12),
                           ("clac-d grade/skip-s2.clac", 3),
                           ("clac-d grade/skip-s3.clac", 5)],
                          "skip tests failed"):
         score += 0.5

      if expect_errors(["clac-d grade/skip-f1.clac",
                        "clac-d grade/skip-f2.clac"],
                       "Errors for skip did not signal error"):
         score += 0.25

   if expect_successes([("clac-d grade/cond-s0.clac", 2),
                        ("clac-d grade/cond-s1.clac", -9),
                        ("clac-d grade/cond-s2.clac", 19)],
                       "simple conditional tests (if+skip) failed"):
      if expect_success("clac-d grade/cond-s3.clac",
                        "if without skip or skip without if failed", 142):
         if expect_success("clac-d grade/cond-s4.clac",
                           "try running '0 if 2 3 9'"):
            if expect_success("clac-d grade/cond-s5.clac",
                              "try running '1 skip 2'"):
               score += 0.75

      if expect_errors(["clac-d grade/cond-f1.clac",
                        "clac-d grade/cond-f2.clac",
                        "clac-d grade/cond-f3.clac"],
                       "Errors for if did not signal error"):
         score += 0.25


   if expect_successes([("clac-d grade/pick-s1.clac", 5),
                        ("clac-d grade/pick-s2.clac", 4),
                        ("clac-d grade/pick-s3.clac", 3),
                        ("clac-d grade/pick-s4.clac", 2),
                        ("clac-d grade/pick-s5.clac", 1)],
                       "Basic pick tests failed"):
      score += 0.5

      if expect_errors(["clac-d grade/pick-f1.clac",
                        "clac-d grade/pick-f2.clac",
                        "clac-d grade/pick-f3.clac"],
                       "Errors for pick did not signal error"):
         score += 0.25

   perf_msg = "Failure on tests with a very large stack size\n" +\
       "*** If these tests fail due to a timeout, then the autograder\n" +\
       "*** suspects this is because you have implemented an O(n)\n" +\
       "*** stack_size function. Don't do that."
   if expect_successes([("clac grade/clac-1000.clac", 4004),
                        ("clac grade/clac-10000.clac", 40004),
                        ("clac grade/clac-100000.clac", 400004)],
                       perf_msg):
      score += 1.5

   return score

def test_dict(tasknum):
   print "-"*50
   print "Testing Task " +str(tasknum)+ " (dict)"

   score = 0.0

   if expect_success("dict-d -test 1",
                     "Lookup in empty dictionary did not return NULL", 0):
      score += 0.5

   if expect_success("dict-d -test 2", "Insert or lookup failed", 0):
      score += 1

   if expect_success("dict-d -test 3",
                     "Lookup of undefined symbol did not return NULL", 0):
      score += 0.5

   if expect_success("dict-d -test 4", "Redefinition of symbol failed", 0):
      score += 1

   if expect_success("dict-d -test 5", "Aliasing queues failed", 0):
      score += 0.5

   # only give these points if they're mostly there
   if score > 2.2:
      if expect_abort("dict-d -test 6",
                      "Invalid dictionary did not signal contract violation"):
         score += 0.5

   return score

def test_defs(tasknum):
   print "-"*50
   print "Testing Task " +str(tasknum)+ " (definitions)"
   score = 0.0

   if not expect_success("clac-d grade/clac-const.clac",
                         "Defining a constant function and then using it \n" +\
                            "*** (try ': zero 0 ; zero'). Giving up for now."):
      return 0

   if expect_success("clac-d grade/clac-op.clac",
                     "Giving a new name to a built-in operation failed.\n" +\
                        "*** (try '2 : plus + ; 2 plus')",
                     4):
      score += 0.5

   if expect_success("clac-d grade/clac-noop.clac",
                     "Defining and using a noop failed.\n" +\
                        "*** (try '2 : noop ; noop 2 noop noop + noop')",
                     4):
      score += 0.5

   if expect_success("clac-d grade/clac-s0.clac",
                     "Multiple non-recursive definitions failed", 321):
      score += 0.75

   if expect_success("clac-d grade/clac-rec1.clac",
                     "Deeply nested non-recursive definitions failed", 100):
      score += 0.5

      if expect_success("clac-d grade/clac-rec2.clac",
                        "Non recursive but out-of-order definitions, like ': a b ; : b 15 ; a'", 100):
         score += 0.25

   if expect_success("clac-d grade/clac-rec3.clac",
                     "Attempts to leave lots of empty queues on the stack",
                     144):
      score += 0.5

   if expect_successes([("clac grade/clac-rec100.clac", 110),
                        ("clac grade/clac-rec1000.clac", 1010),
                        ("clac grade/clac-rec10000.clac", 10010),
                        ("clac grade/clac-rec100000.clac", 100010)],
                       "Tests that recursion is an O(1) operation and that " +\
                       "recursion is implemented with a callstack as in the " +\
                       "handout.\n" +\
                       "*** If you implemented recursion by calling eval() recursively, you are likely to fail this test."):
      score += 0.75

   if expect_success("clac-d grade/clac-recquit.clac",
                     "Quit from within a function call",
                     22):
      score += 0.5

   if expect_success("clac-d grade/clac-zero.clac grade/clac-one.clac grade/clac-plus.clac grade/clac-usedefs.clac",
                     "Checking that the dictionary is preserved across calls to eval()", 2):
      score += 0.75

   if expect_success("clac-d grade/clac-s1.clac",
                     "Full test suite failed",
                     172):
      score += 0.5

   if expect_success("clac-d grade/clac-s3.clac",
                     "Tests that we can define, but not use, a function named '+'", 20):
      if expect_error("clac-d grade/clac-f1.clac",
                      "Tests that an unknown token will raise error()"):
         if expect_error("clac-d grade/clac-f2.clac",
                         "Definition not terminated by ';' " + \
                            "did not raise an error"):
            score += 0.5

   return score

def test_clac_prog(tasknum):
   print "-"*50
   print "Testing Task " +str(tasknum)+ " (Clac program)"
   score = 0.0
   if not os.path.exists("log.clac"):
      print "No log.clac file -- skipping this task"
      return score
   if expect_success("clac-d log-test.clac",
                     "Your Clac program for log did not run correctly",
                     6):
      score += 3.0
   return score

def main():
   # changed all of these to be the correct names from above
   arith_score = test_arith(1)
   manip_score = test_manip(2)
   #dict_score = test_dict(3)
   defs_score = test_defs(3)
   prog_score = test_clac_prog(4)

   print '='*50
   print_score("Task 1: ", arith_score, 9)
   print_score("Task 2: ", manip_score, 7)
   #print "Task 3: ", dict_score)
   print_score("Task 3: ", defs_score,  6)
   print_score("Task 4: ", prog_score,  3)

   total_score = arith_score+manip_score+defs_score+prog_score

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: ",
   print total_score

   # Print JSON results and exit
   print json.dumps({'scores': {'arith': arith_score,
                                'manip': manip_score,
                                'defs': defs_score+prog_score},
                     'scoreboard': [total_score]})

if __name__ == "__main__":
   print "TESTING..."
   main()
