The 15-122 autograder is based on a functional interface for running
tests and giving feedback to students. It's not terribly 'Pythonic'
because I have a low capacity for pain. The documentation here uses
stylized C0-style types, because I am hilarious.

The autograder doesn't try to do everything, and in particular it
doesn't capture any process output whatsoever. This makes it a bit
harder to give good feedback, but that's based on the hunch (which can
and really should be subject to experimentation in the future) that
overly-hand-holding Autolab feedback exacerbates the problem of
Autolab dependence, as opposed to testing and planning.

 -- Rob Simmons, January 4, 2013


PUBLIC INTERFACE

import 

** Check for the existance of a file
bool expect_exists     (string filename 
                      [ string hintmessage ])

** Expect a test (or series of tests) to return the EXIT_FAILURE
** condition, corresponding to a C0 program that calls error()
bool expect_error      (string commandline
                      [ string hintmessage ]
                      [ int timeout=5 ])
bool expect_errors     (string[] commandlines
                      [ string hintmessage ]
                      [ int timeout=5 ])

** Expect a test (or series of tests) to run into an assertion failure
** (assert() all the time, and //@assert, //@loop_invariant,
** //@requires, //@ensures when contracts are checked dynamically with
** the -d option).
bool expect_abort      (string commandline
                      [ string hintmessage ]
                      [ int timeout=5 ])
bool expect_aborts     (string[] commandlines
                      [ string hintmessage ]
                      [ int timeout=5 ])

** Expect a test (or series of tests) to successfully return a
** particular C0 integer from the main function.
bool expect_success    (string commandline
                      [ string hintmessage ]
                      [ expected_return_value=0 ]
                      [ int timeout=5 ])
bool expect_successes  ((string + string*int)[] commandline
                      [ string hintmessage ]
                      [ expected_return_value=0 ]
                      [ int timeout=5 ])

The first argument to expect_successes is a hetrogeneous list. List
items of the form "test-me" will run the test test-me and expect the
return value to be the one indicated by expected_return_value. List
items of the form ("test-me", 18) will run the test test-me and expect
the return value to be 18.


GENERAL NOTES

 - The argument 'hintmessage' is something that gets printed out in
   the format '(Hint: <hintmessage>)' when the given test
   fails. Experience suggests it is really really easy for these to be
   misleading, so be careful, and make notes in OOPS.txt files when
   messages should be changed/improved for future semesters.

 - Timeouts are per-test, so a series of 60 test with a timeout of 5
   seconds could take up to 5 minutes if every test timed out.


TO-DO

 - It would be nice to distinguish //@requires failures (which we want
   to see triggered in student code), //@assert failures (which are
   necessary to check \length() in contracts), assert() failures
   (which may be triggered in truly exceptional cases, such as
   overflow in UBA resizing) and //@loop_invariant or //@requires
   failures (which should never be triggered in correctly-written
   code)
