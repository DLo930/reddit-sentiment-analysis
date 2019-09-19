from gradeC0 import *

def test_tests():
   print "="*50
   print "Testing..."

   if not expect_success("correct_impls", "tests on correct implementation"):
      print "\n******** Errors from incorrectly failed test ********\n"
      print open('.tmp.output', 'r').read()
      return 0
   score = 0

   if expect_abort("bad_transform_impl_0"): score += 1
   if expect_abort("bad_transform_impl_1"): score += 1
   if expect_abort("bad_transform_impl_2"): score += 1
   if expect_abort("bad_transform_impl_3"): score += 1
   if expect_abort("bad_transform_impl_4"): score += 1
   if expect_abort("bad_transform_impl_5"): score += 1
   if expect_abort("bad_transform_impl_6"): score += 1
   if expect_abort("bad_transform_impl_7"): score += 1
   if expect_abort("bad_transform_impl_8"): score += 1
   if expect_abort("bad_transform_impl_9"): score += 1
   if expect_abort("bad_transform_impl_A"): score += 1

   if expect_abort("bad_masking_impl_0"): score += 1
   if expect_abort("bad_masking_impl_1"): score += 1
   if expect_abort("bad_masking_impl_2"): score += 1
   if expect_abort("bad_masking_impl_3"): score += 1
   if expect_abort("bad_masking_impl_4"): score += 1
   if expect_abort("bad_masking_impl_5"): score += 1
   if expect_abort("bad_masking_impl_6"): score += 1
   if expect_abort("bad_masking_impl_7"): score += 1
   if expect_abort("bad_masking_impl_8"): score += 1
   if expect_abort("bad_masking_impl_9"): score += 1
   if expect_abort("bad_masking_impl_A"): score += 1

   return score

def main():
   score = 0
   if expect_exists("correct_impls", "tests did not compile"):
      score = test_tests()
      print '='*50
      print "You caught "+str(score)+" of the buggy programs with your tests"
      if score == 0: print "You need better tests to get full lab credit"
      elif score <= 7: print "That's enough for credit; can you do better?"
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
