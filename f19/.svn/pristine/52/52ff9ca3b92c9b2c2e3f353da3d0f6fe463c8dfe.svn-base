# [images] grader

hwversion = "reflect-blur"
# hwversion = "rotate-mask"

# not installed!!
from PIL import Image # Used to resize images for optional task
from gradeC0 import *

# Written so that the test cases work for either scenerio
def test_tests():
   print "="*50
   print "Testing optional submission of images-test.c0"

   if not expect_success("correct_impls", "tests on correct implementation"):
      print "\n******** Errors from incorrectly failed test ********\n"
      print open('.tmp.output', 'r').read()
      return 0

   score = 1

   if expect_abort("bad_tform_impl_0"): score += 1
   if expect_abort("bad_tform_impl_1"): score += 1
   if expect_abort("bad_tform_impl_2"): score += 1
   if expect_abort("bad_tform_impl_3"): score += 1
   if expect_abort("bad_tform_impl_4"): score += 1
   if expect_abort("bad_tform_impl_5"): score += 1
   if expect_abort("bad_tform_impl_6"): score += 1
   if expect_abort("bad_tform_impl_7"): score += 1
   if expect_abort("bad_tform_impl_8"): score += 1
   if expect_abort("bad_tform_impl_9"): score += 1
   if expect_abort("bad_tform_impl_A"): score += 1

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

def test_imageutil(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (imageutil)"

   if not expect_exists("imageutil-test",
                        "imageutil tests did not compile; skipping"):
      return 0

   correctness_count = 0

   if expect_success("imageutil-test get_row", "issue with get_row"):
      correctness_count += 1

   if expect_success("imageutil-test get_col", "issue with get_column"):
      correctness_count += 1

   if expect_success("imageutil-test is_valid_pixel",
                     "issue with is_valid_pixel"):
      correctness_count += 1

   if expect_success("imageutil-test get_index", "issue with get_index"):
      correctness_count += 1

#   if correctness_count == 4: score = 2
#   elif correctness_count > 0: score = 1
   if correctness_count > 0: score = correctness_count
   else: return 0

   if expect_aborts(["imageutil-test get_row_toobig",
                     "imageutil-test get_row_toosmall",
                     "imageutil-test get_row_invalidsize1",
                     "imageutil-test get_row_invalidsize2",
                     "imageutil-test get_row_invalidsize3",
                     "imageutil-test get_col_toobig",
                     "imageutil-test get_col_toosmall",
                     "imageutil-test get_col_invalidsize",
                     "imageutil-test is_valid_pixel_invalidsize1",
                     "imageutil-test is_valid_pixel_invalidsize2",
                     "imageutil-test is_valid_pixel_invalidsize3",
                     "imageutil-test get_index_toobig1",
                     "imageutil-test get_index_toobig2",
                     "imageutil-test get_index_toosmall1",
                     "imageutil-test get_index_toosmall2",
                     "imageutil-test get_index_invalidsize"],
                    "insufficiently strong preconditions"):
      return score
   else:
      return min(1,score)

   return score

def test_quantize():
   print "="*50
   print "Testing Task 2 (quantize)"
   score = 0

   if not expect_exists("quantize-test",
                        "quantize tests did not compile; skipping"):
      return 0

   # Edge case tests
   if expect_success("quantize-test 10x10-no-aliasing",
                     "Problem with edge cases - " + \
                        "quantize doesn't allocate a new array") and \
      expect_success("quantize-test 1x1-manyvalues",
                     "Problem with edge cases - " + \
                        "quantize does not work on 1x1 images"):
      score += 1

   # Correctness tests
   if expect_success("quantize-comp images/g5.png images/g5-quantize0.png 0",
                     "Incorrect quantize when q_level = 0"):
      score += 1

   if expect_success("quantize-comp images/g5.png images/g5-quantize5.png 5",
                     "Incorrect quantize when q_level = 5"):
      score += 1

   if expect_success("quantize-comp images/g5.png images/g5-quantize6.png 6",
                     "Incorrect quantize when q_level = 6"):
      score += 1

   if expect_success("quantize-comp images/g5.png images/g5-quantize7.png 7",
                     "Incorrect quantize when q_level = 7"):
      score += 1

   # Error tests
   if expect_aborts(["quantize-test size-lies1",
                     "quantize-test size-lies2",
                     "quantize-test size-toosmall1",
                     "quantize-test size-toosmall2",
                     "quantize-test size-invalid",
                     "quantize-test size-quant-toobig",
                     "quantize-test size-quant-toosmall"],
                    "Preconditions on quantize seem to be insufficient"):
      score += 1

   return score

def test_reflect(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (reflect)"
   score = 0

   if not expect_exists("reflect-test",
                        "reflect tests did not compile; skipping"):
      return 0

   # Error tests
   if expect_aborts(["reflect-test size-lies1",
                     "reflect-test size-lies2",
                     "reflect-test size-toosmall1",
                     "reflect-test size-toosmall2",
                     "reflect-test size-invalid"],
                    "Preconditions on reflect seem to be insufficient"):
      score += 2

   # Correctness tests
   if expect_success("reflect-comp images/carnegie.png " \
                        + "images/carnegie-reflect.png",
                     "Incorrect reflect on carnegie.png"):
      score += 1

   if expect_success("reflect-comp images/g5.png images/g5-reflect.png",
                     "Incorrect reflect on g5.png"):
      score += 2

   # Edge case tests
   if expect_successes(["reflect-test 10x10-check-that-result-is-new-array",
                        "reflect-test 1x1-manyvalues",
                        "reflect-test 2x1-1x2"],
                       "Problem uncovered by some unit tests on reflect"):
      score += 3

   return score

def test_rotate(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (rotate)"
   score = 0

   if not expect_exists("rotate-comp",
                        "rotate tests did not compile; skipping"):
      return 0

   # Error tests
   if expect_aborts(["rotate-test size-lies1",
                     "rotate-test size-lies2",
                     "rotate-test size-notsquare",
                     "rotate-test size-toosmall",
                     "rotate-test size-invalid"],
                    "Preconditions on rotate seem to be insufficient"):
      score += 2

   # Correctness tests
   if expect_success("rotate-comp images/carnegie.png " +\
                     "images/carnegie-rotate.png",
                     "Incorrect rotate on carnegie.png"):
      score += 1

   if expect_success("rotate-comp images/scs.png " +\
                     "images/scs-rotate.png",
                     "Incorrect rotate on scs.png"):
      score += 2

   # Edge case tests
   if expect_successes(["rotate-test 10x10-check-that-result-is-new-array",
                        "rotate-test 1x1-manyvalues",
                        "rotate-test 2x2-manyvalues"],
                       "Problem uncovered by some unit tests on rotate"):
      score += 3

   return score

def test_blur(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (blur)"
   score = 0

   if not expect_exists("blur-comp",
                        "blur tests did not compile; skipping"):
      return 0

   # Error tests

   if expect_aborts(["blur-test size-lies1",
                     "blur-test size-lies2",
                     "blur-test size-lies3",
                     "blur-test size-toosmall1",
                     "blur-test size-toosmall2",
                     "blur-test size-toosmall3"],
                    "Preconditions on blur seem to be insufficient (basic)"):
      score += 4

   if expect_aborts(["blur-test size-evenmask",
                     "blur-test size-invalid",
                     "blur-test origin-zero-1x1mask",
                     "blur-test origin-zero-bigmask"],
                    "Preconditions on blur seem to be insufficient\n" +\
                    "*** (trickier, make sure you read the paragraph " +\
                    "above 'TASK 3' on page 6 carefully)"):
      score += 3

   if expect_abort("blur-test size-invalidmask",
                   "Tricky one: make sure the mask width is valid:\n" \
                      + "*** That is, that it can be squared w/o overflow." \
                      + "*** Hint: look back at is_valid_imagesize."):
      score += 1

   if expect_abort("blur-test there-are-negative-nubmbers-lurking",
                   "Check for case where mask has negative numbers"):
      score += 1

   score = score / 3

   # Correctness tests
   if expect_successes(["blur-comp images/scs.png " +\
                        "images/scs-blur.png blur-mask.txt",
                        "blur-comp images/scs.png " +\
                        "images/scs-blur-slightly.png blur-slightly-mask.txt"],
                       "Incorrect blur on scs.png",
                       timeout=15):
      score += 2

   if expect_successes(["blur-comp images/carnegie.png " +\
                        "images/carnegie-blur1.png mask1.txt",
                        "blur-comp images/carnegie.png " +\
                        "images/carnegie-blur2.png mask2.txt",
                        "blur-comp images/carnegie.png " +\
                        "images/carnegie-blur3.png mask3.txt",
                        "blur-comp images/g5.png " +\
                        "images/g5-blur1.png mask1.txt",
                        "blur-comp images/g5.png " +\
                        "images/g5-blur2.png mask2.txt",
                        "blur-comp images/g5.png " +\
                        "images/g5-blur3.png mask3.txt"],
                       "Incorrect blur on other sample images",
                       timeout=30):
      score += 2

   # Edge case tests

   if expect_successes(["blur-test 10x10-check-that-result-is-new-array",
                        "blur-test 1x1img-1x1mask",
                        "blur-test 1x2img-1x1mask",
                        "blur-test 2x2img-1x1mask",
                        "blur-test 1x1img-3x3mask"],
                       "Problem uncovered by some unit tests on blur",
                       timeout=15):
      score += 3

   return score

def test_mask(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (mask)"
   score = 0

   if not expect_exists("mask-comp",
                        "mask tests did not compile; skipping"):
      return 0

   # Correctness tests
   if expect_success("mask-comp images/cmu.png images/cmu-edge.png",
                     "Incorrect mask on cmu.png",
                     timeout=90):
      score += 1

   if expect_success("mask-comp images/g5.png images/g5-edge.png",
                     "Incorrect mask on g5.png",
                     timeout=90):
      score += 1

   if expect_success("mask-comp images/carnegie.png " + \
                        "images/carnegie-edge.png",
                     "Incorrect mask on carnegie.png",
                     timeout=90):
      score += 1

   # Edge case tests
   if expect_successes(["mask-test 10x10-no-aliasing",
                        "mask-test 1x1",
                        "mask-test 3x3"],
                       "Problem with edge cases"):
      score += 3

   if expect_aborts(["mask-test size-lies1",
                     "mask-test size-lies2",
                     "mask-test size-toosmall1",
                     "mask-test size-toosmall2",
                     "mask-test size-toosmall3",
                     "mask-test size-invalid",
                     "mask-test size-evenmask"],
                    "Preconditions on apply_mask seem to be insufficient"):
      score += 2

   if expect_abort("mask-test size-invalidmask",
                   "Tricky one: make sure the mask width is valid:\n" \
                      + "*** That is, that it can be squared w/o overflow." \
                      + "*** Hint: look back at is_valid_imagesize."):
      score += 2

   # Error tests

   return score

# Requires Images package
def make_thumbnail(input_img, output_img):
#   max_size = 140, 140
   max_size = 130, 130
   img = Image.open(input_img)
   img.thumbnail(max_size)
   img.save(output_img)
   return


def test_manipulate(tasknum):
   print "="*50
   print "Testing bonus Task " +str(tasknum)+ " (manipulate)"

   if not expect_exists("manipulate-test",
                        "manipulate tests did not compile; skipping"):
      return 0

   if os.path.exists("manipulate.png"):
      print "PLAN: RUN IMAGE MANIPULATION ON manipulate.png"
      input_png = "manipulate.png"
   elif os.path.exists("images/manipulate.png"):
      print "PLAN: RUN IMAGE MANIPULATION ON images/manipulate.png"
      input_png = "images/manipulate.png"
   else:
      print "PLAN: RUN IMAGE MANIPULATION ON images/g5.png"
      print "*** NOTE: If you want to submit your own file for manipulation,"
      print "*** you must name the file manipulate.png and separately submit"
      print "*** that file when youn hand in your work."
      input_png = "images/g5.png"

   if not expect_success("manipulate-test "+input_png,
                         "Image manipulation test did not run correctly.",
                         timeout=120):
      return 0

   if not expect_exists("output.png",
                        "Image manipulation did not correctly produce output"):
      return 0

   make_thumbnail(input_png, 'input-thumb.png')
   make_thumbnail('output.png', 'output-thumb.png')

   return 1


def main():
   imageutil_score = test_imageutil(1)

   #quantize_score = test_quantize()
   #invert_score = test_invert()

   (transform_score, masking_score) = (0,0)
   if hwversion == "rotate-mask":
      transform_score = test_rotate(2)
      masking_score = test_mask(3)
   if hwversion == "reflect-blur":
      transform_score = test_reflect(2)
      masking_score = test_blur(3)

   manipulate_score = test_manipulate(5)

   testcase_score = test_tests()

   # Test: getting output image to work, in the most naive possible fashion
   tiny_uri = open('images/tinytestpattern.png', 'rb').read().encode('base64').replace('\n','')

   if manipulate_score == 1:
      if os.path.exists('input-thumb.png'):
         thumb_uri = open('input-thumb.png', 'rb').read().encode('base64').replace('\n', '')
         input_tag = thumb_uri
      else: input_tag = tiny_uri

      if os.path.exists('output-thumb.png'):
         thumb_uri = open('output-thumb.png', 'rb').read().encode('base64').replace('\n', '')
         output_tag = thumb_uri
      else: output_tag = tiny_uri
   else:
      input_tag = tiny_uri
      output_tag = tiny_uri

#
#   print "*** FINAL SCORE: "+str(total_score)+"\n"

   total_score = imageutil_score + transform_score + masking_score

   print '='*50
   print "Task 0: 0/0 + 3 points that will be graded by hand"
   print_score("Task 1: ", imageutil_score,  4)
   print_score("Task 2: ", transform_score,  8)
   print_score("Task 3: ", masking_score,   10)
   print "*** TOTAL SCORE: "+str(total_score)

   print json.dumps({'scores': {'imageutil': imageutil_score,
                                'transform': transform_score,
                                'masking': masking_score},
                     'scoreboard': [testcase_score,
                                    output_tag
                                    ]})

if __name__ == "__main__":
   print "TESTING..."
   main()
