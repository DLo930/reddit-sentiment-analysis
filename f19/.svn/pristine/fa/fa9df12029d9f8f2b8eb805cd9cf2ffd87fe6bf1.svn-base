# HW [editor] grader

from gradeC0 import *
# Assignment-specific implementation

def test_is_gapbuf(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_gapbuf)"

   if not expect_exists("gapbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return (0, False)

   rawscore = 0.0
   unusable_is_gapbuf = False

   if expect_success("gapbuf-grade is_gapbuf-size1-empty",
                     "size-1 gap buffer containing 'a'"):
      rawscore += 1
   else: unusable_is_gapbuf = True # Avoid is_gapbuf = \x.false attack

   if expect_success("gapbuf-grade is_gapbuf-size1-full",
                     "valid full size-1 gap buffer (there are two of them)"):
      rawscore += 1

   if expect_success("gapbuf-grade is_gapbuf-size1-badstartend",
                     "size-1 gap buffer with gap_end < gap_start"):
      rawscore += 1

   if expect_success("gapbuf-grade is_gapbuf-NULL", "is_gapbuf(NULL)"):
      rawscore += 1
   else: unusable_is_gapbuf = True

   if expect_success("gapbuf-grade is_gapbuf-size0",
                     "0-length gap buffer should be invalid"):
      rawscore += 1
   else: unusable_is_gapbuf = True

   if expect_abort("gapbuf-grade is_gapbuf-invalidlength",
                   "struct where limit not equal to \length(buffer)"):
      rawscore += 1

   if expect_success("gapbuf-grade is_gapbuf-size1-stuff",
                     "your is_gapbuf function shouldn't care about the " +\
                         "specific characters contained in either \n" +\
                         "*** the buffer or the gap"):
      rawscore += 1

   if expect_success("gapbuf-grade is_gapbuf-size16",
                     "testing is_gapbuf on all valid size 16 buffers"):
      rawscore += 1

   if expect_success("gapbuf-grade is_gapbuf-size10-spotchecks",
                     "unit tests on a size 10 gap buffer"):
      rawscore += 1

   if rawscore == 9: score = 4.0
   elif rawscore >= 6: score = 3.0
   elif rawscore >= 4: score = 2.0
   elif rawscore >= 3: score = 1.0
   else: score = 0

   return (score, unusable_is_gapbuf)

def test_gapbuf_util(tasknum, unusable_is_gapbuf):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (gapbuf utility functions)"

   if not expect_exists("gapbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return (0, False)

   score = 0.0
   if unusable_is_gapbuf:
       print "*** Skipping contract tests because is_gapbuf is insufficient"
   elif expect_aborts(["gapbuf-grade empty-NULL",
                       "gapbuf-grade empty-size0",
                       "gapbuf-grade full-NULL",
                       "gapbuf-grade full-size0",
                       "gapbuf-grade at_left-NULL",
                       "gapbuf-grade at_left-size0",
                       "gapbuf-grade at_right-NULL",
                       "gapbuf-grade at_right-size0"],
                      "gapbuf utility functions seem to lack contracts"):
      score += 2
   if expect_success("gapbuf-grade empty", "check gapbuf_empty()"):
      score += 1
   if expect_success("gapbuf-grade full", "check gapbuf_full()"):
      score += 1
   if expect_success("gapbuf-grade at_left", "check gapbuf_at_left()"):
      score += 1
   if expect_success("gapbuf-grade at_right", "check gapbuf_at_right()"):
      score += 1

   return score

def test_gapbuf_interface(tasknum, unusable_is_gapbuf):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (gapbuf interface functions)"
   if not expect_exists("gapbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return 0

   score = 0.0
   if unusable_is_gapbuf:
      print "*** Skipping contract tests because is_gapbuf is wrong"
   else:
      if expect_aborts(["gapbuf-grade new-0",
                        "gapbuf-grade new-negative",
                        "gapbuf-grade forward-NULL",
                        "gapbuf-grade forward-size0",
                        "gapbuf-grade backward-NULL",
                        "gapbuf-grade backward-size0",
                        "gapbuf-grade insert-NULL",
                        "gapbuf-grade insert-size0",
                        "gapbuf-grade delete-NULL",
                        "gapbuf-grade delete-size0",
                        "gapbuf-grade delete-left"],
                       "gapbuf interface functions seem to lack contracts"):
         score += 2

      if expect_aborts(["gapbuf-grade run '^'",
                        "gapbuf-grade run '<'",
                        "gapbuf-grade run '>'",
                        "gapbuf-grade run 'a>'",
                        "gapbuf-grade run 'a^^'",
                        "gapbuf-grade run 'a<^'",
                        "gapbuf-grade run 'a<<'",
                        "gapbuf-grade run 'a<>>'",
                        "gapbuf-grade run '12345' -bufsize 4",
                        "gapbuf-grade run '1234<<5' -bufsize 4",
                        "gapbuf-grade run '1234<<<<5' -bufsize 4"],
                       "unit tests for gapbuf interface functions"):
         score += 1

   if expect_successes(["gapbuf-grade run 'abc' -bufsize 3 -mimic",
                        "gapbuf-grade run 'abc<<<>>>' -bufsize 3 -mimic",
                        "gapbuf-grade run 'abc^^^def<<^g' -bufsize 3 -mimic",
                        "gapbuf-grade run 'abcd<<<<e>>>>' -bufsize 5",
                        "gapbuf-grade run 'abcd<<<<e>>>>' -bufsize 16",
                        "gapbuf-grade run " +\
                            "grade/test-gapbuf-example-from-writeup.txt " +\
                            "-bufsize 16 -mimic"],
                       "unit tests for gapbuf interface functions"):
      score += 1


   if expect_successes(["gapbuf-grade run grade/test-gapbuf.txt " +\
                            "-bufsize 16 -mimic",
                        "gapbuf-grade run grade/test-gapbuf.txt " +\
                            "-bufsize 17 -mimic",
                        "gapbuf-grade run grade/test-gapbuf.txt " +\
                            "-bufsize 50 -mimic"],
                       "unit tests for gapbuf interface functions"):
      score += 2

   return score

def test_is_dll_pt(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (is_dll_pt)"

   if not expect_exists("dll_pt-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return (0, False)

   score = 0.0
   rawscore = 0.0
   unusable_is_dll_pt = False

   if expect_successes(["dll_pt-grade is_dll_pt -contents 'a'",
                        "dll_pt-grade is_dll_pt -contents 'ab'",
                        "dll_pt-grade is_dll_pt -contents 'abc'",
                        "dll_pt-grade is_dll_pt -contents " +\
                           "'supercalifragilisticexpialidocious'"],
                       "is_dll_pt run on valid buffers " +\
                          "(all valid point positions tested)"):
      rawscore += 1
   else: unusable_is_dll_pt = True

   if expect_success("dll_pt-grade is_dll_pt-NULL",
                     "is_dll_pt(NULL)"):
      rawscore += 0.5
   else: unusable_is_dll_pt = True

   if expect_success("dll_pt-grade is_dll_pt-badalloc",
                     "is_dll_pt(B), where B->everything == NULL"):
      rawscore += 0.5
   else: unusable_is_dll_pt = True

   if expect_successes(["dll_pt-grade is_dll_pt_ends -contents 'a'",
                        "dll_pt-grade is_dll_pt_ends -contents 'ab'",
                        "dll_pt-grade is_dll_pt_ends -contents 'abc'",
                        "dll_pt-grade is_dll_pt_ends -contents " +\
                           "'supercalifragilisticexpialidocious'",
                        "dll_pt-grade is_dll_pt_ends -contents ''"],
                       "is_dll_pt run on structure where " +\
                          "point=start or point=end or point=NULL"):
      rawscore += 0.5

   if expect_success("dll_pt-grade is_dll_pt-unspec -contents 'abc'",
                     "Unspecified fields can be anything!"):
      rawscore += 0.5

   if expect_successes(["dll_pt-grade is_dll_pt-null1",
                        "dll_pt-grade is_dll_pt-null2",
                        "dll_pt-grade is_dll_pt-null3",
                        "dll_pt-grade is_dll_pt-null4",
                        "dll_pt-grade is_dll_pt-null5",
                        "dll_pt-grade is_dll_pt-null6",
                        "dll_pt-grade is_dll_pt-null7",
                        "dll_pt-grade is_dll_pt-null8",
                        "dll_pt-grade is_dll_pt-null9",
                        "dll_pt-grade is_dll_pt-nullA",
                        "dll_pt-grade is_dll_pt-nullB"],
                       "is_dll_pt run on structures with lurking NULLs"):
      rawscore += 1

   proceed_with_fullout = True
   if expect_successes(["dll_pt-grade handout-figure-3 -contents 'ab'",
                        "dll_pt-grade handout-figure-4 -contents 'ab'"],
                       "Pointer examples from handout"):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "This test checks a structure that is nearly a doubly-linked\n" +\
       "*** list, except that B->start has been replaced by some random\n" +\
       "*** other node that is not reachable by following pointers from\n" +\
       "*** B->point or B->end.\n" +\
       "*** \n" +\
       "*** Picture: http://www.cs.cmu.edu/~rjsimmon/15122-f13/hw/dll4.pdf"
   if expect_success("dll_pt-grade is_dll_pt-out9 -contents 'ab'", note):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "This test checks a structure that is nearly a doubly-linked\n" +\
       "*** list, except that B->end has been replaced by some random\n" +\
       "*** other node that is not reachable by following pointers from\n" +\
       "*** B->point or B->start.\n" +\
       "*** \n" +\
       "*** Picture: http://www.cs.cmu.edu/~rjsimmon/15122-f13/hw/dll5.pdf"
   if expect_success("dll_pt-grade is_dll_pt-outB -contents 'ab'", note):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "This test checks a structure that is nearly a doubly-linked\n" +\
       "*** list, except that B->start->next->prev has been replaced by\n" +\
       "*** some random other node that is not reachable by following\n" +\
       "*** pointers forward from B->start.\n" +\
       "*** \n" +\
       "*** Picture: http://www.cs.cmu.edu/~rjsimmon/15122-f13/hw/dll6.pdf"
   if expect_success("dll_pt-grade is_dll_pt-out7 -contents 'ab'", note):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "This test checks a structure that is nearly a doubly-linked\n" +\
       "*** list, except that B->end->prev has been replaced by\n" +\
       "*** some random other node that is not reachable by following\n" +\
       "*** pointers forward from B->start.\n" +\
       "*** \n" +\
       "*** Picture: http://www.cs.cmu.edu/~rjsimmon/15122-f13/hw/dll7.pdf"
   if expect_success("dll_pt-grade is_dll_pt-out5 -contents 'ab'", note):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "This test checks a structure that is nearly a doubly-linked\n" +\
       "*** list, except that the point is not on the path from start to\n" +\
       "*** end.\n" +\
       "*** \n" +\
       "*** Picture: http://www.cs.cmu.edu/~rjsimmon/15122-f13/hw/dll8.pdf"
   if expect_success("dll_pt-grade is_dll_pt-bypasspoint -contents 'ab'", note):
      rawscore += 1
   else: proceed_with_fullout = False

   note = "is_dll_pt run on structures w/o correctly-linked pointers.\n" +\
       "*** \n" +\
       "*** NOTE: It may be rather challenging to find the right test\n" +\
       "*** to use here.\n" +\
       "*** \n" +\
       "*** In this particular instance you should feel free to go to\n" +\
       "*** office or cluster hours and ask a person on course staff\n" +\
       "*** to look at the particular test and draw a picture of the\n" +\
       "*** failing test case.\n" +\
       "*** \n" +\
       "*** TAs: if and when this happens, could you write me a quick\n" +\
       "*** note at least saying which test it was that failed?\n" +\
       "***  - Rob 2/28/2012"

   if proceed_with_fullout and\
          expect_successes(["dll_pt-grade is_dll_pt-bypasspoint",
                            "dll_pt-grade is_dll_pt-out1",
                            "dll_pt-grade is_dll_pt-out2",
                            "dll_pt-grade is_dll_pt-out3",
                            "dll_pt-grade is_dll_pt-out4",
                            "dll_pt-grade is_dll_pt-out5",
                            "dll_pt-grade is_dll_pt-out6",
                            "dll_pt-grade is_dll_pt-out7",
                            "dll_pt-grade is_dll_pt-out8",
                            "dll_pt-grade is_dll_pt-out9",
                            "dll_pt-grade is_dll_pt-outA",
                            "dll_pt-grade is_dll_pt-outB"], note):
      rawscore += 1

   if (rawscore >= 11): score = 5.0
   elif (rawscore >= 9): score = 4.0
   elif (rawscore >= 6): score = 3.0
   elif (rawscore >= 4): score = 2.0
   elif (rawscore >= 2): score = 1.0

   return (score, unusable_is_dll_pt)

def test_dll_pt(tasknum, unusable_is_dll_pt):
   print "="*50
   print "Testing task " +str(tasknum)+ " (dll_pt functions)"
   if not expect_exists("dll_pt-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return 0

   score = 0.0
   if unusable_is_dll_pt:
      print "*** Skipping contract tests because is_dll_pt is wrong"
   else:
      if expect_aborts(["dll_pt-grade dll_pt_at_left-NULL",
                        "dll_pt-grade dll_pt_at_left-badalloc",
                        "dll_pt-grade dll_pt_at_right-NULL",
                        "dll_pt-grade dll_pt_at_right-badalloc",
                        "dll_pt-grade dll_pt_forward-NULL",
                        "dll_pt-grade dll_pt_forward-badalloc",
                        "dll_pt-grade dll_pt_backward-NULL",
                        "dll_pt-grade dll_pt_backward-badalloc",
                        "dll_pt-grade dll_pt_delete-NULL",
                        "dll_pt-grade dll_pt_delete-badalloc"],
                       "dll_pt functions seem to lack contracts"):
         score += 1

      if expect_aborts(["dll_pt-grade run '>' -contents 'a'",
                        "dll_pt-grade run '>' -contents 'ab'",
                        "dll_pt-grade run '>' -contents 'abc'",
                        "dll_pt-grade run '<' -contents 'a'",
                        "dll_pt-grade run '<<' -contents 'ab'",
                        "dll_pt-grade run '<<<' -contents 'abc'",
                        "dll_pt-grade run '^' -contents 'a'",
                        "dll_pt-grade run '^^' -contents 'ab'",
                        "dll_pt-grade run '^^^' -contents 'abc'"],
                       "dll_pt functions, preconditions are expected to fail"):
         score += 1


   if expect_successes(["dll_pt-grade run -contents 's' '' -mimic",
                        "dll_pt-grade run -contents 'st' '<><^' -mimic",
                        "dll_pt-grade run -contents 'steady' '^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' '<^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' " +\
                           "'<<<<^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' " +\
                           "'<<<<<^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' " +\
                           "'<<<<<>>>>>^^^^^' -mimic",
                        "dll_pt-grade run -contents 'steady' " +\
                           "'^<<<<^>>>^<<^>^' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<^>' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<^>>' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<^^>' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<<^>>>' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<<^^>>' -mimic",
                        "dll_pt-grade run -contents 'steady' '<<<<^^^>' -mimic"],
                       "dll_pt functions"):
      score += 2

   return score


def test_is_tbuf(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_tbuf)"
   if not expect_exists("tbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return (0, False)

   can_score = False
   rawscore = 0.0
   unusable_is_tbuf = False

   if expect_successes(["tbuf-grade good1",
                        "tbuf-grade good2",
                        "tbuf-grade good3",
                        "tbuf-grade good8"],
                       "is_tbuf on valid text buffers"):
      can_score = True
   else: unusable_is_tbuf = True

   if expect_successes(["tbuf-grade null",
                        "tbuf-grade alloc",
                        "tbuf-grade nullgap",
                        "tbuf-grade allocgap"],
                       "is_tbuf where some or all gap buffers are invalid"):
      rawscore += 1
   else: unusable_is_tbuf = True

   if expect_successes(["tbuf-grade size",
                        "tbuf-grade mixedsize"],
                       "is_tbuf where some or all gap buffers aren't size 16"):
      rawscore += 1

   if expect_successes(["tbuf-grade full-empty",
                        "tbuf-grade empty-empty"],
                       "is_tbuf where the empty gap buffer invariants " +\
                          "are not respected"):
      rawscore += 1

   if expect_successes(["tbuf-grade aligned1",
                        "tbuf-grade aligned2"],
                       "is-tbuf where alignment invariants are not respected"):
      rawscore += 1

   if can_score: score = rawscore
#   if can_score and rawscore == 4: score = rawscore
#   elif can_score and rawscore == 3: score = 2
#   elif can_score and rawscore >= 1: score = 1
   else: score = 0

   return (score, unusable_is_tbuf)

def test_tbuf_new(tasknum, unusable_is_tbuf):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (tbuf_empty, tbuf_new)"
   if not expect_exists("tbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return 0

   score = 0.0

   if expect_success("tbuf-grade new", "tbuf_new"):
      score += 2

   return score

def test_tbuf_split(tasknum, unusable_is_tbuf):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (tbuf_split_pt)"
   if not expect_exists("tbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return 0

   score = 0.0

   if unusable_is_tbuf:
      print "*** Skipping contract tests because is_tbuf is wrong"
   elif expect_aborts(["tbuf-grade split_pt_bad1",
                       "tbuf-grade split_pt_bad2",
                       "tbuf-grade split_pt_bad3",
                       "tbuf-grade split_pt_bad4",
                       "tbuf-grade split_pt_bad5",
                       "tbuf-grade split_pt_bad6",
                       "tbuf-grade split_pt_bad7",
                       "tbuf-grade split_pt_bad8",
                       "tbuf-grade split_pt_bad9",
                       "tbuf-grade split_pt_badA"],
                      "tbuf_split_pt seems to lack contracts"):
      score += 0.5

   if expect_success("tbuf-grade split_pt1",
                     "tbuf_split fails on 1 node text buffers"):
      score += 1

   if expect_success("tbuf-grade split_pt_dense8",
                     "tbuf_split fails on 8 node text editors " +\
                     "where all the gap buffers are full"):
      score += 1

   if expect_success("tbuf-grade split_pt_sparse8",
                     "tbuf_split fails on 8 node text editors " +\
                     "where all the gap buffers besides the point aren't full"):
      score += 1.5

   return score

def test_tbuf(tasknum, unusable_is_tbuf):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (tbuf functions)"
   if not expect_exists("tbuf-grade",
                        "Skipping task " +str(tasknum)+ " (tests did not compile)"):
      return 0

   score = 0.0

   if expect_aborts(["tbuf-grade forward_bad1",
                     "tbuf-grade forward_bad2",
                     "tbuf-grade forward_bad3",
                     "tbuf-grade forward_bad4",
                     "tbuf-grade forward_bad5",
                     "tbuf-grade forward_bad6"],
                    "tbuf_forward seems to lack contracts"):
      if expect_success("tbuf-grade forward", "tbuf_forward tests",
                        timeout = 30):
         score += 1.25

   if expect_aborts(["tbuf-grade backward_bad1",
                     "tbuf-grade backward_bad2",
                     "tbuf-grade backward_bad3",
                     "tbuf-grade backward_bad4",
                     "tbuf-grade backward_bad5",
                     "tbuf-grade backward_bad6"],
                    "tbuf_backward seems to lack contracts"):
      if expect_success("tbuf-grade backward", "tbuf_backward tests",
                        timeout = 30):
         score += 1.25

   if expect_aborts(["tbuf-grade insert_bad1",
                     "tbuf-grade insert_bad2",
                     "tbuf-grade insert_bad3",
                     "tbuf-grade insert_bad4",
                     "tbuf-grade insert_bad5",
                     "tbuf-grade insert_bad6"],
                    "tbuf_insert seems to lack contracts"):
      if expect_success("tbuf-grade insert", "tbuf_insert tests",
                        timeout = 30):
         score += 1.25

   if expect_aborts(["tbuf-grade delete_bad1",
                     "tbuf-grade delete_bad2",
                     "tbuf-grade delete_bad3",
                     "tbuf-grade delete_bad4",
                     "tbuf-grade delete_bad5",
                     "tbuf-grade delete_bad6"],
                    "tbuf_delete seems to lack contracts"):
      if expect_success("tbuf-grade delete", "tbuf_delete tests",
                        timeout = 30):
         score += 1.25

   return score


"""
   rawscore8 = 0;
   if expect_success("test-task8-c1", "right side split"):
      rawscore8 += 1
   if expect_success("test-task8-c2", "left side split"):
      rawscore8 += 1
   if expect_success("test-task8-c3", "rightwards split discrepancy"):
      rawscore8 += 1
   if expect_success("test-task8-c4", "leftwards split discrepancy"):
      rawscore8 += 1
   if expect_success("test-task8-c5", "rightwards split discrepancy"):
      rawscore8 += 1
   if expect_success("test-task8-c6", "leftwards split discrepancy"):
      rawscore8 += 1
   if expect_success("test-task8-c7", "middle split"):
      rawscore8 += 1

   if rawscore8 == 7: score8 = 2
   elif rawscore8 >= 4: score8 = 1
   else: score8 = 0

   print "="*50
   print "Testing Task 9 (manipulating text buffers)"
   rawscore9 = 0;
   if expect_success("test-task9-c1", "forward_char"):
      rawscore9 += 1
   if expect_success("test-task9-c2", "forward at the edge"):
      rawscore9 += 1
   if expect_success("test-task9-c3", "forward across gapbufs"):
      rawscore9 += 1
   if expect_success("test-task9-c4", "forward with series of edits"):
      rawscore9 += 1
   if expect_success("test-task9-c5", "backward_char"):
      rawscore9 += 1
   if expect_success("test-task9-c6", "backward at the edge"):
      rawscore9 += 1
   if expect_success("test-task9-c7", "backward across gapbufs"):
      rawscore9 += 1
   if expect_success("test-task9-c8", "backward with series of edits"):
      rawscore9 += 1
   if expect_success("test-task9-c9", "insert_char"):
      rawscore9 += 1
   if expect_success("test-task9-c10", "insert_char on full gapbuf"):
      rawscore9 += 1
   if expect_success("test-task9-c11", "insert_char on full gapbuf"):
      rawscore9 += 1
   if expect_success("test-task9-c12", "insert with series of edits"):
      rawscore9 += 1
   if expect_success("test-task9-c13", "delete_char"):
      rawscore9 += 1
   if expect_success("test-task9-c14", "delete on empty"):
      rawscore9 += 1
   if expect_success("test-task9-c15", "delete with series of edits"):
      rawscore9 += 1

   if rawscore9 == 15: score9 = 2
   elif rawscore9 >= 10: score9 = 1
   else: score9 = 0
"""



def main():
   (is_gapbuf_score, bad_gapbuf)  = test_is_gapbuf(1);
   gapbuf_util_score              = test_gapbuf_util(2, bad_gapbuf);
   gapbuf_interface_score         = test_gapbuf_interface(3, bad_gapbuf)
   if FINAL:
      (is_dll_pt_score, bad_dll_pt) = test_is_dll_pt(5)
      dll_pt_score                  = test_dll_pt(6, bad_dll_pt)
      (is_tbuf_score, bad_tbuf)     = test_is_tbuf(7)
      tbuf_new_score                = test_tbuf_new(8, bad_tbuf)
      tbuf_split_score              = test_tbuf_split(9, bad_tbuf)
      tbuf_score                    = test_tbuf(10, bad_tbuf)

   print '='*50
   if not FINAL:
      print_score("Task 1: ", is_gapbuf_score,        4)
      print_score("Task 2: ", gapbuf_util_score,      6)
      print_score("Task 3: ", gapbuf_interface_score, 6)
   else:
      print_score("Task  1: ", is_gapbuf_score,        4, extra=" (FYI -- points were given at checkpoint)")
      print_score("Task  2: ", gapbuf_util_score,      6, extra=" (FYI -- points were given at checkpoint)")
      print_score("Task  3: ", gapbuf_interface_score, 6, extra=" (FYI -- points were given at checkpoint)")
      print "Task  4 (10 points for contracts, checked by hand)"
      print_score("Task  5: ", is_dll_pt_score,  5)
      print_score("Task  6: ", dll_pt_score,  4)
      print_score("Task  7: ", is_tbuf_score,  4)
      print_score("Task  8: ", tbuf_new_score,  2)
      print_score("Task  9: ", tbuf_split_score,  4)
      print_score("Task 10: ", tbuf_score, 5)

   print "\n*** FINISHED!"
   if not FINAL:
      print "*** TOTAL CHECKPOINT SCORE: ",
      print is_gapbuf_score+gapbuf_util_score+gapbuf_interface_score
   else:
      print "*** TOTAL POST-CHECKPOINT SCORE: ",
      print is_dll_pt_score+dll_pt_score+is_tbuf_score+tbuf_new_score+tbuf_split_score+tbuf_score

   # Print JSON results and exit
   if not FINAL:
      print json.dumps({'scores': {'gapbuf': is_gapbuf_score+gapbuf_util_score+gapbuf_interface_score}})
   else:
      print json.dumps({'scores': {'dll_pt': is_dll_pt_score+dll_pt_score,
                                   'tbuf': is_tbuf_score+tbuf_new_score+tbuf_split_score+tbuf_score},
                        'scoreboard': [(0 if is_gapbuf_score < 2 else 1) +\
                                       (0 if gapbuf_util_score < 3 else 1) +\
                                       (0 if gapbuf_interface_score < 3 else 1) +\
                                       (0 if is_dll_pt_score < 4 else 1) +\
                                       (0 if dll_pt_score < 3 else 1) +\
                                       (0 if is_tbuf_score < 3 else 1) +\
                                       (0 if tbuf_new_score < 1 else 1) +\
                                       (0 if tbuf_split_score < 3 else 1) +\
                                       (0 if tbuf_score < 4 else 1)]})

if __name__ == "__main__":
   print "TESTING..."
   main()
