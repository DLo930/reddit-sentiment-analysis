# [peg] grader

from gradeC0 import *

def test_moves(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": constructing moves"

   if not expect_exists("peg-moves", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0.0

   score = 0.0

   if expect_aborts(["peg-moves bad-loc1",
                     "peg-moves bad-loc2",
                     "peg-moves bad-loc3",
                     "peg-moves bad-loc4",
                     "peg-moves bad-loc5",
                     "peg-moves bad-loc6",
                     "peg-moves bad-loc7",
                     "peg-moves bad-loc8"],
                    "bad locations to new_move"):
      score += 1

   if expect_aborts(["peg-moves bad-jump1",
                     "peg-moves bad-jump2",
                     "peg-moves bad-jump3",
                     "peg-moves bad-jump4",
                     "peg-moves bad-jump5",
                     "peg-moves bad-jump6",
                     "peg-moves bad-jump7",
                     "peg-moves bad-jump8",
                     "peg-moves bad-jump9",
                     "peg-moves bad-jump10"],
                    "invalid jump to new_move"):
      score += 1

   if expect_success("peg-moves new-moves_good-moves",
                     "Building and taking apart plausible moves"):
      score += 1

   return score


def test_make_move(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": making and undoing moves"

   if not expect_exists("peg-moves", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0.0

   score = 0.0

   if expect_aborts(["peg-moves make-invalid-move1",
                     "peg-moves make-invalid-move2",
                     "peg-moves make-invalid-move3",
                     "peg-moves make-invalid-move4",
                     "peg-moves make-invalid-move6",
                     "peg-moves make-invalid-move7",
                     "peg-moves make-invalid-move8",
                     "peg-moves make-invalid-move9"],
                    "make_move with invalid moves for given board"):
      score += 0.5

   if expect_successes(["peg-moves make-valid-move1",
                        "peg-moves make-valid-move2",
                        "peg-moves make-valid-move3"],
                       "make_move with valid moves for given board"):
      score += 0.5

   if expect_aborts(["peg-moves undo-invalid-move1",
                     "peg-moves undo-invalid-move2",
                     "peg-moves undo-invalid-move3",
                     "peg-moves undo-invalid-move4",
                     "peg-moves undo-invalid-move6",
                     "peg-moves undo-invalid-move7",
                     "peg-moves undo-invalid-move8",
                     "peg-moves undo-invalid-move9"],
                    "undo_move with invalid moves for given board"):
      score += 0.5

   if expect_successes(["peg-moves undo-valid-move1",
                        "peg-moves undo-valid-move2",
                        "peg-moves undo-valid-move3"],
                       "undo_move with valid moves for given board"):
      score += 0.5

   return score

def test_all_moves(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": finding all valid moves"

   if not expect_exists("peg-moves", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0.0

   score = 0.0

   if expect_success("peg-moves all-moves-german",
                     "all-moves on German board"):
      score += 0.5

   if expect_success("peg-moves all-moves-english",
                     "all-moves on English board"):
      score += 0.5

   if expect_success("peg-moves all-moves-solved",
                     "all-moves on a solved board"):
      score += 0.5

   if expect_success("peg-moves all-moves-none",
                     "all-moves on edge case"):
      score += 0.5

   if expect_success("peg-moves all-moves-some",
                     "all-moves on board with a few moves"):
      score += 0.5

   if expect_success("peg-moves all-moves-many",
                     "all-moves on board with many moves"):
      score += 0.5

   return score


def test_peg1_deterministic(tasknum):
   print "Testing "+str(tasknum)+" on some deterministic (=very easy) boards"

   rawscore = 0
   if expect_success("peg1 grade/1a.txt",
                     "Solvable one-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1b.txt",
                     "Solvable two-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1c.txt",
                     "Solvable two-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1d.txt",
                     "Solvable two-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1e.txt",
                     "Solvable two-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1f.txt",
                     "Solvable multi-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1g.txt",
                     "Solvable multi-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1h.txt",
                     "Solvable multi-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1l.txt",
                     "Solvable multi-peg board", timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1i.txt",
                     "Unsolvable multi-peg board",
                     expected_return_value=2, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1j.txt",
                     "Unsolvable multi-peg board",
                     expected_return_value=3, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1k.txt",
                     "Unsolvable multi-peg board (edge conditions)",
                     expected_return_value=28, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1n.txt",
                     "Unsolvable multi-peg board (edge conditions)",
                     expected_return_value=16, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1o.txt",
                       "Unsolvable multi-peg board (edge conditions)",
                       expected_return_value=16, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/1m.txt",
                     "Unsolvable multi-peg board (edge conditions)",
                     expected_return_value=56, timeout=5):
      rawscore += 1

   if   rawscore == 15: score = 2.0
   elif rawscore >= 13: score = 1.5
   elif rawscore >= 11: score = 1.0
   elif rawscore >= 9:  score = 0.5
   else:                score = 0.0

   print "Solved "+str(rawscore)+" out of 15 deterministic boards"
   return (score, rawscore)


def test_peg1(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": peg1"

   if not expect_exists("peg1", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return (0, 0, False)

   (det_score, det_rawscore) = test_peg1_deterministic(tasknum)

   if det_score < 2.0:
      print "You need to be able to solve all deterministic boards before proceeding"
      return (det_score, det_rawscore, False)
   else:
      print "Good job with the deterministic boards.  Let's try something harder"

   rawscore = 0
   if expect_success("peg1 grade/3x4a.txt", "Solvable 3x4 board",
                     timeout=6):
      rawscore += 1
   if expect_success("peg1 grade/3x4b.txt", "Solvable 3x4 board",
                     timeout=6):
      rawscore += 1
   if expect_success("peg1 grade/4x4b.txt", "Solvable 4x4 board",
                     timeout=10):
      rawscore += 1
   if expect_success("peg1 grade/4x5a.txt", "Solvable 4x5 board",
                     timeout=12):
      rawscore += 1
   if expect_success("peg1 grade/4x5d.txt", "Solvable 4x5 board",
                     timeout=12):
      rawscore += 1
   if expect_success("peg1 grade/4x5f.txt", "Solvable 4x5 board",
                     timeout=12):
      rawscore += 1
   if expect_success("peg1 grade/3x3a.txt", "Unsolvable 3x3 board",
                     expected_return_value=4, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/3x3b.txt", "Unsolvable 3x3 board",
                     expected_return_value=7, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/3x3c.txt", "Unsolvable 3x3 board",
                     expected_return_value=8, timeout=5):
      rawscore += 1
   if expect_success("peg1 grade/3x4c.txt", "Unsolvable 3x4 board",
                     expected_return_value=9, timeout=12):
      rawscore += 1
   if expect_success("peg1 grade/4x4a.txt", "Unsolvable 4x4 board",
                     expected_return_value=2, timeout=12):
      rawscore += 1
   if expect_success("peg1 grade/4x4c.txt", "Unsolvable 4x4 board",
                     expected_return_value=2, timeout=12):
      rawscore += 1

   if   rawscore == 12: score = 6.0
   elif rawscore >= 10: score = 5.0
   elif rawscore >= 8:  score = 4.0
   elif rawscore >= 7:  score = 3.0
   else:                score = rawscore / 3

   print "Solved "+str(rawscore)+" out of 12 harder boards"

   score = score + det_score
   rawscore = rawscore + det_rawscore

   if expect_success("peg1 english.txt",
                     "English board (optional)",
                     timeout=12):
      return (score, rawscore, True)
   else: return (score, rawscore, False)

def test_compress(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": compressing boards"

   if not expect_exists("peg-hash", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0.0

   score = 0.0

   if expect_success("peg-hash compress-real",
                     "Equal compression of distinct boards"):
      score += 1

   if expect_success("peg-hash compress-random",
                     "Compression of many random boards"):
      score += 1

   return score

def test_hashing(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": hashing functions"

   if not expect_exists("peg-hash", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return 0.0

   print "Not knowing what you chose for entries and keys, this task is untestable"
   score = 0.0

   return score

def test_peg2(tasknum, peg1_english):
   print "="*50
   print "Task " +str(tasknum)+ ": peg2"

   if not expect_exists("peg2", "Skipping task " +str(tasknum)+ " (test did not compile)"):
      return (0, 0, False)

   if not expect_successes(["peg2 grade/1a.txt",
                            "peg2 grade/1b.txt",
                            "peg2 grade/1g.txt",
                            "peg2 grade/3x4a.txt",
                            ("peg2 grade/1i.txt", 2),
                            ("peg2 grade/1k.txt", 28),
                            ("peg2 grade/1m.txt", 56),
                            ("peg2 grade/3x4c.txt", 9)],
                           "peg2 failed select peg1-2 tests, skipping task " +str(tasknum),
                           timeout=8):
      return (0, 0, False)

   rawscore = 0
   if expect_success("peg2 english.txt", "English board, take 2", timeout=4):
      rawscore += 1
      english_board = True
      if (not peg1_english):
         print "  Good job: your updated solver can handle the English board!"
   else:
      english_board = False
      if peg1_english:
         print "  uh-oh! Your first solver could handle the English board but the new version can't!"

   if expect_success("peg2 grade/4x4c.txt", "Unsolvable 4x4 board",
                     expected_return_value=2, timeout=4):
      rawscore += 1

   if expect_success("peg2 grade/5x5a.txt", "Unsolvable 5x5 board",
                     expected_return_value=2, timeout=20):
      rawscore += 1

   if expect_success("peg2 grade/5x5b.txt", "Unsolvable 5x5 board",
                     expected_return_value=2, timeout=20):
      rawscore += 1

   if expect_success("peg2 grade/5x5c.txt", "Solvable 5x4 board",
                     timeout=10):
      rawscore += 1

   if expect_success("peg2 grade/5x5d.txt", "Unsolvable 5x5 board",
                     expected_return_value=2, timeout=20):
      rawscore += 1

   if expect_success("peg2 grade/5x5e.txt", "Solvable 5x4 board",
                     timeout=10):
      rawscore += 1

   if expect_success("peg2 grade/5x5f.txt", "Unsolvable 5x5 board",
                     expected_return_value=2, timeout=20):
      rawscore += 1

   if   rawscore == 8: score = 7.0
   elif rawscore >= 7: score = 6.0
   elif rawscore >= 6: score = 5.0
   elif rawscore >= 5: score = 4.0
   elif rawscore >= 4: score = 3.0
   elif rawscore >= 3: score = 2.0
   elif rawscore >= 2: score = 1.0
   else:               score = 0.0
   print "Solved "+str(rawscore)+" out of our 8 hardest boards"

   return (score, rawscore, english_board)


def test_bonus():
   print "="*50
   print "Bonus: checking French boards with peg2 ..."

   rawscore = 0

   time1 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if expect_success("peg2 french1.txt", "French1 board", timeout=30):
      rawscore += 1
      time1 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - time1
      print "Time: "+str(time1)
   else:
      time1 = 999

   time2 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if expect_success("peg2 french2.txt", "French2 board", timeout=30):
      rawscore += 1
      time2 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - time2
      print "Time: "+str(time2)
   else:
      time2 = 999

   time3 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
   if expect_success("peg2 french3.txt", "French3 board", timeout=30):
      rawscore += 1
      time3 = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - time3
      print "Time: "+str(time3)
   else:
      time3 = 999

   time = min(time1,time2,time3)


   if rawscore == 3:   score = 2.0
   elif rawscore >= 2: score = 1.0
   else:               score = 0.0
   return (score, rawscore, "n/a" if time > 100 else time)

def main():
   moves_score                          = test_moves(1)
   make_move_score                      = test_make_move(2)
   all_moves_score                      = test_all_moves(3)
   (peg1_score, peg1_raw, peg1_english) = test_peg1(4)
   compress_score                       = test_compress(5)
   hashing_score                        = test_hashing(6)
   (peg2_score, peg2_raw, peg2_english) = test_peg2(7, peg1_english)

   if peg2_english: english = "with peg2"
   elif peg1_english: english = "with peg1"
   else: english = "no"

   if peg2_score > 6:
      (bonus_score, bonus_raw, bonus_time) = test_bonus()
   else:
      bonus_score = 0
      bonus_raw   = 0
      bonus_time  = "n/a"

   total_score = moves_score + make_move_score + all_moves_score + peg1_score \
               + compress_score + hashing_score + peg2_score \
               + bonus_score

   print '='*50
   print_score("Task 1: ", moves_score,     3)
   print_score("Task 2: ", make_move_score, 2)
   print_score("Task 3: ", all_moves_score, 3)
   print_score("Task 4: ", peg1_score,      8, extra=" -- solved "+str(peg1_raw)+" boards")
   print_score("Task 5: ", compress_score,  2)
   print_score("Task 6: ", hashing_score,   0, extra=" -- (this task has no associated points)")
   print_score("Task 7: ", peg2_score,      7, extra=" -- solved "+str(peg2_raw)+" boards")
   print_score("Task 8: ", bonus_score,     2, extra=" (bonus) -- solved "+str(bonus_raw)+" boards")
   print "English board: "+english

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: ",
   print total_score

   # Print JSON results and exit
   print json.dumps({'scores': {'moves' : moves_score + make_move_score + all_moves_score,
                                'peg1': peg1_score,
                                'peg2': compress_score + hashing_score + peg2_score,
                                'bonus': bonus_score},
                     'scoreboard': [peg1_raw + peg2_raw + bonus_raw,
                                    bonus_time,
                                    english]})

if __name__ == "__main__":
   print "TESTING..."
   main()
