from gradeC0 import *

def test_is_tbuf(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_tbuf)"
   score = 0.0

   if not expect_exists("is_tbuf-grade", "tbuf.c0 did not compile"):
      return score

   if expect_success("is_tbuf-grade okbuf",
                     "Testing is_tbuf on normal, well-formed buffers"):
      score += 1
   else: return score

   if expect_success("is_tbuf-grade NULLbuf",
                     "Testing is_tbuf on structures that aren't tbufs becau" +\
                     "se there are NULL pointers where there shouldn't be"):
      score += 1
   else: return score

   if expect_success("is_tbuf-grade oddbuf",
                     "Test is_tbuf on buffers with unusual structure " +\
                     "that is still allowed by specification"):
      score += 0.5

   if expect_success("is_tbuf-grade one-node",
                     "Tests that a one-node linked list is not a text buffer"):
      if expect_success("is_tbuf-grade bypasspoint",
                        "Cursor is not on the path from start to end"):
         if expect_success("is_tbuf-grade order",
                           "Tests that have start -- cursor -- end in the " +\
                           "wrong order\n" +\
                           "    These tests take a valid tbuf and swap " +\
                           "T->start, T->cursor, and T->end " +\
                           "to make an invalid buffer."):
            score += 1

   if expect_success("is_tbuf-grade handout-figure-A",
                     "First example from page 4 of the handout"):
      if expect_success("is_tbuf-grade handout-figure-B",
                        "Second example from page 4 of the handout"):
         score += 0.5


   if score == 4.0 and \
      expect_success("is_tbuf-grade discovered-1",
                     "This structure needs to return false: " +\
                     "http://pic.cs.cmu.edu/tbuf/baddll-discovered-1.pdf"):

      if expect_success("is_tbuf-grade badalloc",
                        "Poorly-constructed text buffer; you may need to " +\
                        "ask on Piazza for TA help on a test case for this."):
         score += 1

   return score


def test_tbuf(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (tbuf)"
   score = 0.0

   if not expect_exists("tbuf-grade", "tbuf.c0 did not compile"):
      return score

   if expect_success("tbuf-grade new", "tbuf_new"): score += 0.5
   if expect_aborts(["tbuf-grade at_left_NULL",
                     "tbuf-grade at_left_alloc",
                     "tbuf-grade at_left_bad"],
                    "tbuf_at_left preconditions"): score += 0.5
   if expect_success("tbuf-grade at_left", "tbuf_at_left"): score += 0.75
   if expect_aborts(["tbuf-grade at_right_NULL",
                     "tbuf-grade at_right_alloc",
                     "tbuf-grade at_right_bad"],
                    "tbuf_at_right preconditions"): score += 0.5
   if expect_success("tbuf-grade at_right", "tbuf_at_right"): score += 0.75
   if expect_aborts(["tbuf-grade forward_NULL",
                     "tbuf-grade forward_alloc",
                     "tbuf-grade forward_bad",
                     "tbuf-grade forward_end"],
                    "tbuf_forward preconditions"): score += 0.5
   if expect_success("tbuf-grade forward", "tbuf_forward"): score += 1.0
   if expect_aborts(["tbuf-grade backward_NULL",
                     "tbuf-grade backward_alloc",
                     "tbuf-grade backward_bad",
                     "tbuf-grade backward_start"],
                    "tbuf_backward preconditions"): score += 0.5
   if expect_success("tbuf-grade backward", "tbuf_backward"): score += 1.0
   if expect_aborts(["tbuf-grade delete_NULL",
                     "tbuf-grade delete_alloc",
                     "tbuf-grade delete_bad",
                     "tbuf-grade delete_start"],
                    "tbuf_delete preconditions"): score += 0.5
   if expect_success("tbuf-grade delete", "tbuf_delete"): score += 1.0
   if expect_aborts(["tbuf-grade insert_NULL",
                     "tbuf-grade insert_alloc",
                     "tbuf-grade insert_bad"],
                    "tbuf_insert preconditions"): score += 0.5
   if expect_success("tbuf-grade insert", "tbuf_insert"): score += 1.0

   return score


def test_rowcol(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (rowcol)"
   score = 0.0

   if not expect_exists("tbuf-grade", "tbuf.c0 did not compile"):
      return score

   if expect_aborts(["tbuf-grade row_NULL",
                     "tbuf-grade row_alloc",
                     "tbuf-grade row_bad"],
                    "tbuf_row preconditions"): score += 0.25
   if expect_success("tbuf-grade row", "tbuf_row"): score += 0.75

   if expect_aborts(["tbuf-grade col_NULL",
                     "tbuf-grade col_alloc",
                     "tbuf-grade col_bad"],
                    "tbuf_col preconditions"): score += 0.25
   if expect_success("tbuf-grade col", "tbuf_col"): score += 0.75

   return score

def test_is_editor(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (is_editor)"
   score = 0.0

   if not expect_exists("is_editor-grade", "editor.c0 did not compile"):
      return score

   if expect_success("is_editor-grade ok",
                     "Testing is_editor on normal, well-formed buffers"):
      score += 1.0
   else: return score

   if expect_success("is_editor-grade badbuf",
                     "Testing is_editor on buffers with ill-formed buffers"):
      score += 1.0

   if expect_success("is_editor-grade badrowcol",
                     "Testing is_editor on buffers with incorrect row/col " +\
                     "fields"):
      score += 1.0

   return score

def test_editor(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (editor)"
   score = 0.0

   if not expect_exists("editor-grade", "editor.c0 did not compile"):
      return score

   if expect_success("editor-grade-d new", "editor_new"): score += 0.5

   if expect_aborts(["editor-grade-d forward_NULL",
                     "editor-grade-d forward_alloc",
                     "editor-grade-d forward_badpos",
                     "editor-grade-d forward_badbuf"],
                    "editor_forward preconditions"): score += 0.25
   if expect_success("editor-grade-d forward", "editor_forward"):
      score += 0.5
      if expect_success("editor-grade forward_recalculate",
                        "Checks editor-forward doesn't recalculate position"):
         score += 0.5
   if expect_aborts(["editor-grade-d backward_NULL",
                     "editor-grade-d backward_alloc",
                     "editor-grade-d backward_badpos",
                     "editor-grade-d backward_badbuf"],
                    "editor_backward preconditions"): score += 0.5
   if expect_success("editor-grade-d backward", "editor_backward"):
      score += 0.5
      if expect_success("editor-grade backward_recalculate",
                        "Checks editor-backward only recalculates column, " +\
                        "and only when required"):
         score += 0.5
   if expect_aborts(["editor-grade-d delete_NULL",
                     "editor-grade-d delete_alloc",
                     "editor-grade-d delete_badpos",
                     "editor-grade-d delete_badbuf"],
                    "editor_delete preconditions"): score += 0.5
   if expect_success("editor-grade-d delete", "editor_delete"):
      score += 0.5
      if expect_success("editor-grade delete_recalculate",
                        "Checks editor-delete only recalculates column, " +\
                        "and only when required"):
         score += 0.5
   if expect_aborts(["editor-grade-d insert_NULL",
                     "editor-grade-d insert_alloc",
                     "editor-grade-d insert_badpos",
                     "editor-grade-d insert_badbuf"],
                    "editor_insert preconditions"): score += 0.25
   if expect_success("editor-grade-d insert", "editor_insert"):
      score += 0.5
      if expect_success("editor-grade insert_recalculate",
                        "Checks editor-insert doesn't recalculate position"):
         score += 0.5

   return score

def test_editor_extra(tasknum):
   print "="*50
   print "Testing Task " +str(tasknum)+ " (extra editor capabilities)"
   score = 0.0

   if not expect_exists("editor-updown-grade-d", "editor_up and/or editor_down are not implemented"):
      return score

   if expect_aborts(["editor-updown-grade-d up_NULL",
                     "editor-updown-grade-d up_alloc",
                     "editor-updown-grade-d up_badpos",
                     "editor-updown-grade-d up_badbuf"],
                    "editor_up preconditions"):
      if expect_success("editor-updown-grade-d up", "editor_up"):
         score += 0.5

   if expect_aborts(["editor-updown-grade-d down_NULL",
                     "editor-updown-grade-d down_alloc",
                     "editor-updown-grade-d down_badpos",
                     "editor-updown-grade-d down_badbuf"],
                    "editor_down preconditions"):
      if expect_success("editor-updown-grade-d down", "editor_down"):
         score += 1.0

   return score

def main():
   is_tbuf = test_is_tbuf(1)
   tbuf = test_tbuf(2)
   rowcol = test_rowcol(3)
   is_editor = test_is_editor(4)
   editor = test_editor(5)
   extra = test_editor_extra(6) if editor > 5.0 else 0.0

   print "\n"
   print '='*50
   print_score("Task 1: ", is_tbuf,   5)
   print_score("Task 2: ", tbuf,      9)
   print_score("Task 3: ", rowcol,    2)
   print_score("Task 4: ", is_editor, 3)
   print_score("Task 5: ", editor,    6)
   print_score("Task 6: ", extra,     1.5, extra=" bonus")

   score = is_tbuf + tbuf + rowcol + is_editor + editor + extra
   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: "+str(score)
   print json.dumps({'scores': {'is_tbuf': is_tbuf,
                                'tbuf': tbuf,
                                'rowcol': rowcol,
                                'is_editor': is_editor,
                                'editor': editor,
                                'bonus': extra},
                     'scoreboard': [extra]})

if __name__ == "__main__":
   print "TESTING..."
   main()
