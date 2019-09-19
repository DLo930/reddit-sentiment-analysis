# [huffman] grader

from gradeC0 import *

# Global variables
huff_output = "_huff_output"

source_dir     = "data/source/"
freq_dir       = "data/freq/"
binascii_dir   = "data/binascii/"
htree_dir      = "data/htree/"
compressed_dir = "data/compressed/"

basic_tests = [("free coffee",      "free_coffee",        ".txt"),
               ("more free coffee", "more_free_coffee",   ".txt"),
               ("more free coffee", "more_free_coffeeNL", ".txt"),
               ("room for creme",   "room_for_cremeNL",   ".txt"),
               ("nobody's face",    "nobody",             ".jpg")]
adv_tests   = [("Shakespeare",      "shakespeare",        ".txt"),
               ("sonnets",          "sonnets",            ".txt"),
               ("G5",               "g5",                 ".png")]

unrel_tests = [("nothing",
                "-safe",
                "empty.01", "free_coffee", "empty.txt"),
               ("one of a kind",
                "-safe",
                "singleton.01", "free_coffee", "singleton.txt"),
               ("not more free coffee",
                "-safe",
                "free_coffee2.01", "more_free_coffee","free_coffee.txt"),
               ("Two free coffees",
                "-safe",
                "2free_coffee.01", "free_coffee", "2free_coffee.txt"),
               ("128 free coffees",
                "-safe",
                "128free_coffee.01", "free_coffee", "128free_coffee.txt"),
               ("free coffee for Shakespeare",
                "-fast",
                "free_coffee3.01", "shakespeare", "free_coffee.txt"),
               ("free coffee on the go",
                "-fast",
                "free_coffee4.01", "g5", "free_coffee.txt")]


#### Running commands

def run(executable, expected_outcome=0, timeout=5):
   max = 42   # Number of characters of command to print
#   max = 500  # Debug value

   print "-"*50
   print "Test "+executable[0:max]+" ...",
   try:
      proc_id = subprocess.Popen("./"+executable,
                                 stderr=open(".tmp.error", "w"),
                                 stdout=open(".tmp.output", "w"),
                                 shell=True)
      if timeout <> -1:
         signal.alarm(timeout)
      proc_id.wait()
      output = normalize(proc_id.returncode);
   except Alarm:
      output = STATUS_TIMEOUT()
      proc_id.kill();
      proc_id.wait();

   if (output == STATUS_SUCCESS()):
      if (output == expected_outcome):
         print "- good, it ran to completion"
         return True
      else:
         print ""
         print "*** Test_failed: expected execution to abort but it ran to completion"
         return False
   if (output == STATUS_FAILURE()):
      if (output == expected_outcome):
         print "- good, execution aborted, as expected"
         return True
      else:
         print ""
         print "*** TEST FAILED: execution did not succeed"
         return False
   if (output == STATUS_TIMEOUT()):
      print ""
      print "*** TEST FAILED: timeout"
      return False
   print ""
   print "*** TEST FAILED, unexpected outcome:"
   f = open('.tmp.error', 'r')
   print(f.read())
   f.close()
   return False

def run_for_success(cmd, msg, expected_outcome=0, timeout=5):
   if not run(cmd, expected_outcome, timeout):
      print msg;
      return False
   return True

def run_for_successes(executables, msg, expected_outcome=0, timeout=5):
   successes = 0
   for cmd in executables:
      if run_for_success(cmd, msg, expected_outcome, timeout):
         successes += 1
   return successes

def diff(file1, file2, msg):        # diff is not expected to time-out
   command = "diff "+file1+" "+file2
   proc_id = subprocess.Popen(command,
                              stderr=open("/dev/null", "w"),
                              stdout=open(".diff.output", "w"),
                              shell=True)
   proc_id.wait()

   if (os.path.getsize(".diff.output") == 0):
      return True
   print msg
   return False


def test_huff(test, executable, good, type):
   score = 0
   if run(executable):
      if diff(huff_output, good, test + ": incorrect "+type):
         score += 1
      else:
         print test+": "+type+" failed"

   return score


def mk_tests(tests, case, cmd):
   cmd = "./"+cmd
   if case == "build_htree_edge":
      return [(test_name,
               cmd+" -f "+freq_dir+fname+".frq",
               "")
              for (test_name, fname, _) in tests]

   if case == "build_htree"            \
   or case == "htree_to_codetable"     \
   or case == "encode_src":            # Roundtrip
      mid_file = "_result.01"
      return [(test_name,
               cmd+" -E -s "+source_dir+fname+ext
                  +   " -f "+freq_dir+fname+".frq"
                  +   " -a "+mid_file
                  +"; "+
               cmd+" -D -a "+mid_file
                  +   " -f "+freq_dir+fname+".frq"
                  +   " -s ",                            # Left unspecified
               source_dir+fname+ext)
              for (test_name, fname, ext) in tests]

   if case == "decode_src":  # one way from htree file
      return [(test_name,
               cmd+" -D -a "+binascii_dir+fname+".01"
                  +   " -r "+htree_dir+fname+".htr"
                  +   " -s ",                            # Left unspecified
               source_dir+fname+ext)
              for (test_name, fname, ext) in tests]

   if case == "crs_edocne":            # reverse roundtrip
      mid_file = "_result.src"
      return [(test_name,
               cmd+" -D -a "+binascii_dir+fname+".01"
                  +   " -r "+htree_dir+fname+".htr"
                  +   " -s "+mid_file
                  +"; "+
               cmd+" -E -s "+mid_file
                  +   " -r "+htree_dir+fname+".htr"
                  +   " -a ",                            # Left unspecified
               binascii_dir+fname+".01")
              for (test_name, fname, _) in tests]

   if case == "write_freq_table":
      return [(test_name,
               cmd+" -F -s "+source_dir+fname+ext
                  +   " -f ",
               freq_dir+fname+".frq")
              for (test_name, fname, ext) in tests]

   if case == "compress":
      mid_file = "_result.hip"
      return [(test_name,
               cmd+" -C -s "+source_dir+fname+ext
                  +   " -h "+mid_file
                  +"; "+
               cmd+" -U -h "+mid_file
                  +   " -s ",
               source_dir+fname+ext)
              for (test_name, fname, ext) in tests]

   if case == "uncompress":
      return [(test_name,
               cmd+" -U -h "+compressed_dir+fname+ext+".hip"
                  +   " -s ",
               source_dir+fname+ext)
              for (test_name, fname, ext) in tests]

      return [("error", "error", "error")]  # Error

def mk_unrelated_tests(cmd1, tests, case):
   cmd1 = "./"+cmd1
   if case == "decode_src":   # one way from htree file
      return [(test_name,
               cmd1+cmd2+" -D -a "+binascii_dir+bin_file
                        +   " -r "+htree_dir+sym_file+".htr"
                        +   " -s ",                          # Left unspecified
               source_dir+src_file)
              for (test_name, cmd2, bin_file, sym_file, src_file) in tests]

   if case == "htree_to_codetable"     \
   or case == "encode_src":            # roundtrip
      mid_file = "_result.01"
      return [(test_name,
               cmd1+cmd2+" -E -s "+source_dir+src_file
                        +   " -f "+freq_dir+sym_file+".frq"
                        +   " -a "+mid_file
                        +"; "+
               cmd1+cmd2+" -D -a "+mid_file
                        +   " -f "+freq_dir+sym_file+".frq"
                        +   " -s ",                          # Left unspecified
               source_dir+src_file)
              for (test_name, cmd2, _, sym_file, src_file) in tests]

   if case == "crs_edocne":            # reverse roundtrip
      mid_file = "_result.src"
      return [(test_name,
               cmd1+cmd2+" -D -a "+binascii_dir+bin_file
                        +   " -r "+htree_dir+sym_file+".htr"
                        +   " -s "+mid_file
                        +"; "+
               cmd1+cmd2+" -E -s "+mid_file
                        +   " -r "+htree_dir+sym_file+".htr"
                        +   " -a ",                          # Left unspecified
               binascii_dir+bin_file)
              for (test_name, cmd2, bin_file, sym_file, _) in tests]

   return [("error", "error", "error")]  # Error


def mk_valgrind_tests(tests, type, executable):
   return [cmd+"/dev/null"
            for (_,cmd,_) in mk_tests(basic_tests, type, executable)]

def run_tests(tests, case,  huff="huff-safe"):
   score = 0
   for (name, cmd, ref) in mk_tests(tests, case, huff):
      score += test_huff(name, cmd+" " +huff_output, ref, case)
   return score


#### TEST is_htree*
def test_is_tree(tasknum):
   print "="*50
   print "Task " +str(tasknum)+ ": is_tree & Co"
   print "The tests for this task use:"
   print "- YOUR is_htree, is_htree_leaf, and is_htree_interior"
   print "- (nothing from US besides what's in the starter code)"
   score = 0

   if not os.path.exists("test-htree"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return 0

   good_leaf = ["test-htree is_htree-good-leaf"]
   good_leaf_msg = "Hint: is_htree_leaf too picky!"

   good_inner = ["test-htree is_htree-good-interior"]
   good_inner_msg = "Hint: is_htree_interior too picky!"

   good_excl = ["test-htree is_htree-exclusive"]
   good_excl_msg = "Hint: both a leaf and an interior node?"

   bad_null = ["test-htree is_htree-edge"]
   bad_null_msg = "Hint: consider edge cases!"

   bad_leaf = ["test-htree is_htree-bad-leaf1",
               "test-htree is_htree-bad-leaf2",
               "test-htree is_htree-bad-leaf3",
               "test-htree is_htree-bad-leaf4"]
   bad_leaf_msg = "Hint: is_tree_leaf too liberal"

   bad_inner = ["test-htree is_htree-bad-interior1",
                "test-htree is_htree-bad-interior2"]
   bad_inner_msg = "Hint: is_tree_interior too liberal"

   small_tests = ["test-htree is_htree-free_coffee",
                  "test-htree is_htree-more_free_coffee",
                  "test-htree is_htree-nobody"]
   small_tests_msg = "Hint: small tests from the data directory"

   big_tests = ["test-htree is_htree-more_free_coffee2",
                "test-htree is_htree-room_for_creme",
                "test-htree is_htree-sonnets",
                "test-htree is_htree-shakespeare",
                "test-htree is_htree-g5"]
   big_tests_msg = "Hint: large or tricky tests"

   good_leaf_score = run_for_successes(good_leaf, good_leaf_msg) \
                  / len(good_leaf)

   good_inner_score = run_for_successes(good_inner, good_inner_msg) \
                  / len(good_inner)

   good_excl_score = run_for_successes(good_excl, good_excl_msg) \
                  / len(good_excl)

   bad_leaf_score = run_for_successes(bad_leaf, bad_leaf_msg) \
                  / len(bad_leaf)

   bad_inner_score = run_for_successes(bad_inner, bad_inner_msg) \
                  / len(bad_inner)

   bad_null_score = run_for_successes(bad_null, bad_null_msg) \
                  / len(bad_null)

   small_score = run_for_successes(small_tests, small_tests_msg) \
                  / len(small_tests)

   big_score = run_for_successes(big_tests, big_tests_msg) \
                  / len(big_tests)

   leaf_score = 0
   if good_leaf_score <> 0 and bad_leaf_score <> 0:
      leaf_score = good_leaf_score + bad_leaf_score

   inner_score = 0
   if good_inner_score <> 0 and bad_inner_score <> 0:
      inner_score = good_inner_score + bad_inner_score

   weird_score = 0
   if good_excl_score <> 0 and bad_null_score <> 0:
      weird_score = good_excl_score + bad_null_score

   score = 2.0 * (  0.1 * leaf_score  \
                  + 0.1 * inner_score \
                  + 0.1 * weird_score \
                  + 0.2 * small_score \
                  + 0.2 * big_score)
   return score


#### TEST build_htree
def test_build_htree(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": build_htree"
   print "The tests for this task use:"
   print "- YOUR is_htree, htree_higher_priority, and build_htree"
   print "- OUR decode_src, htree_to_codetable, and encode_src"
   goodtests = 0; ntests = 0

   if not os.path.exists("huff2-safe"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   print "-"*25
   print "Testing build_htree (basic)"
   good = run_tests(basic_tests, "build_htree", huff="huff2-safe")
   n = len(basic_tests)
   basic_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing build_htree (big ugly files)"
   good = run_tests(adv_tests, "build_htree", huff="huff2-fast")
   n = len(adv_tests)
   adv_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing build_htree (edge cases)"
   edge_tests = [("singleton", "singleton", ""),
                 ("empty",     "empty",     ""),
                 ("empty",     "emptyNL",   "")]
   good = run_for_successes([cmd for (_,cmd,_)
                                  in mk_tests(edge_tests, "build_htree_edge", "huff2-safe")],
                            "Look for invalid Huffman trees",
                            expected_outcome=1)  # Failure
   n = len(edge_tests)
   edge_score = good/n
   goodtests += good; ntests += n

   score = 1.0 * edge_score   \
         + 2.0 * basic_score  \
         + 2.0 * adv_score

   print "-"*25
   print "Testing build_htree (valgrind)"
   tests = mk_valgrind_tests(basic_tests, "build_htree", "huff2-safe")
   tests.extend(mk_valgrind_tests(adv_tests, "build_htree", "huff2-fast"))
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max score = 5


#### TEST decode_src
def test_decode_src(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": decode_src"
   print "The tests for this task use:"
   print "- YOUR is_htree and decode_src"
   print "- (nothing from US besides what's in the starter code)"
   goodtests = 0; ntests = 0

   if not os.path.exists("huff-safe"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   print "-"*25
   print "Testing decode (basic)"
   good = run_tests(basic_tests, "decode_src")
   n = len(basic_tests)
   basic_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing decode (big ugly files)"
   good = run_tests(adv_tests, "decode_src", huff="huff-fast")
   n = len(adv_tests)
   adv_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing decode (unrelated Huffman trees)"
   unr_tests = mk_unrelated_tests("huff", unrel_tests, "decode_src")
   good = 0
   for (name, cmd, ref) in unr_tests:
      good += test_huff(name, cmd+huff_output, ref, "decode_src")
   n = len(unr_tests)
   unr_score = good/n
   goodtests += good; ntests += n

   score = 3.0 * basic_score  \
         + 3.0 * adv_score    \
         + 2.0 * unr_score

   tests = mk_valgrind_tests(basic_tests, "decode_src", "huff-safe")
   tests.extend([cmd+"/dev/null" for (_,cmd,_) in unr_tests])
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max score = 8


#### TEST htree_to_codetable
def test_htree_to_codetable(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": htree_to_codetable"
   print "The tests for this task use:"
   print "- YOUR is_htree, htree_higher_priority, build_htree, and htree_to_codetable"
   print "- OUR decode_src and encode_src"
   goodtests = 0; ntests = 0

   if not os.path.exists("huff3-safe"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   print "-"*25
   print "Testing htree_to_codetable (basic)"
   good = run_tests(basic_tests, "htree_to_codetable", huff="huff3-safe")
   n = len(basic_tests)
   basic_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing htree_to_codetable (big ugly files)"
   good = run_tests(adv_tests, "htree_to_codetable", huff="huff3-fast")
   n = len(adv_tests)
   adv_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing htree_to_codetable (unrelated Huffman trees)"
   unr_tests = mk_unrelated_tests("huff3", unrel_tests, "htree_to_codetable")
   good = 0
   for (name, cmd, ref) in unr_tests:
      good += test_huff(name, cmd+huff_output, ref, "htree_to_codetable")
   n = len(unr_tests)
   unr_score = good/n
   goodtests += good; ntests += n

   score = 1.0 * basic_score  \
         + 1.0 * adv_score    \
         + 1.0 * unr_score

   print "-"*25
   print "Testing htree_to_codetable (valgrind)"
   tests = mk_valgrind_tests(basic_tests, "htree_to_codetable", "huff3-safe")
   tests.extend(mk_valgrind_tests(adv_tests, "htree_to_codetable", "huff3-fast"))
   tests.extend([cmd+"/dev/null" for (_,cmd,_) in unr_tests])
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max score = 3


#### TEST encode
def test_encode_src(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": encode_src"
   print "The tests for this task use:"
   print "- YOUR is_htree, htree_higher_priority, build_htree, decode_src,"
   print "       htree_to_codetable, and encode_src"
   print "- (nothing from US besides what's in the starter code)"
   goodtests = 0; ntests = 0

   if not os.path.exists("huff4-safe"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   # encode-decode roundtrip test
   print "-"*25
   print "Testing encode_src (basic)"
   good = run_tests(basic_tests, "encode_src", huff="huff4-safe")
   n = len(basic_tests)
   basic_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing encode_src (big ugly files)"
   good = run_tests(adv_tests, "encode_src", huff="huff4-fast")
   n = len(adv_tests)
   adv_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing encode_src (unrelated Huffman trees)"
   unr_tests = mk_unrelated_tests("huff4", unrel_tests, "encode_src")
   good = 0
   for (name, cmd, ref) in unr_tests:
      good += test_huff(name, cmd+huff_output, ref, "encode_src")
   n = len(unr_tests)
   unr_score = good/n
   goodtests += good; ntests += n

   # decode-encode reverse roundtrip test
   print "-"*25
   print "Testing encode_src in reverse (basic)"
   good = run_tests(basic_tests, "crs_edocne", huff="huff4-safe")
   n = len(basic_tests)
   basic_score2 = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing encode_src in reverse (big ugly files)"
   good = run_tests(adv_tests, "crs_edocne", huff="huff4-fast")
   n = len(adv_tests)
   adv_score2 = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing encode_src in reverse (unrelated Huffman trees)"
   unr_tests = mk_unrelated_tests("huff4", unrel_tests, "crs_edocne")
   good = 0
   for (name, cmd, ref) in unr_tests:
      good += test_huff(name, cmd+huff_output, ref, "crs_edocne")
   n = len(unr_tests)
   unr_score2 = good/n
   goodtests += good; ntests += n

   score = 0.5 * basic_score  \
         + 0.5 * adv_score    \
         + 0.5 * unr_score    \
         + 0.5 * basic_score2 \
         + 0.5 * adv_score2   \
         + 0.5 * unr_score2

   print "-"*25
   print "Testing encode_src (valgrind)"
   tests = mk_valgrind_tests(basic_tests, "encode_src", "huff4-safe")
   tests.extend(mk_valgrind_tests(adv_tests, "encode_src", "huff4-fast"))
   tests.extend([cmd+"/dev/null" for (_,cmd,_) in unr_tests])
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max = 3


#### TEST build_freqtable
def test_build_freqtable(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": build_freqtable"
   print "The tests for this task use:"
   print "- YOUR build_freqtable"
   print "- (nothing from US besides what's in the starter code)"
   goodtests = 0; ntests = 0

   if not os.path.exists("huff-safe"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   print "-"*25
   print "Testing build_freqtable (basic)"
   good = run_tests(basic_tests, "write_freq_table", huff="huff-fast")
   n = len(basic_tests)
   basic_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing build_freqtable (big ugly files)"
   good = run_tests(adv_tests, "write_freq_table")
   n = len(adv_tests)
   adv_score = good/n
   goodtests += good; ntests += n

   score = 0.5 * basic_score  \
         + 0.5 * adv_score

   print "-"*25
   print "Testing build_freqtable (valgrind)"
   tests = mk_valgrind_tests(basic_tests, "write_freq_table", "huff-safe")
   tests.extend(mk_valgrind_tests(adv_tests, "write_freq_table", "huff-fast"))
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max=1


#### TEST pack/unpack
def test_bitpacking_simple(tasknum):
   goodtests = 0; ntests = 0

   if not os.path.exists("test-pack"):
      print "Skipping Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0)

   print "="*25
   print "The next few tests use YOUR pack in isolation"

   pack_edge_tests = ["test-pack pack-0-bits",
                      "test-pack pack-1-bit"]
   pack_edge_msg = "Hint: pack doesn't work on edge cases"

   pack_few_tests = ["test-pack pack-4-bits",
                     "test-pack pack-7-bits",
                     "test-pack pack-8-bits",
                     "test-pack pack-9-bits"]
   pack_few_msg = "Hint: pack doesn't work on a small number of bits"

   pack_many_tests = ["test-pack pack-many-bits"]
   pack_many_msg = "Hint: pack doesn't work on increasingly many bits"

   pack_file_tests = ["test-pack pack-free-coffee",
                      "test-pack pack-nobody",
                      "test-pack-fast pack-sonnets"]
   pack_file_msg = "Hint: pack doesn't work on binascii files"

   goodtests += run_for_successes(pack_edge_tests, pack_edge_msg)
   ntests += len(pack_edge_tests)

   goodtests += run_for_successes(pack_few_tests, pack_few_msg)
   ntests += len(pack_few_tests)

   goodtests += run_for_successes(pack_many_tests, pack_many_msg)
   ntests += len(pack_many_tests)

   goodtests += run_for_successes(pack_file_tests, pack_file_msg, timeout=15)
   ntests += len(pack_file_tests)


   print "="*25
   print "The next few tests use YOUR unpack in isolation"

   unpack_edge_tests = ["test-pack unpack-0-bytes",
                        "test-pack unpack-1-byte"]
   unpack_edge_msg = "Hint: unpack doesn't work on edge cases"

   unpack_few_tests = ["test-pack unpack-4-bytes",
                       "test-pack unpack-7-bytes",
                       "test-pack unpack-8-bytes",
                       "test-pack unpack-9-bytes"]
   unpack_few_msg = "Hint: unpack doesn't work on a small number of bytes"

   unpack_many_tests = ["test-pack unpack-many-bytes"]
   unpack_many_msg = "Hint: unpack doesn't work on increasingly many bytes"

   unpack_file_tests = ["test-pack unpack-free-coffee",
                        "test-pack unpack-nobody",
                        "test-pack-fast unpack-sonnets",
                        "test-pack-fast unpack-sonnets-bin",
                        "test-pack unpack-shakespeare"]
   unpack_file_msg = "Hint: unpack doesn't work on binascii files"

   goodtests += run_for_successes(unpack_edge_tests, unpack_edge_msg)
   ntests += len(unpack_edge_tests)

   goodtests += run_for_successes(unpack_few_tests, unpack_few_msg)
   ntests += len(unpack_few_tests)

   goodtests += run_for_successes(unpack_many_tests, unpack_many_msg)
   ntests += len(unpack_many_tests)

   goodtests += run_for_successes(unpack_file_tests, unpack_file_msg, timeout=15)
   ntests += len(unpack_file_tests)

   return (goodtests, ntests)


def test_bitpacking(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": pack and unpack"

   (goodtests, ntests) = test_bitpacking_simple(tasknum)
   if (goodtests != ntests):
      print "Fix elementary bitpacking tests to continue"
      return (0, 0, 0)

   #goodtests = 0; ntests = 0
   if not os.path.exists("test-pack"):
      print "Skipping rest of Task " +str(tasknum)+ " (huffman.c did not compile)"
      return (0, 0, 0)

   print "="*25
   print "The next tests for this task use:"
   print "- YOUR is_htree, htree_higher_priority, build_htree, htree_to_codetable,"
   print "       encode_src, build_freqtable, and pack (twice)"
   print "- (nothing from US besides what's in the starter code)"

   print "-"*25
   print "Testing Huffman compress (basic)"
   good = run_tests(basic_tests, "compress")
   n = len(basic_tests)
   basic_compress_score =  good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing Huffman compress (big ugly files)"
   good = run_tests(adv_tests, "compress", huff="huff-fast")
   n = len(adv_tests)
   adv_compress_score = good/n
   goodtests += good; ntests += n

   print "="*25
   print "The remaining tests for this task use:"
   print "- YOUR is_htree, decode_src, and unpack (twice)"
   print "- (nothing from US besides what's in the starter code)"

   print "-"*25
   print "Testing Huffman uncompress (basic)"
   good = run_tests(basic_tests, "uncompress")
   n = len(basic_tests)
   basic_uncompress_score = good/n
   goodtests += good; ntests += n

   print "-"*25
   print "Testing Huffman uncompress (big ugly files)"
   good = run_tests(adv_tests, "compress", huff="huff-fast")
   n = len(adv_tests)
   adv_uncompress_score = good/n
   goodtests += good; ntests += n

   score = 0.5 * basic_compress_score   \
         + 0.5 * basic_uncompress_score \
         + 0.5 * adv_compress_score     \
         + 0.5 * adv_uncompress_score

   tests = mk_valgrind_tests(basic_tests, "compress", "huff-safe")
   tests.extend(mk_valgrind_tests(basic_tests, "uncompress", "huff-safe"))
   score = grind_deductions(tests, score, safety=score/2, leaky=score/2)

   return (score, goodtests, ntests)  # max = 2


#### TEST compressed submission
def test_submit_hip(tasknum):
   print "="*50
   print "Task " + str(tasknum) + ": Compressed submission?"

   if not os.path.exists("huffman.c.hip"):
      print "Nope"
      return 0.0
   else:
      if not os.path.exists("huff-safe"):
         print "huffman.c.hip does not uncompress into a valid C file for this homework"
         return 0.0
      else:
         print "Yep!"
         return 1.0


def main():
   is_tree_score                                 = test_is_tree(1)
   (build_htree_score,        bh_good, bh_tests) = test_build_htree(2)
   (decode_src_score,         ds_good, ds_tests) = test_decode_src(3)
   (htree_to_codetable_score, hc_good, hc_tests) = test_htree_to_codetable(4)
   (encode_src_score,         es_good, es_tests) = test_encode_src(5)
   (build_freqtable_score,    bf_good, bf_tests) = test_build_freqtable(6)
   (bitpacking_score,         bp_good, bp_tests) = test_bitpacking(7)
   submit_hip_score                              = test_submit_hip(8)
   htrees_score    = is_tree_score + build_htree_score
   encodings_score = decode_src_score + htree_to_codetable_score \
                   + encode_src_score + build_freqtable_score
   total_score = htrees_score + encodings_score + bitpacking_score \
               + submit_hip_score

   total_good  = bh_good  + ds_good  + hc_good  + es_good  + bf_good  + bp_good
   total_tests = bh_tests + ds_tests + hc_tests + es_tests + bf_tests + bp_tests

   print '='*50
   print_score("Task 1: ", is_tree_score,            2)
   print_score("Task 2: ", build_htree_score,        5)
   print_score("Task 3: ", decode_src_score,         8)
   print_score("Task 4: ", htree_to_codetable_score, 3)
   print_score("Task 5: ", encode_src_score,         3)
   print_score("Task 6: ", build_freqtable_score,    1)
   print_score("Task 7: ", bitpacking_score,         2)
   print_score("Task 8: ", submit_hip_score,         1)

   print "\n*** FINISHED!"
   print "*** TOTAL SCORE: ",
   print total_score

   scoreboard_msg = str(total_good) + " out of " + str(total_tests)
   # Print JSON results and exit
   print json.dumps({'scores': {'htrees':     htrees_score,
                                'encodings':  encodings_score,
                                'bitpacking': bitpacking_score,
                                'submission': submit_hip_score
                               },
                     'scoreboard': [scoreboard_msg]})


if __name__ == "__main__":
   print "TESTING..."
   main()
