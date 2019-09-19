# queues grader

from gradeC0 import *

def test_is_queue(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_queue)"
   score = 0.0

   if expect_successes(["is_queue-d emp",
                        "is_queue-d nonemp",
                        "is_queue-d NULL"],
                       "basic is_queue tests"):
      score += 0.5
   else: return 0.0

   if expect_successes(["is_queue-d emp_back_not_NULL",
                        "is_queue-d nonemp_back_next_not_NULL"],
                       "checks specified vs. unspecified parts of the spec"):
      score += 0.5

   if expect_successes(["is_queue-d wrong_length"],
                       "length checks"):
      score += 0.5

   if expect_successes(["is_queue-d circular"],
                       "some circular queues"):
      score += 0.5

   return score

def test_constant(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (usual queue interface)"
   score = 0.0

   if expect_success("constant-d new"): score += 0.5

   if expect_aborts(["constant-d size_precon1",
                     "constant-d size_precon2"]): score += 0.2
   if expect_success("constant-d size"): score += 0.3

   if expect_aborts(["constant-d enq_precon1",
                     "constant-d enq_precon2"]): score += 0.1
   if expect_success("constant-d enq"): score += 0.275

   if expect_aborts(["constant-d deq_precon1",
                     "constant-d deq_precon2",
                     "constant-d deq_precon3"]): score += 0.1
   if expect_success("constant-d deq"): score += 0.275

   if expect_success("constant-d NULLs-are-allowed"): score += 0.25

   return score

def test_linear(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (extended queue interface)"
   score = 0.0

   if expect_aborts(["linear-d peek_precon1",
                     "linear-d peek_precon2",
                     "linear-d peek_precon3",
                     "linear-d peek_precon4"]): score += 0.25
   if expect_success("linear-d peek"): score += 0.75

   if expect_aborts(["linear-d reverse_precon1",
                     "linear-d reverse_precon2"]): score += 0.15
   if expect_success("linear-d reverse-empty"): score += 0.35
   if expect_success("linear-d reverse-correctly"):
      score += 0.5
      if expect_success("linear-d reverse-without-new-allocation"): score += 1.0

   return score

def test_generic(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (generic operations on queues)"
   score = 0.0

   if expect_aborts(["generic-d all_precon1",
                     "generic-d all_precon2",
                     "generic-d all_precon3"]): score += 0.5
   if expect_success("generic-d all"): score += 1.0

   if expect_aborts(["generic-d iterate_precon1",
                     "generic-d iterate_precon2",
                     "generic-d iterate_precon3"]): score += 0.5
   if expect_success("generic-d iterate"): score += 1.0

   return score

def test_use(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (arguments for generic operations on queues)"
   score = 0.0

   if expect_aborts(["use-d even:char",
                     "use-d odd:char",
                     "use-d incr:char"],
                    "Cases where preconditions should fail"):
      score += 0.5

   if expect_successes(["use-d even:NULL",
                        "use-d odd:NULL",
                        "use-d incr:NULL"],
                       "Cases where functions should be able to handle NULL"):
      score += 0.5

   if expect_successes(["use-d even:4",
                        "use-d even:5",
                        "use-d even:0",
                        "use-d even:-3",
                        "use-d even:-4"]): score += 0.5

   if expect_successes(["use-d odd:4",
                        "use-d odd:5",
                        "use-d odd:0",
                        "use-d odd:-4",
                        "use-d odd:-5"]): score += 0.5

   if expect_success("use-d incr:int"): score += 0.5

   if expect_aborts(["use-d findneg:wrongtag_1",
                     "use-d findneg:wrongtag_2",
                     "use-d copy:wrongtag",
                     "use-d copy:NULL",
                     "use-d insert:NULL1",
                     "use-d insert:NULL2",
                     "use-d insert:NULL3",
                     "use-d insert:wrongtag1",
                     "use-d insert:wrongtag2",
                     "use-d insert:wrongtag3"],
                    "Cases where preconditions should fail"):
      score += 1.0

   if expect_success("use-d find_negative"): score += 0.75
   if expect_success("use-d copy"): score += 0.75
   if expect_success("use-d insert"): score += 1.0

   return score

def test_trans(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (C translation)"
   score = 0.0

   if expect_aborts(["ctest-d size_precon1",
                     "ctest-d size_precon2"]): score += 0.25
   if expect_aborts(["ctest-d enq_precon1",
                     "ctest-d enq_precon2"]): score += 0.25
   if expect_aborts(["ctest-d deq_precon1",
                     "ctest-d deq_precon2",
                     "ctest-d deq_precon3"]): score += 0.25
   if expect_aborts(["ctest-d peek_precon1",
                     "ctest-d peek_precon2",
                     "ctest-d peek_precon3",
                     "ctest-d peek_precon4"]): score += 0.5
   if expect_aborts(["ctest-d rev_precon1",
                     "ctest-d rev_precon2"]): score += 0.5
   if expect_aborts(["ctest-d all_precon1",
                     "ctest-d all_precon2",
                     "ctest-d all_precon3"]): score += 0.5
   if expect_aborts(["ctest-d iter_precon1",
                     "ctest-d iter_precon2",
                     "ctest-d iter_precon3"]): score += 0.5

   if expect_successes(["ctest tests", "ctest-d tests"]):
      score += grind_deductions(["ctest tests", "ctest-d tests"],
                                score = 3.25,
                                leaky = 1,
                                safety = 1.75)
   return score

def test_free(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (deallocation)"
   score = 0.0

   if expect_aborts(["cfree-d free_precon1",
                     "cfree-d free_precon2"]): score += 0.5

   if expect_successes(["cfree tests", "cfree-d tests"]):
      score += grind_deductions(["cfree tests", "cfree-d tests"],
                                score = 2.5,
                                leaky = 1.5,
                                safety = 2.5)
   return score

def main():
   is_queue_score = test_is_queue(1) if os.path.exists("is_queue-d") else 0.0
   constant_score = test_constant(2) if os.path.exists("constant-d") else 0.0
   linear_score   = test_linear(3)   if os.path.exists("linear-d")   else 0.0
   generic_score  = test_generic(4)  if os.path.exists("generic-d")  else 0.0
   use_score      = test_use(5)      if os.path.exists("use-d")      else 0.0
   trans_score    = test_trans(6)    if (os.path.exists("ctest") and os.path.exists("ctest-d")) else 0.0
   free_score     = test_free(7)     if (os.path.exists("cfree") and os.path.exists("cfree-d")) else 0.0

   print '='*50
   print_score("Task 1: ", is_queue_score, 2)
   print_score("Task 2: ", constant_score, 2)
   print_score("Task 3: ", linear_score,   3)
   print_score("Task 4: ", generic_score,  3)
   print_score("Task 5: ", use_score,      6)
   print_score("Task 6: ", trans_score,    6)
   print_score("Task 7: ", free_score,     3)

   total_score = is_queue_score + constant_score + linear_score +\
                 generic_score + use_score + trans_score + free_score

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: ",
   print total_score

   # Print JSON results and exit
   print json.dumps({'scores': {'is_queue':  is_queue_score,
                                'constant':  constant_score,
                                'linear':    linear_score,
                                'generic':   generic_score,
                                'use':       use_score,
                                'translate': trans_score,
                                'free':      free_score,
                             }})

if __name__ == "__main__":
   print "TESTING..."
   main()
