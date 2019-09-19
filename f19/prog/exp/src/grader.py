# [exp] grader

from gradeC0 import *

# The following flag should be False before we close handins, True after (then regrade)
#FINAL = True
FINAL = False

def test_clac(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (clac implementation)"

   if not expect_exists("clac", "clac.c0 does not compile"):
      return 0
   score = 0.0

   if expect_successes([("clac-d '15 122 +'", 137),
                        ("clac-d '122 15 +'", 137)]): score += 0.5
   if expect_successes([("clac-d '15 122 -'", -107),
                        ("clac-d '122 15 -'", 107)]): score += 0.5
   if expect_successes([("clac-d '1512 2 /'", 756),
                        ("clac-d '15 122 /'", 0),
                        ("clac-d '122 15 /'", 8)]): score += 0.5
   if expect_successes([("clac-d '15 122 *'", 1830),
                        ("clac-d '122 15 *'", 1830)]): score += 0.5
   if expect_successes([("clac-d '1512 2 **'", 2286144),
                        ("clac-d '5 3 **'", 125),
                        ("clac-d '3 5 **'", 243)]): score += 0.5
   if expect_successes([("clac-d '-3 2 **'", 9),
                        ("clac-d '-3 3 **'", -27),
                        ("clac-d '0 0 **'", 1),
                        ("clac-d '3 0 **'", 1),
                        ("clac-d '-3 0 **'", 1)]): score += 0.5

   # Score: 3.0

   if expect_success("clac-d '23 42 81 9 3 -5 + * / - **'",
                     expected_return_value = 1351359601):
      score += 0.5

   if expect_successes([("clac-d '-1948459 -1948459 -1948459 -1948459 * * *'",
                         1957408433),
                        ("clac-d '-2000000000 1000000000 -'", 1294967296),
                        ("clac-d '2000000000 1000000000 +'", -1294967296)],
                       "Tests for modular arithmetic"):
      score += 0.5

   # Score: 4.0

   if expect_errors(["clac '-102 839 234 * - /'",
                     "clac-d '-102 839 234 ** + *'",
                     "clac '-102 839 234 + - +'",
                     "clac-d '-102 839 234 * + **'",
                     "clac '-102 839 234 - - -'",
                     "clac '+'",
                     "clac-d '-'",
                     "clac '*'",
                     "clac-d '/'",
                     "clac '**'",
                     "clac-d '1 +'",
                     "clac '2 *'",
                     "clac-d '-7 /'",
                     "clac '22 **'"]): score += 1.0

   if expect_errors(["clac '12 3 + 999999999999999 -'",
                     "clac '99 2 bogus'"]): score += 0.5

   if expect_errors(["clac '0 0 /'",
                     "clac '16 0 /'",
                     "clac '-2147483648 -1 /'",
                     "clac '55 -1 **'",
                     "clac '0 -2 **'",
                     "clac '-2147483648 -1 **'",
                     "clac '-1 -2147483648 **'"]): score += 0.5

   return score

def test_dict(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (dictionary implementation)"

   if not expect_exists("dict-grade", "dict.c0 does not compile"):
      return 0

   if not expect_exists("isdict-grade", "function is_dict does not exist"):
      return 0

   score = 0.0

   ## Testing is_dict
   if expect_success("isdict-grade empty",
                     "A valid dictionary can't be NULL"): score += 0.25
   if expect_successes(["isdict-grade good",
                        "isdict-grade bad"],
                       "Basic is_dict behavior"): score += 0.25

   ## Testing dictionary itself
   if expect_success("dict-grade empty1"): score += 0.5
   if expect_success("dict-grade empty2"): score += 0.5
   if expect_success("dict-grade singleton1"): score += 0.5
   if expect_successes(["dict-grade singleton2",
                        "dict-grade singleton3",
                        "dict-grade singleton4"]): score += 0.5
   if expect_success("dict-grade basic1"): score += 0.5
   if expect_success("dict-grade basic2"): score += 0.5
   if expect_success("dict-grade invalid1"): score += 0.5
   if expect_successes(["dict-grade invalid2",
                        "dict-grade invalid3"]): score += 1.0
   if expect_successes(["dict-grade few",
                        "dict-grade many",
                        "dict-grade manymore"],
                       "Lots of operators",
                       timeout = 15): score += 1.0

   return score

def test_is_precstack(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (is_precstack data structure invariant)"

   if not expect_exists("precstack-grade", "parse.c0 does not compile"):
      return (0 if FINAL else -1)
   if not FINAL: return 0

   score = 0.0
   if expect_successes(["precstack-grade empty1",
                        "precstack-grade one1",
                        "precstack-grade exp1",
                        "precstack-grade exp2",
                        "precstack-grade exp6"],
                       "Correct return value for is_precstack, basic tests"):
      if expect_successes(["precstack-grade exp3",
                           "precstack-grade exp4",
                           "precstack-grade exp5"],
                          "Checks for strictly-decreasing values"): score += 0.5
      if expect_successes(["precstack-grade one2",
                           "precstack-grade bad1",
                           "precstack-grade bad2",
                           "precstack-grade bad3"],
                          "Correctly handles invalid operators"): score += 0.5

   if expect_successes(["precstack-grade one1 -pure",
                        "precstack-grade exp1 -pure",
                        "precstack-grade exp6 -pure"],
                       "is_precstack leaves stack unchanged " +\
                       "when it returns true"): score += 0.5

   if expect_successes(["precstack-grade exp2 -pure",
                        "precstack-grade exp3 -pure",
                        "precstack-grade exp4 -pure",
                        "precstack-grade exp5 -pure"],
                       "is_precstack leaves stack unchanged " +\
                       "when it returns false"): score += 0.5

   return score

def test_parse(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (parser)"

   if not expect_exists("parse", "parse.c0 does not compile"):
      return (0 if FINAL else -1)
   if not FINAL: return 0

   score = 0.0

   if not expect_successes(["parse   '1 + 1' '1 1 +'",
                            "parse-d '1 + 1' '1 1 +'"],
                           "Basic test cases: " +\
                           "if you don't pass these we give up"): return score

   if expect_successes(["parse   ' ' -fails",
                        "parse-d ' ' -fails"]): score += 0.25

   if expect_successes(["parse   '+' -fails",
                        "parse-d '+' -fails"]): score += 0.25

   if expect_successes(["parse   '1 2 +' -fails",
                        "parse-d '1 2 +' -fails"]): score += 0.25

   if expect_successes(["parse   '1 + 2 -' -fails",
                        "parse-d '1 + 2 -' -fails"]): score += 0.25

   if expect_successes(["parse   '3 + ** 2' -fails",
                        "parse-d '3 + ** 2' -fails"]): score += 0.25

   if expect_successes(["parse   '** 3 + 2' -fails",
                        "parse-d '** 3 + 2' -fails"]): score += 0.25

   if expect_successes(["parse   '** 3 +' -fails",
                        "parse-d '** 3 +' -fails"]): score += 0.5

   if expect_successes(["parse   '4 @ 4' -fails",
                        "parse-d '4 @ 4' -fails"]): score += 0.5


   if expect_successes(["parse   '99' '99'",
                        "parse-d '99' '99'"]): score += 0.5

   if expect_successes(["parse   '1 + 2 + 3' '1 2 + 3 +'",
                        "parse-d '1 + 2 + 3' '1 2 + 3 +'"]): score += 0.5

   if expect_successes(["parse   '1 - 2 + 3' '1 2 - 3 +'",
                        "parse-d '1 + 2 - 3' '1 2 + 3 -'"]): score += 0.5


   if expect_successes(["parse   '1 * 2 + 3 * 4' '1 2 * 3 4 * +'",
                        "parse-d '1 * 2 + 3 * 4' '1 2 * 3 4 * +'"]):
      score += 1.0

   if expect_successes(["parse   '3 * 4 + -9 / 2' '3 4 * -9 2 / +'",
                        "parse-d '3 * 4 + -9 / 2' '3 4 * -9 2 / +'"]):
      score += 1.0

   if expect_successes(["parse   '3 * 4 > -9 / 2 && 3 << 2 == 24 >> 2 - 1'" +\
                        "        '3 4 * -9 2 / > 3 2 << 24 2 1 - >> == &&'",
                        "parse-d '3 * 4 > -9 / 2 && 3 << 2 == 24 >> 2 - 1'" +\
                        "        '3 4 * -9 2 / > 3 2 << 24 2 1 - >> == &&'"]):
      score += 1.0

   return score

def test_runtime(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (implementation of extra functions, in Clac)"

   score = 0.0

   if not expect_exists("exp-defs.clac", "exp-defs.clac does not exist"):
      return 0

   if not expect_success("clac-ref exp-defs.clac 0",
                         "exp-defs.clac does load in clac-ref"):
      return 0

   if expect_successes([("clac-ref exp-defs.clac '0 0 ||'", 0),
                        ("clac-ref exp-defs.clac '0 1 ||'", 1),
                        ("clac-ref exp-defs.clac '1 0 ||'", 1),
                        ("clac-ref exp-defs.clac '1 1 ||'", 1),
                        ("clac-ref exp-defs.clac '0 3 ||'", 1),
                        ("clac-ref exp-defs.clac '-2 0 ||'", 1),
                        ("clac-ref exp-defs.clac '99 5 ||'", 1)]): score += 1.0

   if expect_successes([("clac-ref exp-defs.clac '0 0 &&'", 0),
                        ("clac-ref exp-defs.clac '0 1 &&'", 0),
                        ("clac-ref exp-defs.clac '1 0 &&'", 0),
                        ("clac-ref exp-defs.clac '1 1 &&'", 1),
                        ("clac-ref exp-defs.clac '0 3 &&'", 0),
                        ("clac-ref exp-defs.clac '-2 0 &&'", 0),
                        ("clac-ref exp-defs.clac '99 5 &&'", 1)]): score += 1.0

   if expect_successes([("clac-ref exp-defs.clac '0 0 <<'", 0),
                        ("clac-ref exp-defs.clac '0 1 <<'", 0),
                        ("clac-ref exp-defs.clac '0 2 <<'", 0),
                        ("clac-ref exp-defs.clac '9 0 <<'", 9),
                        ("clac-ref exp-defs.clac '1 1 <<'", 2),
                        ("clac-ref exp-defs.clac '1 3 <<'", 8),
                        ("clac-ref exp-defs.clac '1 31 <<'", -2147483648),
                        ("clac-ref exp-defs.clac '-1 3 <<'", -8),
                        ("clac-ref exp-defs.clac '-154 20 <<'", -161480704),
                        ("clac-ref exp-defs.clac '1 6 <<'", 64)]): score += 1.0

   if expect_successes([("clac-ref exp-defs.clac '0 0 >>'", 0),
                        ("clac-ref exp-defs.clac '0 1 >>'", 0),
                        ("clac-ref exp-defs.clac '0 2 >>'", 0),
                        ("clac-ref exp-defs.clac '1 0 >>'", 1),
                        ("clac-ref exp-defs.clac '32 2 >>'", 8),
                        ("clac-ref exp-defs.clac '99 3 >>'", 12),
                        ("clac-ref exp-defs.clac '99 31 >>'", 0),
                        ("clac-ref exp-defs.clac '2000000000 29 >>'", 3),
                        ("clac-ref exp-defs.clac '2000000000 30 >>'", 1),
                        ("clac-ref exp-defs.clac '2000000000 31 >>'", 0),
                        ("clac-ref exp-defs.clac '9 9 >>'", 0)]): score += 1.0

   return score


def test_extra1(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (bonus -- shifting with error)"

   score = 0.0

   if expect_errors(["clac-ref exp-defs.clac '0 -1 >>'",
                     "clac-ref exp-defs.clac '19 -1 >>'",
                     "clac-ref exp-defs.clac '3 32 >>'",
                     "clac-ref exp-defs.clac '6 99 >>'",
                     "clac-ref exp-defs.clac '0 -1 <<'",
                     "clac-ref exp-defs.clac '19 -1 <<'",
                     "clac-ref exp-defs.clac '3 32 <<'",
                     "clac-ref exp-defs.clac '6 99 <<'"]):
      score += 1.0

   return score


def test_extra2(tasknum):
   print "="*50
   print "Testing task " +str(tasknum)+ " (bonus -- shifting with sign extension)"

   score = 0.0

   if expect_successes([("clac-ref exp-defs.clac '-8 0 >>'", -8),
                        ("clac-ref exp-defs.clac '-8 1 >>'", -4),
                        ("clac-ref exp-defs.clac '-8 2 >>'", -2),
                        ("clac-ref exp-defs.clac '-8 3 >>'", -1),
                        ("clac-ref exp-defs.clac '-8 4 >>'", -1),
                        ("clac-ref exp-defs.clac '-8 31 >>'", -1),
                        ("clac-ref exp-defs.clac '-9 2 >>'", -3),
                        ("clac-ref exp-defs.clac '-27 3 >>'", -4)]):
      score += 1.0

   return score


def main():
   # Prettyprint a score post-release, signals failed compilation pre-release
   okmsg = "Compiles, seems to respect interface. That's all for now!"
   badmsg = "ERROR: does not compile, check output!!!"
   nc_signal = -0.1    # scores that signals a failed compilation pre-release
   def print_final(task, score, max):
      if FINAL:
         print_score(task, score, max)
      else:
         print task+(okmsg if score is 0 else badmsg)

   clac_score         = test_clac(1)
   dict_score         = test_dict(2)
   is_precstack_score = test_is_precstack(3)
   parse_score        = test_parse(4)
   runtime_score      = test_runtime(5)
   runtime_extra = 0
   if FINAL and runtime_score == 4.0:
      runtime_extra     = test_extra1(6)
      runtime_extra    += test_extra2(7)

   print "\n"
   print '='*50
   print_score("Task  1:   ", clac_score,         6)
   print_score("Task  2:   ", dict_score,         6)
   print_final("Task  3:   ", is_precstack_score, 2)
   print_final("Task  4:   ", parse_score,        7)
   print_score("Task  5:   ", runtime_score,      4)
   print_final("Tasks 6&7: ", runtime_extra,      2)


   total_score = clac_score + dict_score + runtime_score
   if FINAL:
      total_score += is_precstack_score + parse_score

   print "*** TOTAL SCORE: "+str(total_score)+"\n"
   if FINAL:
      scores = {'clac':      clac_score,
                'dict':      dict_score,
                'precstack': is_precstack_score,
                'exp':       parse_score,
                'defs':      runtime_score,
                'bonus':     runtime_extra}
   else:
      scores = {'clac': clac_score,
                'dict': dict_score,
                'defs': runtime_score}
      if (is_precstack_score != 0): scores['precstack'] = nc_signal
      if (parse_score        != 0): scores['exp']       = nc_signal

   print json.dumps({'scores':     scores,
                     'scoreboard': [runtime_extra]})

if __name__ == "__main__":
   print "TESTING..."
   main()
