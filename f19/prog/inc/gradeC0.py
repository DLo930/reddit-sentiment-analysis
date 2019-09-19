# Edited by Daniel Santoro and James Komianos 2/4/2012
# Updated for Fall 2012 by Jonathan Clark 9/13/2012
# and Rob Simmons 10/11/2012
# Revised for Spring 2013 by Rob Simmons

# Why is stderr piped to subprocess.PIPE instead of dev/null? Does
# that even make sense.

import sys
import subprocess
import os.path
import struct
import signal
import resource
import json
import re

# Pretty-print a score on Autolab output
def print_score(task, score, max, extra=""):
    print task+str(score)+"/"+str(max)+extra


## Return behavior
# Some OS's return statuses in [-128,127], others in [0-255]
def normalize(status):
    if (status < 0):
        return 128 - status
    return status

def STATUS_SUCCESS(): return 0
def STATUS_FAILURE(): return 1
def STATUS_ABRT(): return normalize(-6)
def STATUS_FPE(): return normalize(-8)
def STATUS_SEGV(): return normalize(-11)
def STATUS_NOTHING(): return 127
def STATUS_TIMEOUT(): return normalize(-1000) # Must be distinct from "natural" signals

## These return statuses are specific to the C0VM homework
# They need to be different from the above codes so that the C0VM causes
# non-standard codes to tbe thrown.
def C0VM_ABRT(): return 26
def C0VM_SEGV(): return 28
def C0VM_FPE(): return 31


# Pretty HTML scoreboard
def nice_html(score, limit):
    if (limit == None):
        return "<span style='color:#999'>N/A</span>"
    if (score == 0):
        return "<span style='color:#900'>none</span>"
    if (score >= limit):
        return "<span style='color:#090'>full</span>"
    return "<span style='color:#990'>some</span>"

# Check a file for existance
def expect_exists(filename, hintmessage=None):
    print "-"*50
    print "Checking for the existence of "+filename,
    if os.path.exists(filename):
        print "- okay, it exists."
        return True
    else:
        print ""
        print "*** TEST FAILED! Expected the file to exist and it did not."
        if hintmessage <> None: print "*** Hint: "+hintmessage
        return False

# Expect assertion failure
def expect_abort(executable,
                 hintmessage=None,
                 timeout=5,
                 multitest=False):
   if not multitest: print "-"*50
   result = expect_code(executable,
                        STATUS_ABRT(),
                        None,
                        timeout)
   if result == None:
      print "- good, there was an assertion failure."
      return True
   else:
      (actual_status, actual_result, result_desc) = result
      print ""
      print "*** TEST FAILED! Expected a contract to fail."
      print "*** Actual outcome: "+result_desc
      if hintmessage <> None: print "*** Hint: "+hintmessage
      return False

# Expect assertion failure for a series of files
def expect_aborts(executables,
                  hintmessage=None,
                  timeout=5):
    print "-"*50
    result_success = True
    for x in executables:
        if result_success:
            result_success = expect_abort(x, hintmessage, timeout, True)
    return result_success

# Expect assertion failure
def expect_error(executable,
                 hintmessage=None,
                 timeout=5,
                 multitest=False):
   if not multitest: print "-"*50
   result = expect_code(executable,
                        STATUS_FAILURE(),
                        None,
                        timeout)
   if result == None:
      print "- good, error() was called."
      return True
   else:
      (actual_status, actual_result, result_desc) = result
      print ""
      print "*** TEST FAILED! Expected error() to be called."
      print "*** Actual outcome: "+result_desc
      if hintmessage <> None: print "*** Hint: "+hintmessage
      return False

# Expect assertion failure for a series of files
def expect_errors(executables,
                  hintmessage=None,
                  timeout=5):
    print "-"*50
    result_success = True
    for x in executables:
        if result_success:
            result_success = expect_error(x, hintmessage, timeout, True)
    return result_success

# Successful execution that ends with 'return 0' (Or 'return <something else>')
def expect_success(executable,
                   hintmessage=None,
                   expected_return_value=0,
                   timeout=5,
                   multitest=False):
    if not multitest: print "-"*50
    result = expect_code(executable,
                         STATUS_SUCCESS(),
                         expected_return_value,
                         timeout)
    if result == None:
        print "- good, this worked."
        return True
    else:
        (actual_status, actual_result, result_desc) = result
        print ""
        print "*** TEST FAILED! Expected successful execution."
        print "*** Actual outcome: "+result_desc
        if hintmessage <> None: print "*** Hint: "+hintmessage
        return False

# Expect successful execution ending with 'return 0' for a series of files
def expect_successes(executables,
                     hintmessage=None,
                     expected_return_value=0,
                     timeout=5):
    print "-"*50
    result_success = True
    for x in executables:
        if isinstance(x, basestring):
            result_success = \
                result_success and \
                expect_success(x, hintmessage, expected_return_value, timeout,
                               True)
        else:
            (y, retval) = x
            result_success = \
                result_success and \
                expect_success(y, hintmessage, retval, timeout,
                               True)
    return result_success

# Expect specific return codes (somewhat system specific, used in VM testing)
def expect_codes(executables,
                 message,
                 timeout=15,
                 expected_code=0):
    print "-"*50
    for x in executables:
        if isinstance(x,basestring):
            y = x
            code = expected_code
        else:
            (y, code) = x

        result = expect_code(y, code, None, timeout)

        if result <> None:
            (actual_status, actual_result, result_desc) = result
            print ""
            print "*** TESTS FAILED! (Hint: "+message+")"
            print "*** Actual outcome: "+result_desc
            return False

        print "- good, this did what we expected."
    return True

# Set up alarms for timeouts
class Alarm(Exception):
    pass
def alarm_handler(signum, frame):
    raise Alarm
signal.signal(signal.SIGALRM, alarm_handler)

def run_for_result(executable,
                   timeout = 5):

    # C0 programs do not treat the integer returned from main as a
    # status message, they treat the integer returned from main as
    # an integer!  This integer is the last thing printed out in a
    # C0 program when it runs successfully, and if the environment
    # variable C0_RESULT_FILE is set, the C0 runtime also places
    # this return value as the second, third, fourth, and fifth
    # values in the file $C0_RESULT_FILE.
    os.environ['C0_RESULT_FILE'] = '_c0_result'
    def read_return_value():
        try:
            f = open('_c0_result', 'rb')
            f.read(1)
            (b1, b2, b3, b4) = struct.unpack('4B', f.read(4))
            b = (b4 << 24) + (b3 << 16) + (b2 << 8) + b1
            if b > 0x7FFFFFFF: b = b - (1 << 32)
            return b
        except: return None

    # Run executable with a timeout managed by SIGALRM
    try:
        proc_id = subprocess.Popen("./"+executable,
                                   stderr=open(".tmp.output", "w"),
                                   stdout=open(".tmp.stdout", "w"),
                                   shell=True)
        if timeout <> -1:
            signal.alarm(timeout)
        proc_id.wait()
        output = proc_id.returncode
        #if os.WIFSIGNALED(output):
        #    output = 0-os.WTERMSIG(output)
        #elif os.WIFEXITED(output):
        #    output = os.WEXITSTATUS(output)
        #else:
        #    # should never happen
        #    output = STATUS_NOTHING()
    except Alarm:
        try:
            output = STATUS_TIMEOUT()
            proc_id.kill();
            proc_id.wait();
        # Adding this because it happened Feb 2015, don't know how...
        # - RJS
        except UnboundLocalError:
            output = STATUS_TIMEOUT()

    if output == STATUS_SUCCESS():
        return_value = read_return_value()
    else:
        return_value = None

    return (output, return_value)

# expect_code takes
#   - a shell-executable command
#   - an expected status
#   - an optional expected return (for this to work, the
#     shell-executable command must be a C0 compiled binary)
#   - a timeout in seconds (15 is the default, -1 disables timeout)
# Upon success, expect_code returns None
# Upon failure, expect_code returns a triple:
#   - the actual status code
#   - the actual return value (only if the cause of the failure was
#     the actual and expected return values disagreeing; this is None
#     otherwise)
#   - a short explanation of the actual observed outcome
def expect_code(executable,
		expected_status,
		expected_return_value=None,
		timeout=5):

    expected_status = normalize(expected_status)
    # Announce test
    print "Test "+executable+", expect",
    if expected_status == 0: print "successful execution",
    elif expected_status == 1: print "unsuccessful execution (error)",
    elif expected_status == STATUS_ABRT(): print "assertion failure",
    elif expected_status == C0VM_ABRT(): print "c0_assertion_failure()",
    elif expected_status == C0VM_SEGV(): print "c0_memory_error()",
    elif expected_status == C0VM_FPE(): print "c0_arith_error()",
    elif 32 <= expected_status and expected_status <= 112:
        print "c0_user_error() on string of length "+str(expected_status - 32),
    else: print "status code "+str(expected_status),
    sys.stdout.flush()

    (output, actual_return_value) = run_for_result(executable, timeout)
    output = normalize(output)

    # Give generic feedback on result result
    if output == STATUS_TIMEOUT():
        return (output, None,
                "Autograder timed out after "+str(timeout)+" seconds")
    if output == STATUS_NOTHING():
        return (output, None, "File did not compile")
    if output == STATUS_SEGV():
        return (output, None,
                "A segfault occurred: "+\
                    "this means a pointer or array was accessed unsafely!")
    if output == STATUS_FPE():
        return (output, None, "An arithmetic error occurred")
    if output == STATUS_FAILURE() and expected_status <> STATUS_FAILURE():
        return (output, None,
                "Your program signaled failure with a call to error()")
    if output == STATUS_SUCCESS() and expected_status <> STATUS_SUCCESS():
        return (output, None,
                "Your program ran to completion, "+\
                    "but should have signaled an error or failed a contract")
    if output == STATUS_ABRT() and expected_status <> STATUS_ABRT():
        return (output, None, "An assertion failed unexpectedly")
    if output <> expected_status:
        # The following logic only applies to the C0VM assignment:
        if output == C0VM_ABRT():
            return (output, None, "c0_assertion_failure() was called")
        if output == C0VM_SEGV():
            return (output, None, "c0_memory_error() was called")
        if output == C0VM_FPE():
            return (output, None, "c0_arith_error() was called")
        if 32 <= output and output < 200:
            return (output, None, "Status code "+str(output) +\
                    ", possibly the result of c0_user_error() " +\
                    "on a string of length "+str(output - 32))
        return (output, None, "Unexpected result: status code "+str(output))

    assert(output == expected_status)

    if output <> STATUS_SUCCESS() or expected_return_value == None:
        return None # Success!

    # If the test ran fine, we need only to check the return value
    if expected_return_value == actual_return_value:
        return None # Success!
    else:
        return (output, actual_return_value,
                "The program, when run, produced the wrong answer")

# Returns a four-tuple: (failure, mem_errors, mem_leaks, mem_alloced)
#
#  - If failure is non-zero, then Valgrind failed and the program
#    exited abnormally
#  - mem_errors returns the number of memory errors (or -1 for failure)
#  - mem_leaks returns the bytes of memory leaked (or -1 for failure)
#  - mem_alloced returns the bytes of memory allocated (or -1 for failure)

def run_valgrind(executable, timeout=10, expected_return_value=0):
    print "Valgrinding "+executable
    cmd = "valgrind " +\
        "--tool=memcheck " +\
        "--log-file=valgrind.out " +\
        "./" + executable
        # " suppressions=shutup " +\


    try:
        proc_id = subprocess.Popen(cmd,
                                   stderr=open("/dev/null", "w"),
                                   stdout=open("/dev/null", "w"),
                                   shell=True)
        if timeout <> -1:
            signal.alarm(timeout)
        proc_id.wait()
        output = proc_id.returncode
    except Alarm:
        output = STATUS_TIMEOUT()
        proc_id.kill()
        proc_id.wait()

    if output == STATUS_TIMEOUT():
        print "*** VALGRIND FAILED: Valgrind timed out after " +\
            str(timeout)+" seconds"
        return (output, 0, 0, 0)
    elif expected_return_value <> None and output <> expected_return_value:
        print "*** VALGRIND FAILED: " +\
            "With valgrind, the program exited incorrectly"
        return (output, 0, 0, 0)

    return (output, mem_errors(), mem_leaks(), mem_alloced())

def int_comma(s):
	return int(s.replace(",", ""))

def mem_errors():
    re_arg = r'ERROR SUMMARY: ([0123456789,]+) errors'
    with open("valgrind.out", "r") as valgrind:
        for line in valgrind:
            result = re.search(re_arg, line)
            if result <> None:
                return int_comma(result.group(1))
    return -1

def mem_leaks():
    re_arg = r'(definitely|indirectly) lost: ([0123456789,]+) bytes'
    with open("valgrind.out", "r") as valgrind:
        seen = False
        byte_count = 0
        for line in valgrind:
            result = re.search(re_arg, line)
            if result <> None:
                seen = True
                byte_count += int_comma(result.group(2))
            result = re.search(r'All heap blocks were freed', line)
            if result <> None:
                return 0
    if not seen:
        return -1
    else:
        return byte_count

def mem_alloced():
    re_arg = r'([01234567890,]+) bytes allocated'
    with open("valgrind.out", "r") as valgrind:
        for line in valgrind:
            result = re.search(re_arg, line)
            if result <> None:
                return int_comma(result.group(1))
    return -1

def grind_deductions(executables,
                     score=2,
                     safety=1,
                     leaky=1,
                     timeout=15,
                     expected_return_value=0):

    print "-"*50
    deduct_safety = False
    deduct_leaky = False

    for executable in executables:
        res = run_valgrind(executable, timeout=timeout,
                           expected_return_value=None) # We give errors here
        (output, num_errors, num_leaks, num_alloced) = res

        if (output == STATUS_TIMEOUT()):
            print "*** VALGRIND FAILED: Valgrind timed out after " +\
                str(timeout), " seconds (-" + str(score) + " points)"
            return 0

        if (expected_return_value <> None and output <> expected_return_value):
            print "*** VALGRIND FAILED: " +\
                "With valgrind, the program exited incorrectly (-" +\
                str(score) + " points)"
            return 0

        if not deduct_safety and num_errors > 0:
            print "*** VALGRIND FAILED (SAFETY): " +\
                "Valgrind detected " + str(num_errors) + " errors (-" +\
                str(safety) + " points)"
            deduct_safety = True

        if num_errors == -1:
            print  "*** VALGRIND FAILED (SAFETY): " +\
                "Valgrind failed to print error summary (-" +\
                str(score) + " points)"
            return 0

        if leaky > 0 and not deduct_leaky and num_leaks > 0:
            print "*** VALGRIND FAILED (LEAKS): " +\
                "Valgrind detected " + str(num_leaks) +\
                " bytes of leaked memory (-" + str(leaky) + " points)"
            deduct_leaky = True

        if leaky > 0 and num_leaks == -1:
            print "*** VALGRIND FAILED (LEAKS): " +\
                "Valgrind failed to print leak summary (-" +\
                str(score) + " points)"
            return 0

        if deduct_safety and deduct_leaky:
            return score - safety - leaky

    if deduct_safety: score = score - safety
    if deduct_leaky: score = score - leaky

    if score < 0: return 0
    return score
