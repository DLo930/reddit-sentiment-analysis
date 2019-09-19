This homework has a two Autolab instances, one for the "Bloom filter
test case checker" (ungraded) and one for the assignment itself.
- The test case checkers is in directory ../bloomtests
- The assignment itself is in directory ../bloom

The Makefile of each operates differently from other homeworks:
- bloom: run
  > make init    hw=bloom  (new!)
  > make install hw=bloom  (or other normal make invocations)

- bloomcheck: run
  > make init    hw=bloomtests  (new!)
  > make install hw=bloomtests  (or other normal make invocations)
  > make final   hw=bloomtests  (new!)

(init creates the appropriate src/grader.py file)
(final renames the writeup and handout files on Autolab)


TESTS:

Incorrect implementations (should assertion-fail test cases)

broke1 - bloom_new fails assertion if table size is 1
broke2 - bloom_new fails assertion if table size is 2000
broke3 - bloom_contains always returns false (postconditions weakened)
broke4 - only stores most recent element
broke5 - only stores m most recent elements
broke6 - lookup skips next-to-most recently added element
broke7 - appears to delete everything else when empty string is added
broke8 - element is removed once looked-up [compile with --no-purity-check]
broke9 - element is removed if re-added
brokeA - re-insertion removes other elements
brokeB - every action switches what's in the set
brokeC - bloom filter attempts to resize when load factor > .5
brokeD - bloom filter attempts to resize when load factor > 1
brokeE - insertion fails if the table size is 1
brokeF - bloom filter always returns false when table size is 1

Bad implementations (should have low performance)

bad1 - Threshold is maximum length
bad2 - Threshold is sum of digits
bad3 - Threshold is max ASCII value
bad4 - Task 2 solution with hash = length
bad5 - Task 2 solution with hash = sum of digits in ASCII

meh1 - Task 2 solution with hash = hash_mul32
meh2 - Task 2 solution with hash = reverse hash_mul32
meh3 - Task 2 solution where table size maxes out at 1024
meh4 - Task 2 solution which does five random insertions for each insertion

Reasonable implementations (should have high performance)

ok1 - Task 2 solution with 8x table size (by using integers)
ok2 - Task 5 solution (LCG from Numerical Recipies, Borland Delphi, Microsoft C)
ok3 - Task 5 solution (fnv, hash_lcg, murmer)
