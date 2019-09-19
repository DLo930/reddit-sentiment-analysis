hwversion = "opacify-histogram"
#hwversion = "remove_red-count_zeroes"
#hwversion = "remove_green-summarize"

# [pixels] grader

from gradeC0 import *

# Each function corresponds to one task (usually)
def test_pixel(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (pixel.c0)"

    # Small number of tests to make sure the most obvious things work
    if not expect_exists("pixel-grade",
                         "There seems to be a syntax error in pixel.c0"):
        return 0

    # This example returns always 0, 1 or 2 (for historical reasons)
    score = 0
    if expect_success("pixel-grade get_component",
                      "Problem with get_component functions"):
        score += 2
    if expect_success("pixel-grade make_pixel",
                      "Problem with make_pixel"):
        score += 1

    if score < 3: return score

    # Now we're just testing for the perfect score
    if not expect_success("pixel-grade test_pixel_interface",
                          "Problem with the implementation that the " +\
                          "previous tests didn't catch"):
        return 2

    if not expect_aborts(["pixel-grade make_pixel_toobig1",
                          "pixel-grade make_pixel_toobig2",
                          "pixel-grade make_pixel_toobig3",
                          "pixel-grade make_pixel_toobig4",
                          "pixel-grade make_pixel_toosmall1",
                          "pixel-grade make_pixel_toosmall2",
                          "pixel-grade make_pixel_toosmall3",
                          "pixel-grade make_pixel_toosmall4"],
                         "Problem with make_pixel preconditions"):
        return 2

    return 3

def test_pixel_bad(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (pixel-bad.c0)"

    if not expect_exists("pixel-failure",
                         "There seems to be a syntax error in pixel-bad.c0"):
        return 0

    if not expect_exists("pixel-exploit",
                         "There seems to be a syntax error in pixel-bad.c0"):
        return 0

    score = 0
    ms1 = "Our test code was unable to find a contract failure in your\n" +\
          "    pixel-bad.c0 implementation. This may be because our tests\n" +\
          "    were not good enough. If that's the case, we'll go back and\n" +\
          "    make sure you get credit - make sure you explain in a\n" +\
          "    comment which inputs would cause a postcondition to fail."

    ms2 = "Our test code was unable to find a contract exploit in your\n" +\
          "    pixel-bad.c0 implementation. This may be because our tests\n" +\
          "    were not good enough. If that's the case, we'll go back and\n" +\
          "    make sure you get credit - make sure you explain in a\n" +\
          "    comment which inputs would cause incorrect outputs without\n" +\
          "    violating any contracts."

    ms3 = "We were also unable to find any contract failures!"

    if expect_abort("pixel-exploit", ms2):
        score += 1
        if expect_abort("pixel-failure", ms1):
            score += 1
    else:
        if expect_abort("pixel-failure", ms3):
            score += 1


    return score

def test_pixel_test(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (pixel-test.c0)"

    if not expect_exists("pixeltest-self",
                         "Your pixel.c0 does not compile against " +\
                         "your pixel-test.c0"):
        return (0,0)

    if not expect_successes(["pixeltest-self", "pixeltest-ours"],
                            "Your pixel-test.c0 fails in combination with " +\
                            "valid implementations of pixel.c0\n",
                            expected_return_value = None):
        return (0,0)

    if not expect_abort("pixeltest-sbad",
                        "Your pixel-test.c0 doesn't find any errors in your " +\
                        "own pixel-bad.c0"):
        return (0,0)

    caught = 0
    if expect_abort("pixeltest-bad1",
                    "Tests don't catch flagrant postcondition violations"):
        caught = caught + 1
    if expect_abort("pixeltest-bad2",
                    "Tests don't catch flagrant postcondition violations"):
        caught = caught + 1
    if expect_abort("pixeltest-bad3",
                    "Tests don't catch component mix-ups"):
        caught = caught + 1
    if expect_abort("pixeltest-bad4",
                    "Tests don't catch sign-extension bugs"):
        caught = caught + 1
    if expect_abort("pixeltest-bad5",
                    "Do your tests check *all* the functions... " +\
                    "with multiple inputs?"):
        caught = caught + 1
    if expect_abort("pixeltest-bad6",
                    "Do your tests check *all* the functions... " +\
                    "with multiple inputs?"):
        caught = caught + 1
    if expect_abort("pixeltest-bad7",
                    "Do your tests check *all* the functions... " +\
                    "with multiple inputs?"):
        caught = caught + 1
    if expect_abort("pixeltest-bad8",
                    "Do your tests check *all* the functions... " +\
                    "with multiple inputs?"):
        caught = caught + 1
    if expect_abort("pixeltest-bad9",
                    "Tests don't catch realistic sign-extension bugs"):
        caught = caught + 1
    if expect_abort("pixeltest-badA",
                    "Tests don't catch component mix-ups"):
        caught = caught + 1
    if expect_abort("pixeltest-badB",
                    "Tests don't catch component mix-ups"):
        caught = caught + 1

    if caught >= 10: return (caught, 7)
    if caught >= 9:  return (caught, 6)
    if caught >= 8:  return (caught, 5)
    if caught >= 7:  return (caught, 4)
    if caught >= 6:  return (caught, 3)
    if caught >= 5:  return (caught, 2)
    if caught >= 3:  return (caught, 1)
    return (caught, 0)

def test_opacify(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - opacify)"

    if not expect_success("tasks-grade opacify",
                          "Revisions to opacify don't work"):
        return 0

    if expect_successes(["tasks-int opacify",
                         "tasks-struct opacify"],
                        "Some part of tasks.c0 doesn't seem to respect the "+\
                        "pixel interface.\n" +\
                        "*** (The error messages above may give you a hint " +\
                        "as to where)") \
        and expect_exists("tasks-string",
                          "Some part of tasks.c0 seems to compare pixels for " +\
                          "equality.\n" +\
                          "*** (The error messages above may give you a " +\
                          "hint as to where)"):
        return 2
    else: return 0

def test_remove_red(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - remove_red)"

    if not expect_success("tasks-grade remove_red",
                          "Revisions to remove_red don't work"):
        return 0

    if expect_successes(["tasks-int remove_red",
                         "tasks-struct remove_red"],
                        "Some part of tasks.c0 doesn't seem to respect the "+\
                        "pixel interface.\n" +\
                        "*** (The error messages above may give you a hint " +\
                        "as to where)") \
        and expect_exists("tasks-string",
                          "Some part of tasks.c0 seems to compare pixels for " +\
                          "equality.\n" +\
                          "*** (The error messages above may give you a " +\
                          "hint as to where)"):
        return 2
    else: return 0

def test_remove_green(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - remove_green)"

    if not expect_success("tasks-grade remove_green",
                          "Revisions to remove_green don't work"):
        return 0

    if expect_successes(["tasks-int remove_green",
                         "tasks-struct remove_green"],
                        "Some part of tasks.c0 doesn't seem to respect the "+\
                        "pixel interface.\n" +\
                        "*** (The error messages above may give you a hint " +\
                        "as to where)") \
        and expect_exists("tasks-string",
                          "Some part of tasks.c0 seems to compare pixels for " +\
                          "equality.\n" +\
                          "*** (The error messages above may give you a " +\
                          "hint as to where)"):
        return 2
    else: return 0

def test_remove_blue(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - remove_blue)"

    if not expect_success("tasks-grade remove_blue",
                          "Revisions to remove_blue don't work"):
        return 0

    if expect_successes(["tasks-int remove_blue",
                         "tasks-struct remove_blue"],
                        "Some part of tasks.c0 doesn't seem to respect the "+\
                        "pixel interface.\n" +\
                        "*** (The error messages above may give you a hint " +\
                        "as to where)") \
        and expect_exists("tasks-string",
                          "Some part of tasks.c0 seems to compare pixels for " +\
                          "equality.\n" +\
                          "*** (The error messages above may give you a " +\
                          "hint as to where)"):
        return 2
    else: return 0

def test_quantize(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - quantize)"

    if expect_success("tasks-grade quantize", "Our tests for quantize fail"):
        return 3
    else: return 0

def test_quantize_test(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - test_quantize)"

    if not expect_success("tq-good test_quantize",
                          "Your quantize tests did not succeed when " +\
                          "run on a solution we think is correct.\n"):
        return (0, 0)

    expect_successes(["tq-self test_quantize",
                      "tq-ours test_quantize"],
                     "Your quantize tests did not succeed when " +\
                     "run on your own solution (no penalty, but ugh!)")

    caught = 0
    if expect_abort("tq-bad1 test_quantize",
                    "Didn't catch bug 1 (returns wrong answers)"):
        caught = caught + 1
    if expect_abort("tq-bad2 test_quantize",
                    "Didn't catch bug 2 (returns wrong answers)"):
        caught = caught + 1
    if expect_abort("tq-bad3 test_quantize",
                    "Didn't catch bug 3 (returns wrong answers)"):
        caught = caught + 1
    if expect_abort("tq-bad4 test_quantize",
                    "Didn't catch bug 4 (edge case)"):
        caught = caught + 1
    if expect_abort("tq-bad5 test_quantize",
                    "Didn't catch bug 5 (edge case)"):
        caught = caught + 1

    if caught >= 4: return (caught, 4)
    if caught >= 3: return (caught, 3)
    if caught >= 2: return (caught, 2)
    return (caught, 0)


def test_count_zeroes(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - count_zeroes)"

    if expect_success("tasks-grade count_zeroes", "Tests for count_zeroes fail"):
        return 3
    else: return 0

def test_histogram(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - histogram)"

    if expect_success("tasks-grade histogram", "Tests for histogram fail"):
        return 3
    else: return 0


def test_summarize(tasknum):
    print "="*50
    print "Testing Task " +str(tasknum)+ " (tasks.c0 - summarize)"

    if expect_success("tasks-grade summarize", "Tests for summarize fail"):
        return 3
    else: return 0


def main():
    pixel_score                         = test_pixel(1)
    badpixel_score                      = test_pixel_bad(2)
    (pixelbugs_caught, testpixel_score) = test_pixel_test(3)

    manipulate_pixel_score = 0
    quantize_score = 0
    (quantizebugs_caught, testquantize_score) = (0, 0)
    return_args_score = 0

    if os.path.exists("tasks-grade"):
        if hwversion == "opacify-histogram":
            manipulate_pixel_score = test_opacify(4)
        if hwversion == "remove_red-count_zeroes":
            manipulate_pixel_score = test_remove_red(4)
        if hwversion == "remove_green-summarize":
            manipulate_pixel_score = test_remove_green(4)
        quantize_score                            = test_quantize(5)
        (quantizebugs_caught, testquantize_score) = test_quantize_test(6)
        if hwversion == "opacify-histogram":
            return_args_score = test_histogram(7)
        if hwversion == "remove_red-count_zeroes":
            return_args_score = test_count_zeroes(7)
        if hwversion == "remove_green-summarize":
            return_args_score = test_summarize(7)
    else:
        print "="*50
        print "Cannot test tasks.c0 (Tasks 4-7), it seems to not compile"

    print '='*50
    print_score("Task 1: ", pixel_score,            3,
                extra = " + 1 point that will be graded by hand")
    print_score("Task 2: ", badpixel_score,         2)
    print_score("Task 3: ", testpixel_score,        7)
    print_score("Task 4: ", manipulate_pixel_score, 2)
    print_score("Task 5: ", quantize_score,         3)
    print_score("Task 6: ", testquantize_score,     4)
    print_score("Task 7: ", return_args_score,      3)

    total = pixel_score + badpixel_score + testpixel_score + \
            manipulate_pixel_score + \
            quantize_score + testquantize_score + \
            return_args_score

    print "\n*** FINISHED!"
    print "*** TOTAL SCORE: "+str(total)

    print json.dumps({'scores':
                      {'pixel': pixel_score,
                       'badpixel': badpixel_score,
                       'testpixel': testpixel_score,
                       'modifypixel' : manipulate_pixel_score,
                       'quantize': quantize_score,
                       'testquantize': testquantize_score,
                       'multireturn': return_args_score},
                      'scoreboard': [pixelbugs_caught + quantizebugs_caught,
                                     pixelbugs_caught,
                                     quantizebugs_caught]})

if __name__ == "__main__":
    print "TESTING..."
    main()
