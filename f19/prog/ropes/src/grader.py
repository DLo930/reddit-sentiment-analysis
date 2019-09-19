# ropes grader

from gradeC0 import *

def test_isrope(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_rope)"
   score = 0.0

   if expect_success("isrope-d simpleropes",
                     "Lots of medium-sized, valid ropes"):
      score += 1

   if expect_success("isrope-d edge",
                     "Lots of little edge cases"):
      score += 1

   if expect_success("isrope-d example",
                     "The 'happy birthday!' handout example, plus a half-dozen invalid-rope variations"):
      score += 1

   if expect_success("isrope-d circular",
                     "Ropes that are invalid due to circularity.\n" +\
                     "***     If you're only missing this part, " +\
                     "you should move on and come back to this.\n" +\
                     "***     Also, the 'segfault' result might be due to " +\
                     "non-termination: programs report segfault when they " +\
                     "run out of space on the system stack"):
      score += 1

   return score

def test_basic(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (basic, non-recursive functions)"
   score = 0.0
   if expect_success("basic-d new", "rope_new"): score += 1.5
   if expect_success("basic-d length", "rope_length"): score += 1.5
   if expect_success("basic-d join", "rope_join"): score += 1.5
   score = min(score, 4.0)
   if expect_success("basic huge",
                     "rope_new, rope_length, rope_join for very large ropes"):
      score += 1.0

   return score

def test_rec(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (recursive functions)"
   score = 0.0
   if expect_success("rec-d charat", "rope_charat"): score += 1
   if expect_success("rec charat-huge", "rope_charat for very large (but not very high) ropes"): score += 1
   if expect_success("rec-d tostring", "rope_tostring"): score += 2
   return score

def test_sub(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (rope_sub)"
   score = 0.0
   if expect_success("sub-d simple",
                     "correctness checks (we're not checking for correct " +\
                     "structure sharing, just checking that rope_sub works " +\
                     "like string_sub)"):
      score += 1.0
   if expect_success("sub-d edge", "edge cases"):
      score += 1.5
   if expect_success("sub-d noalloc", "subropes that require no allocation"):
      score += 1.5
   if expect_success("sub-d noshare", "subropes that allow no sharing"):
      score += 1.5
   if expect_success("sub-d someshare",
                     "subropes w/ partial sharing, like the handout example"):
      score += 1.5
   return score

def test_reduce(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (rope_reduce)"
   score = 0.0
   if not expect_success("reduce-d correctness",
                         "Basic correctness tests - checking the strings " +\
                         "that a rope represents aren't changed"):
      return 0.0
   if expect_success("reduce-d edge", "Some edge cases"):
      score += 1.5

   if expect_success("reduce-d examples",
                     "Some tests based on the 'abracadabra' examples"):
      score += 1.5
   if expect_success("reduce more",
                     "Tests inducing interesting sharing patterns"):
      score += 2.0
   return score

def test_tests():
   print "="*50
   print "Testing rope-test.c0 (totally optional)"
   n = 0
   if not os.path.exists("good-ours"):
      print "Looks like you didn't write a rope-test.c0, or you did and it"
      print "doesn't compile. It's not necessary to do this, but if you do"
      print "the number of test cases you help will appear on the scoreboard"
      return 'none'

   if not expect_success("good-ours",
                         "This is your test cases running against our " +\
                         "implementation, which should work",
                         None):
      print "\n******** Errors from incorrectly failed test ********\n"
      print open('.tmp.output', 'r').read()
      return 0

   if not expect_success("good-yours",
                         "Your test cases running against your " +\
                         "implementation. This indicates you have a bug, " +\
                         "but that you also have a test case that catches it!",
                         None):
      print "\n******** Errors from incorrectly failed test ********\n"
      print open('.tmp.output', 'r').read()

   if expect_abort("bug-is_rope1"):  n += 1
   if expect_abort("bug-is_rope2"):  n += 1
   if expect_abort("bug-is_rope3"):  n += 1
   if expect_abort("bug-is_rope3b"): n += 1
   if expect_abort("bug-is_rope4"):  n += 1
   if expect_abort("bug-is_rope5"):  n += 1
   if expect_abort("bug-is_rope6"):  n += 1
   if expect_abort("bug-is_rope7"):  n += 1
   if expect_abort("bug-is_rope8"):  n += 1
   if expect_abort("bug-new1"):      n += 1
   if expect_abort("bug-new2"):      n += 1
   if expect_abort("bug-new3"):      n += 1
   if expect_abort("bug-new4"):      n += 1
   if expect_abort("bug-new5"):      n += 1
   if expect_abort("bug-join1"):     n += 1
   if expect_abort("bug-join2"):     n += 1
   if expect_abort("bug-join3"):     n += 1
   if expect_abort("bug-join4"):     n += 1
   if expect_abort("bug-tostring1"): n += 1
   if expect_abort("bug-tostring2"): n += 1
   if expect_abort("bug-charat1"):   n += 1
   if expect_abort("bug-charat2"):   n += 1
   if expect_abort("bug-sub1"):      n += 1
   if expect_abort("bug-sub2"):      n += 1
   if expect_abort("bug-sub3"):      n += 1
   if expect_abort("bug-sub4"):      n += 1
   if expect_abort("bug-sub5"):      n += 1
   if expect_abort("bug-sub6"):      n += 1
   if expect_abort("bug-sub7"):      n += 1
   if expect_abort("bug-sub8"):      n += 1
   if expect_abort("bug-reduce1"):   n += 1
   if expect_abort("bug-reduce2"):   n += 1
   if expect_abort("bug-reduce3"):   n += 1
   if expect_abort("bug-reduce4"):   n += 1
   if expect_abort("bug-reduce5"):   n += 1
   if expect_abort("bug-reduce6"):   n += 1
   if expect_abort("bug-reduce7"):   n += 1

   return n

def main():
   # changed all of these to be the correct names from above
   isrope_score = test_isrope(1)
   basic_score = test_basic(2)
   rec_score = test_rec(3)
   sub_score = test_sub(4)
   reduce_score = test_reduce(5)
   testcases = test_tests()

   print '='*50
   print_score("Task 1: ", isrope_score, 4)
   print_score("Task 2: ", basic_score,  5)
   print_score("Task 3: ", rec_score,    4)
   print_score("Task 4: ", sub_score,    7)
   print_score("Task 5: ", reduce_score, 5)

   total_score = isrope_score + basic_score + rec_score + sub_score + reduce_score

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: ",
   print total_score

   # Print JSON results and exit
   print json.dumps({'scores': {'isrope': isrope_score,
                                'basic': basic_score,
                                'rec': rec_score,
                                'sub': sub_score,
                                'reduce': reduce_score},
                     'scoreboard': [testcases]})

if __name__ == "__main__":
   print "TESTING..."
   main()
