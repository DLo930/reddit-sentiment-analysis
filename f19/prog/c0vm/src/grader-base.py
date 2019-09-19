# [c0vm] grader

from gradeC0 import *

# value for CHECKPOINT supplied by Makefile
POSTFINAL = False
#POSTFINAL = True

def test_arithmetic(tasknum):
    print "="*50
    print "Testing task " +str(tasknum)+ " (arithmetic)"

    if not expect_successes([("c0vm  tests/task1/return1.bc0", 0),
                             ("c0vmd tests/task1/return1.bc0", 0),
                             ("c0vm  tests/task1/return2.bc0", 15),
                             ("c0vmd tests/task1/return2.bc0", 15)],
                            "Problem with bipush or return. Giving up."):
        return 0

    score = 0

    if not expect_successes([("c0vm  tests/task1/return3.bc0", -1),
                             ("c0vmd tests/task1/return3.bc0", -1),
                             ("c0vmd tests/task1/return4.bc0", -128),
                             ("c0vmd tests/task1/return4.bc0", -128)],
                            "Bipush doesn't sign extend? Giving up."):
        return 1

    print "-"*50
    print "*** Note: *all* remaining tests use bipush and return."
    print "*** Future errors may be problems with bipush and return."

    score += 2

    if expect_successes([("c0vm  tests/task1/add1.bc0", 137),
                         ("c0vmd tests/task1/add1.bc0", 137),
                         ("c0vm  tests/task1/add2.bc0", -107),
                         ("c0vmd tests/task1/add2.bc0", -107),
                         ("c0vm  tests/task1/add3.bc0", 107),
                         ("c0vmd tests/task1/add3.bc0", 107),
                         ("c0vm  tests/task1/add4.bc0", -137),
                         ("c0vmd tests/task1/add4.bc0", -137)],
                        "Problem with iadd"):
        if expect_successes([("c0vm  tests/task1/sub1.bc0", -107),
                             ("c0vmd tests/task1/sub1.bc0", -107),
                             ("c0vm  tests/task1/sub2.bc0", 137),
                             ("c0vmd tests/task1/sub2.bc0", 137),
                             ("c0vm  tests/task1/sub3.bc0", -137),
                             ("c0vmd tests/task1/sub3.bc0", -137),
                             ("c0vm  tests/task1/sub4.bc0", 107),
                             ("c0vmd tests/task1/sub4.bc0", 107)],
                            "Problem with isub"):
            score += 1

    if expect_successes([("c0vm  tests/task1/by-hand-dup.bc0", 30),
                         ("c0vmd tests/task1/by-hand-dup.bc0", 30),
                         ("c0vm  tests/task1/by-hand-dup2.bc0", -2),
                         ("c0vm  tests/task1/by-hand-dup2.bc0", -2)],
                        "Problem with dup or iadd"):
        score += 1

    if expect_successes([("c0vm  tests/task1/by-hand-popswap.bc0", 122),
                         ("c0vmd tests/task1/by-hand-popswap.bc0", 122),
                         ("c0vm  tests/task1/by-hand-popswap2.bc0", -3),
                         ("c0vmd tests/task1/by-hand-popswap2.bc0", -3),
                         ("c0vm  tests/task1/by-hand-popswap3.bc0", -2),
                         ("c0vmd tests/task1/by-hand-popswap3.bc0", -2)],
                        "Problem with pop or swap"):
        score += 1

    print "-"*50
    print "Score before valgrind #1: "+str(score)+" (max deduction 5)"
    score = grind_deductions(["c0vm tests/task1/return1.bc0",
                              "c0vm tests/task1/sub3.bc0",
                              "c0vm tests/task1/by-hand-dup.bc0",
                              "c0vm tests/task1/by-hand-dup2.bc0",
                              "c0vm tests/task1/by-hand-popswap.bc0",
                              "c0vm tests/task1/by-hand-popswap2.bc0",
                              "c0vm tests/task1/by-hand-popswap3.bc0"],
                             score = score,
                             safety = 3,
                             leaky = 2)


    if expect_successes([("c0vm  tests/task1/and1.bc0", 10),
                         ("c0vmd tests/task1/and1.bc0", 10),
                         ("c0vm  tests/task1/and2.bc0", 0),
                         ("c0vmd tests/task1/and2.bc0", 0),
                         ("c0vm  tests/task1/and3.bc0", 15),
                         ("c0vmd tests/task1/and3.bc0", 15),
                         ("c0vm  tests/task1/and4.bc0", 0),
                         ("c0vmd tests/task1/and4.bc0", 0),
                         ("c0vm  tests/task1/and5.bc0", -1),
                         ("c0vmd tests/task1/and5.bc0", -1)],
                        "Problem with iand"):
        score += 1

    if expect_successes(["c0vm  tests/task1/div1.bc0",
                         "c0vmd tests/task1/div1.bc0",
                         "c0vm  tests/task1/div2.bc0",
                         "c0vmd tests/task1/div2.bc0",
                         "c0vm  tests/task1/div3.bc0",
                         "c0vmd tests/task1/div3.bc0",
                         "c0vm  tests/task1/div4.bc0",
                         "c0vmd tests/task1/div4.bc0",
                         "c0vm  tests/task1/div6.bc0",
                         "c0vmd tests/task1/div6.bc0",
                         ("c0vm  tests/task1/div8.bc0", 8),
                         ("c0vmd tests/task1/div8.bc0", 8),
                         ("c0vm  tests/task1/div9.bc0", -8),
                         ("c0vmd tests/task1/div9.bc0", -8),
                         ("c0vm  tests/task1/div10.bc0", -8),
                         ("c0vmd tests/task1/div10.bc0", -8),
                         ("c0vm  tests/task1/div11.bc0", 8),
                         ("c0vmd tests/task1/div11.bc0", 8),
                         ("c0vm  tests/task1/div12.bc0", 25),
                         ("c0vmd tests/task1/div12.bc0", 25)],
                        "Problem with idiv"):
        if expect_codes([("c0vm  tests/task1/div5.bc0", C0VM_FPE()),
                         ("c0vmd tests/task1/div5.bc0", C0VM_FPE()),
                         ("c0vm  tests/task1/div7.bc0", C0VM_FPE()),
                         ("c0vmd tests/task1/div7.bc0", C0VM_FPE())],
                        "Problem with idiv (need to call to c0_arith_error?)"):
            score += 1

    if expect_successes([("c0vm  tests/task1/mul1.bc0", 1830),
                         ("c0vmd tests/task1/mul1.bc0", 1830),
                         ("c0vm  tests/task1/mul2.bc0", -1830),
                         ("c0vmd tests/task1/mul2.bc0", -1830),
                         ("c0vm  tests/task1/mul3.bc0", -1830),
                         ("c0vmd tests/task1/mul3.bc0", -1830),
                         ("c0vm  tests/task1/mul4.bc0", 1830),
                         ("c0vmd tests/task1/mul4.bc0", 1830),
                         ("c0vm  tests/task1/mul5.bc0", 0),
                         ("c0vmd tests/task1/mul5.bc0", 0),
                         ("c0vm  tests/task1/mul6.bc0", 0),
                         ("c0vmd tests/task1/mul6.bc0", 0),
                         ("c0vm  tests/task1/mul7.bc0", 0),
                         ("c0vmd tests/task1/mul7.bc0", 0)],
                        "Problem with imul"):
        score += 1

    if expect_successes([("c0vm  tests/task1/or1.bc0", 127),
                         ("c0vmd tests/task1/or1.bc0", 127),
                         ("c0vm  tests/task1/or2.bc0", 15),
                         ("c0vmd tests/task1/or2.bc0", 15),
                         ("c0vm  tests/task1/or3.bc0", -1),
                         ("c0vmd tests/task1/or3.bc0", -1),
                         ("c0vm  tests/task1/or4.bc0", -1),
                         ("c0vmd tests/task1/or4.bc0", -1),
                         ("c0vm  tests/task1/or5.bc0", -1),
                         ("c0vmd tests/task1/or5.bc0", -1)],
                        "Problem with ior"):
        score += 1

    if expect_successes([("c0vm  tests/task1/mod1.bc0", 15),
                         ("c0vmd tests/task1/mod1.bc0", 15),
                         ("c0vm  tests/task1/mod2.bc0", 15),
                         ("c0vmd tests/task1/mod2.bc0", 15),
                         ("c0vm  tests/task1/mod3.bc0", -15),
                         ("c0vmd tests/task1/mod3.bc0", -15),
                         ("c0vm  tests/task1/mod4.bc0", -15),
                         ("c0vmd tests/task1/mod4.bc0", -15),
                         ("c0vm  tests/task1/mod6.bc0", 0),
                         ("c0vmd tests/task1/mod6.bc0", 0),
                         ("c0vm  tests/task1/mod8.bc0", 2),
                         ("c0vmd tests/task1/mod8.bc0", 2),
                         ("c0vm  tests/task1/mod9.bc0", 2),
                         ("c0vmd tests/task1/mod9.bc0", 2),
                         ("c0vm  tests/task1/mod10.bc0", -2),
                         ("c0vmd tests/task1/mod10.bc0", -2),
                         ("c0vm  tests/task1/mod11.bc0", -2),
                         ("c0vmd tests/task1/mod11.bc0", -2),
                         ("c0vm  tests/task1/mod12.bc0", 0),
                         ("c0vmd tests/task1/mod12.bc0", 0)],
                        "Problem with irem"):
        if expect_codes([("c0vm  tests/task1/mod5.bc0", C0VM_FPE()),
                         ("c0vmd tests/task1/mod5.bc0", C0VM_FPE()),
                         ("c0vm  tests/task1/mod7.bc0", C0VM_FPE()),
                         ("c0vmd tests/task1/mod7.bc0", C0VM_FPE())],
                        "Problem with irem (call c0_arith_error?)"):
            score += 1

    if expect_successes([("c0vm  tests/task1/shl1.bc0", 15),
                         ("c0vmd tests/task1/shl1.bc0", 15),
                         ("c0vm  tests/task1/shl2.bc0", 30),
                         ("c0vmd tests/task1/shl2.bc0", 30),
                         ("c0vm  tests/task1/shl3.bc0", 60),
                         ("c0vmd tests/task1/shl3.bc0", 60),
                         ("c0vm  tests/task1/shl4.bc0", 3840),
                         ("c0vmd tests/task1/shl4.bc0", 3840),
                         ("c0vm  tests/task1/shl5.bc0", -2147483648),
                         ("c0vmd tests/task1/shl5.bc0", -2147483648),
                         ("c0vm  tests/task1/shl9.bc0", -1610612736),
                         ("c0vmd tests/task1/shl9.bc0", -1610612736),
                         ("c0vm  tests/task1/shl10.bc0", 1073741824),
                         ("c0vmd tests/task1/shl10.bc0", 1073741824),
                         ("c0vm  tests/task1/shl11.bc0", -2147483648),
                         ("c0vmd tests/task1/shl11.bc0", -2147483648),
                         ("c0vm  tests/task1/shl12.bc0", 0),
                         ("c0vmd tests/task1/shl12.bc0", 0),
                         ("c0vm  tests/task1/shr1.bc0", 15),
                         ("c0vmd tests/task1/shr1.bc0", 15),
                         ("c0vm  tests/task1/shr2.bc0", 7),
                         ("c0vmd tests/task1/shr2.bc0", 7),
                         ("c0vm  tests/task1/shr3.bc0", 3),
                         ("c0vmd tests/task1/shr3.bc0", 3),
                         ("c0vm  tests/task1/shr4.bc0", 0),
                         ("c0vmd tests/task1/shr4.bc0", 0),
                         ("c0vm  tests/task1/shr5.bc0", 0),
                         ("c0vmd tests/task1/shr5.bc0", 0),
                         ("c0vm  tests/task1/shr9.bc0", -1),
                         ("c0vmd tests/task1/shr9.bc0", -1),
                         ("c0vm  tests/task1/shr10.bc0", -1),
                         ("c0vmd tests/task1/shr10.bc0", -1),
                         ("c0vm  tests/task1/shr11.bc0", -1),
                         ("c0vmd tests/task1/shr11.bc0", -1),
                         ("c0vm  tests/task1/shr12.bc0", -1),
                         ("c0vmd tests/task1/shr12.bc0", -1)],
                        "Problem with ishl or ishr"):
        score += 1

    if expect_codes([("c0vm  tests/task1/shl6.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shl6.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shl7.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shl7.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shl8.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shl8.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shl13.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shl13.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shl14.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shl14.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shr6.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr6.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shr7.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr7.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr8.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr8.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shr13.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr13.bc0", C0VM_FPE()),
                     ("c0vm  tests/task1/shr14.bc0", C0VM_FPE()),
                     ("c0vmd tests/task1/shr14.bc0", C0VM_FPE())],
                    "Problem with ishl/ishr (call c0_arith_error?)"):
        score += 1

    if expect_successes([("c0vm  tests/task1/xor1.bc0", 117),
                         ("c0vmd tests/task1/xor1.bc0", 117),
                         ("c0vm  tests/task1/xor2.bc0", 15),
                         ("c0vmd tests/task1/xor2.bc0", 15),
                         ("c0vm  tests/task1/xor3.bc0", -16),
                         ("c0vmd tests/task1/xor3.bc0", -16),
                         ("c0vm  tests/task1/xor4.bc0", -1),
                         ("c0vmd tests/task1/xor4.bc0", -1),
                         ("c0vm  tests/task1/xor5.bc0", 0),
                         ("c0vmd tests/task1/xor5.bc0", 0),
                         ("c0vm  tests/task1/xor6.bc0", -1),
                         ("c0vmd tests/task1/xor6.bc0", -1)],
                        "Problem with ixor"):
        score += 1

    if expect_successes([("c0vm  tests/task1/shladd1.bc0", 2147483647),
                         ("c0vmd tests/task1/shladd1.bc0", 2147483647),
                         ("c0vmd tests/task1/div14.bc0", -2147483648),
                         ("c0vmd tests/task1/div16.bc0", 1),
                         ("c0vmd tests/task1/div17.bc0", -2147483647),
                         ("c0vmd tests/task1/mod14.bc0", 0),
                         ("c0vmd tests/task1/mod16.bc0", 0),
                         ("c0vmd tests/task1/mod17.bc0", 0),
                         ("c0vmd tests/task1/mod18.bc0", -3),
                         ("c0vm  tests/task1/combo1.bc0", 15122),
                         ("c0vmd tests/task1/combo1.bc0", 15122),
                         ("c0vm  tests/task1/combo2.bc0", 5),
                         ("c0vmd tests/task1/combo2.bc0", 5)],
                        "Problem with combination tests") \
                        and \
                        expect_codes([("c0vm  tests/task1/div13.bc0", C0VM_FPE()),
                                      ("c0vmd tests/task1/div13.bc0", C0VM_FPE()),
                                      ("c0vmd tests/task1/div15.bc0", C0VM_FPE()),
                                      ("c0vmd tests/task1/mod15.bc0", C0VM_FPE()),
                                      ("c0vm  tests/task1/shldiv1.bc0", C0VM_FPE()),
                                      ("c0vmd tests/task1/shldiv1.bc0", C0VM_FPE())],
                                     "Problem with combination tests -- execution succeeded where it should have failed, or failed for the wrong reason"):
        score += 2
        print "-"*50
        print "Score before valgrind #2: "+str(score)+" (max deduction 6)"
        score = grind_deductions(["c0vm tests/task1/shladd1.bc0",
                                  "c0vm tests/task1/combo1.bc0",
                                  "c0vm tests/task1/combo2.bc0"],
                                 score = score,
                                 leaky = 2,
                                 safety = 4)
    return score

def test_locals(tasknum):
    print "="*50
    print "Testing task " +str(tasknum)+ " (local variables)"

    if expect_successes([("c0vmd tests/task2/ildc1.bc0", 4401),
                         ("c0vmd tests/task2/ildc2.bc0", 1364597427),
                         ("c0vmd tests/task2/ildc3.bc0", -246015309)],
                        "Problem with ildc (or pop), giving up."):
       score = 2
       cangrind = True
    else: return 0

    if expect_successes([("c0vmd tests/task2/ildc4.bc0", 10000),
                         ("c0vmd tests/task2/ildc5.bc0", -2147483648)],
                        "Problem with ildc's interpretation of two bytes " +\
                        "as an unsigned int"):
        score += 1
    else: cangrind = False

    print "-"*50
    print "*** Note: the next batch of tests use ildc."
    print "*** Future errors may be problems with ildc."

    if expect_successes([("c0vmd tests/task2/largeadd1.bc0", 36249),
                         ("c0vmd tests/task2/largeadd2.bc0", -1),
                         ("c0vmd tests/task2/largeadd3.bc0", -2),
                         ("c0vmd tests/task2/largeadd4.bc0", -2147483648),
                         ("c0vmd tests/task2/largeand1.bc0", 0),
                         ("c0vmd tests/task2/largeand2.bc0", 305419896),
                         ("c0vmd tests/task2/largediv1.bc0", 1),
                         ("c0vmd tests/task2/largediv2.bc0", 7561),
                         #("c0vmd tests/task2/largediv3.bc0", 1),
                         #("c0vmd tests/task2/largediv4.bc0", 1),
                         ("c0vmd tests/task2/largemod1.bc0", 6005),
                         ("c0vmd tests/task2/largemod2.bc0", 1),
                         #("c0vmd tests/task2/largemod3.bc0", 1),
                         #("c0vmd tests/task2/largemod4.bc0", 1),
                         ("c0vmd tests/task2/largemul1.bc0", 319482494),
                         ("c0vmd tests/task2/largemul2.bc0", -446591760),
                         ("c0vmd tests/task2/largeor1.bc0", -1),
                         ("c0vmd tests/task2/largeor2.bc0", -1),
                         ("c0vmd tests/task2/largeshl1.bc0", 1982070784),
                         ("c0vmd tests/task2/largeshl2.bc0", 15122),
                         ("c0vmd tests/task2/largeshl3.bc0", 30244),
                         ("c0vmd tests/task2/largeshr1.bc0", 118),
                         ("c0vmd tests/task2/largeshr2.bc0", 118),
                         ("c0vmd tests/task2/largeshr3.bc0", -119),
                         ("c0vmd tests/task2/largesub1.bc0", -6005),
                         ("c0vmd tests/task2/largesub2.bc0", -255),
                         ("c0vmd tests/task2/largesub3.bc0", 2147483647),
                         ("c0vmd tests/task2/largesub4.bc0", 1),
                         ("c0vmd tests/task2/largexor1.bc0", -1),
                         ("c0vmd tests/task2/largexor2.bc0", -305419897)],
                        "Problem with ildc+arithmetic") \
                        and expect_codes(["c0vmd tests/task2/largediv3.bc0",
                                          "c0vmd tests/task2/largediv4.bc0",
                                          "c0vmd tests/task2/largemod3.bc0",
                                          "c0vmd tests/task2/largemod4.bc0"],
                                         "Problem with ildc+arithmetic",
                                         expected_code=C0VM_FPE()):
        score += 2

    if expect_successes([("c0vmd tests/task2/const1.bc0", 15122),
                         ("c0vmd tests/task2/const2.bc0", 228674884),
                         ("c0vmd tests/task2/const3.bc0", 319482494),
                         ("c0vmd tests/task2/const4.bc0", 31848),
                         ("c0vmd tests/task2/const5.bc0", 228674884),
                         ("c0vmd tests/task2/const6.bc0", 81300)],
                        "Problem with ildc+vstore and vload"):
        score += 1
    else: cangrind = False

    if expect_successes([("c0vmd tests/task2/const8.bc0", -2),
                         ("c0vmd tests/task2/const9.bc0", 19999),
                         ("c0vmd tests/task2/const10.bc0", 19999)],
                        "Problem with ildc+vstore and vload, lots of vars"):
        score += 1
    else: cangrind = False


    print "-"*50
    print "*** Note: the next batch of tests use aldc, athrow and assert."
    print "*** Future errors may be problems with aldc, athrow and assert."

    if expect_codes([("c0vmd tests/task2/aldc1.bc0", 48),
                     #("c0vmd tests/task3/error.bc0", 37),
                     ("c0vmd tests/task2/assert1.bc0", 0),
                     ("c0vmd tests/task2/assert2.bc0", C0VM_ABRT())],
                    "aldc, athrow and assert"):
        score += 0.5
    else: cangrind = False

    if expect_codes([("c0vmd tests/task2/aldc2.bc0", 48),
                     ("c0vmd tests/task2/aldc3.bc0", 48)],
                    "Problem with aldc, pop, or athrow: fix for more tests"):
        if expect_codes([("c0vmd tests/task2/assert3.bc0", 0),
                         ("c0vmd tests/task2/assert4.bc0", C0VM_ABRT()),
                         ("c0vmd tests/task2/assert5.bc0", 0),
                         ("c0vmd tests/task2/aldc4.bc0", 52),
                         ("c0vmd tests/task2/aldc5.bc0", 61),
                         ("c0vmd tests/task2/aldc6.bc0", 61)],
                        "Problem with aldc, assert, athrow and anything else so far"):
            score += 0.5
        else: cangrind = False
    else: cangrind = False

    if cangrind:
        print "-"*50
        print "Score before valgrind #3: "+str(score)
        score += grind_deductions(["c0vm tests/task2/const1.bc0",
                                   "c0vm tests/task2/const8.bc0",
                                   "c0vmd tests/task2/ildc4.bc0"],
                                  score = 1,
                                  leaky = 1,
                                  safety = 1)
        score += grind_deductions(["c0vm tests/task2/aldc1.bc0",
                                   "c0vm tests/task2/aldc2.bc0",
                                   "c0vm tests/task2/aldc3.bc0",
                                   "c0vm tests/task2/aldc4.bc0",
                                   "c0vm tests/task2/aldc5.bc0",
                                   "c0vm tests/task2/aldc6.bc0"],
                                  score = 1,
                                  leaky = 0.5,
                                  safety = 1,
                                  expected_return_value = None)

    return score

def test_conditionals(tasknum):
    print "="*50
    print "Testing task " +str(tasknum)+ " (conditionals)"

    score = 0.0

    if expect_successes([("c0vmd tests/task3/ifeq1.bc0", 15123),
                         ("c0vmd tests/task3/ifeq2.bc0", 15122),
                         ("c0vmd tests/task3/ifeq3.bc0", 15124),
                         ("c0vmd tests/task3/ifeq4.bc0", 15120),
                         ("c0vmd tests/task3/ifeq13.bc0", 15122)],
                        "Problem with simple if statement programs " + \
                            "(if_cmpeq, goto, arithmetic, and locals). " + \
                            "Giving up."):
        score += 0.5
    else: return 0.0

    if expect_successes([("c0vmd tests/task3/ifne1.bc0", 15122),
                         ("c0vmd tests/task3/ifne2.bc0", 15123),
                         ("c0vmd tests/task3/ifne3.bc0", 15120),
                         ("c0vmd tests/task3/ifne4.bc0", 15124),
                         ("c0vmd tests/task3/ifne5.bc0", 15123)],
                        "Problem, maybe with if_cmpne"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/ifge1.bc0", 15123),
                         ("c0vmd tests/task3/ifge2.bc0", 15123),
                         ("c0vmd tests/task3/ifge3.bc0", 15122),
                         ("c0vmd tests/task3/ifge4.bc0", 15124),
                         ("c0vmd tests/task3/ifge5.bc0", 15124),
                         ("c0vmd tests/task3/ifge6.bc0", 15120),
                         ("c0vmd tests/task3/ifge7.bc0", 15120),
                         ("c0vmd tests/task3/ifge8.bc0", 15124)],
                        "Problem, maybe with if_cmpge"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/ifgt1.bc0", 15122),
                         ("c0vmd tests/task3/ifgt2.bc0", 15123),
                         ("c0vmd tests/task3/ifgt3.bc0", 15122),
                         ("c0vmd tests/task3/ifgt4.bc0", 15120),
                         ("c0vmd tests/task3/ifgt5.bc0", 15124),
                         ("c0vmd tests/task3/ifgt6.bc0", 15120),
                         ("c0vmd tests/task3/ifgt7.bc0", 15120),
                         ("c0vmd tests/task3/ifgt8.bc0", 15124)],
                        "Problem, maybe with if_cmpgt"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/ifle1.bc0", 15123),
                         ("c0vmd tests/task3/ifle2.bc0", 15122),
                         ("c0vmd tests/task3/ifle3.bc0", 15123),
                         ("c0vmd tests/task3/ifle4.bc0", 15124),
                         ("c0vmd tests/task3/ifle5.bc0", 15120),
                         ("c0vmd tests/task3/ifle6.bc0", 15124),
                         ("c0vmd tests/task3/ifle7.bc0", 15124),
                         ("c0vmd tests/task3/ifle8.bc0", 15120)],
                        "Problem, maybe with if_cmple"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/iflt1.bc0", 15122),
                         ("c0vmd tests/task3/iflt2.bc0", 15122),
                         ("c0vmd tests/task3/iflt3.bc0", 15123),
                         ("c0vmd tests/task3/iflt4.bc0", 15120),
                         ("c0vmd tests/task3/iflt5.bc0", 15120),
                         ("c0vmd tests/task3/iflt6.bc0", 15124),
                         ("c0vmd tests/task3/iflt7.bc0", 15124),
                         ("c0vmd tests/task3/iflt8.bc0", 15120)],
                        "Problem, maybe with if_cmplt"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/goto1.bc0", 15122),
                         ("c0vmd tests/task3/goto2.bc0", 15178)],
                        "Conditionals and large positive goto"):
        score += 0.5

    if expect_successes([("c0vmd tests/task3/goto3.bc0", 15178)],
                        "Conditionals and large negative goto"):
        score += 0.5

    if expect_successes([("c0vm tests/task3/eq2.bc0", 0),
                         ("c0vm tests/task3/for1.bc0", 7398),
                         ("c0vm tests/task3/for2.bc0", 0),
                         ("c0vm tests/task3/for3.bc0", 3672),
                         ("c0vm tests/task3/for4.bc0", -69025792),
                         ("c0vm tests/task3/for5.bc0", 0),
                         ("c0vm tests/task3/nested1.bc0", -63558),
                         ("c0vm tests/task3/nested2.bc0", 450),
                         ("c0vm tests/task3/nested3.bc0", 494982),
                         ("c0vm tests/task3/while1.bc0", 7398),
                         ("c0vm tests/task3/while2.bc0", 3672),
                         ("c0vm tests/task3/while3.bc0", 0),
                         ("c0vm tests/task3/while4.bc0", 7398),
                         ("c0vm tests/task3/while5.bc0", 225)],
                        "Full conditional tests failed"):
        score += 1.0

    print "-"*50
    print "Current score: "+str(score)+"/5"
    print "The last 2 points of this task test aspects of Tasks 1 and 2"
    print "that we couldn't fully test without having if_cmpeq, and goto around"

    if expect_successes(["c0vmd tests/task3/ifeqNULL.bc0",
                         "c0vmd tests/task3/ifneqNULL.bc0"],
                        "Checking if NULL == NULL"):
        score += 0.5

    if expect_codes([("c0vmd tests/task3/error.bc0", 48),
                     ("c0vmd tests/task3/assert6.bc0", 0),
                     ("c0vmd tests/task3/assert7.bc0", C0VM_ABRT())],
                    "aldc, pop, athrow, assert, or arithmetic"):
            score += grind_deductions(["c0vm tests/task3/error.bc0",
                                       "c0vm tests/task3/assert6.bc0",
                                       "c0vm tests/task3/assert7.bc0"],
                                      score = 1,
                                      leaky = 0.5,
                                      safety = 1,
                                      expected_return_value = None)

    if expect_successes(["c0vmd tests/task3/ifeq5.bc0",
                         "c0vmd tests/task3/ifeq6.bc0",
                         "c0vmd tests/task3/ifeq7.bc0",
                         "c0vmd tests/task3/ifeq8.bc0",
                         "c0vmd tests/task3/ifeq9.bc0",
                         "c0vmd tests/task3/ifeq10.bc0",
                         "c0vmd tests/task3/ifeq11.bc0",
                         "c0vmd tests/task3/ifeq12.bc0"],
                        "Integers are not stored properly masked.\n"+\
                        "NOTE: these tests (2 of the 7 points) "+\
                        "are tests of arithmetic operations (task 1) "+\
                        "but would only work ildc was implemented in Task 2 "+\
                        "and if_cmpeq and goto were implemented in Task 3."):
        score += 0.5

    return score

def test_functions(tasknum):
    print "="*50
    print "Testing task " +str(tasknum)+ " (functions)"

    score = 0.0

    if expect_successes([("c0vm  tests/task4/static2.bc0", 19523),
                         ("c0vmd tests/task4/static2.bc0", 19523),
                         ("c0vm  tests/task4/static3.bc0", 114345003),
                         ("c0vmd tests/task4/static3.bc0", 114345003),],
                        "Problem with invokestatic."):
        score += 0.5
    else:
        if not expect_success("c0vm tests/task4/native1.bc0",
                              "Also problem with invokenative. Giving up."):
            return 0

    if expect_successes([("c0vm  tests/task4/static1.bc0", 19523),
                         ("c0vmd tests/task4/static1.bc0", 19523),
                         ("c0vm  tests/task4/static4.bc0", 7398),
                         ("c0vmd tests/task4/static4.bc0", 7398),
                         ("c0vm  tests/task4/static5.bc0", 377),
                         ("c0vmd tests/task4/static5.bc0", 377),
                         ("c0vm  tests/task4/static6.bc0", 86),
                         ("c0vmd tests/task4/static6.bc0", 86)],
                        "Problem with different numbers of arguments/locals."):
        score += 1.0

    if expect_successes([("c0vm tests/task4/recursion1.bc0", 362880),
                         ("c0vm tests/task4/recursion2.bc0", 1),
                         ("c0vm tests/task4/recursion3.bc0", 610),
                         #("c0vm tests/task4/recursion4.bc0", 0),
                         ],
                        "Problem with recursive functions."):
        score += 1.0

    if expect_codes([("c0vmd tests/task4/recursion4.bc0", C0VM_ABRT()),
                     ("c0vmd tests/task4/recursion6.bc0", 38)],
                    "athrow and assert inside a recursive call"):
        score += 1.0

    if expect_successes([("c0vm tests/task4/recursion5.bc0", -1849350655)],
                        "Recursively computes 7^1,000,000. Will likely fail if recursion is not efficiently implemented with a callstack data structure.",
                        timeout = 30):
        score += 1.0

    if score >= 2.0:
        print "-"*50
        print "Score before valgrind #5: "+str(score)+" (max deduction 2.5)"
        score = grind_deductions(["c0vm tests/task4/static1.bc0",
                                  "c0vm tests/task4/static4.bc0",
                                  "c0vm tests/task4/static5.bc0",
                                  "c0vm tests/task4/static6.bc0"],
                                 score = score,
                                 leaky = 1,
                                 safety = 1.5)

    if expect_successes(["c0vm  tests/task4/native1.bc0",
                         "c0vmd tests/task4/native1.bc0",
                         "c0vm  tests/task4/native2.bc0",
                         "c0vmd tests/task4/native2.bc0",
                         "c0vm  tests/task4/native3.bc0",
                         "c0vmd tests/task4/native3.bc0",
                         "c0vm  tests/task4/native4.bc0",
                         "c0vmd tests/task4/native4.bc0"],
                        "Problem with invokenative."):
        score += 2.0

    if expect_successes([("c0vm tests/task4/returnstring.bc0", 4),
                         ("c0vm tests/task4/string12.bc0", 8)],
                        "Functions that return strings"):
        score += 1.0

    if expect_successes([("c0vm tests/task4/string1.bc0", 8),
                         ("c0vm tests/task4/string2.bc0", 20),
                         ("c0vm tests/task4/string3.bc0", 0),
                         ("c0vm tests/task4/string4.bc0", 1),
                         #("c0vm tests/task4/string5.bc0", 8),
                         ("c0vm tests/task4/string6.bc0", 0),
                         #("c0vm tests/task4/string7.bc0", 8),
                         ("c0vm tests/task4/string8.bc0", 0),
                         ("c0vm tests/task4/string9.bc0", 0),
                         ("c0vm tests/task4/string10.bc0", 0),
                         ("c0vm tests/task4/string11.bc0", 0)],
                        "invokenative and the string library.\n*** NOTE: "+\
                            "this could also be a problem with strings, "+\
                            "aldc, or invokestatic/return"):
        score += 1.5

    if expect_aborts(["c0vm tests/task4/string5.bc0",
                      "c0vm tests/task4/string7.bc0"],
                     "invokenative and the string library (negative numbers)",
                     timeout=10):
        score += 1.0

    return score

def test_memory_after_final_deadline(tasknum): # 8 points total
    print "="*50
    print "Testing task " +str(tasknum)+ " (memory)"

    score = 0.0

    # 3.5 points allocated on *MLOAD/*MSTORE

    if expect_successes([("c0vm  tests/task5/intmem.bc0", 5),
                         ("c0vmd tests/task5/intmem.bc0", 5)],
                        "IMLOAD/IMSTORE (store 5 then read it back out)"):
        score += 0.5

    if expect_successes(["c0vm  tests/task5/charmem.bc0",
                         "c0vmd tests/task5/charmem.bc0"],
                        "CMLOAD/CMSTORE (store 'c' then read it back out)"):
        score += 0.5

    if expect_successes(["c0vm  tests/task5/ptrmem.bc0",
                         "c0vmd tests/task5/ptrmem.bc0"],
                        "AMLOAD/AMSTORE (store NULL then read it back out)"):
        score += 0.5

    if expect_codes([("c0vm  tests/task5/stringmem.bc0", 43),
                     ("c0vm  tests/task5/stringmem.bc0", 43)],
                    "AMLOAD/AMSTORE (store string then read it back out)"):
        score += 0.5

    if expect_successes([("c0vm  tests/task5/alloc1.bc0", 137),
                         ("c0vmd tests/task5/alloc1.bc0", 137),
                         "c0vm  tests/task5/alloc3.bc0",
                         "c0vmd tests/task5/alloc3.bc0",
                         ("c0vm  tests/task5/alloc4.bc0", 1),
                         ("c0vmd tests/task5/alloc4.bc0", 1)],
                        "More IMLOAD/IMSTORE tests and pointer equality tests"):
        score += grind_deductions(["c0vm tests/task5/intmem.bc0",
                                   "c0vm tests/task5/charmem.bc0",
                                   "c0vm tests/task5/ptrmem.bc0",
                                   "c0vm tests/task5/alloc1.bc0",
                                   "c0vm tests/task5/alloc4.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.25)

    if expect_codes(["c0vm  tests/task5/alloc5.bc0",
                     "c0vmd tests/task5/alloc5.bc0",
                     "c0vm  tests/task5/null1.bc0",
                     "c0vmd tests/task5/null1.bc0",
                     "c0vm  tests/task5/null2.bc0",
                     "c0vmd tests/task5/null2.bc0",
                     "c0vm  tests/task5/null3.bc0",
                     "c0vmd tests/task5/null3.bc0",
                     "c0vm  tests/task5/null4.bc0",
                     "c0vmd tests/task5/null4.bc0",
                     "c0vm  tests/task5/null5.bc0",
                     "c0vmd tests/task5/null5.bc0",
                     "c0vm  tests/task5/null6.bc0",
                     "c0vmd tests/task5/null6.bc0"],
                    "Null pointer dereference",
                    expected_code=C0VM_SEGV()):
        score += 0.5

    if expect_successes(["c0vm  tests/task5/charzero.bc0",
                         "c0vmd tests/task5/charzero.bc0",
                         "c0vm  tests/task5/intzero.bc0",
                         "c0vmd tests/task5/intzero.bc0",
                         "c0vm  tests/task5/ptrzero.bc0",
                         "c0vmd tests/task5/ptrzero.bc0"],
                        "Reading default vaules from uninitalized pointers"):
        score += grind_deductions(["c0vm tests/task5/charzero.bc0",
                                   "c0vm tests/task5/intzero.bc0",
                                   "c0vm tests/task5/ptrzero.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.5)

    # 1 point allocated to struct offsets

    if expect_successes([("c0vmd tests/task5/alloc6.bc0", 4),
                         ("c0vm  tests/task5/alloc6.bc0", 4),
                         ("c0vmd tests/task5/alloc7.bc0", 65),
                         ("c0vm  tests/task5/alloc7.bc0", 65),
                         ("c0vmd tests/task5/struct1.bc0", 6),
                         ("c0vm  tests/task5/struct1.bc0", 6),
                         ("c0vmd tests/task5/struct3.bc0", 6),
                         ("c0vm  tests/task5/struct3.bc0", 6)],
                        "Struct offsets"):
        score += 0.5

    if expect_codes(["c0vm  tests/task5/null7.bc0",
                     "c0vmd tests/task5/null7.bc0",
                     "c0vm  tests/task5/null8.bc0",
                     "c0vmd tests/task5/null8.bc0",
                     "c0vmd tests/task5/struct4.bc0",
                     "c0vm  tests/task5/struct4.bc0"],
                    "Null pointer dereference in AADDF",
                    expected_code=C0VM_SEGV()):
        score += 0.5

    if expect_codes(["c0vmd tests/task5/array3.bc0",
                     "c0vm  tests/task5/array3.bc0",
                     "c0vmd tests/task5/array4.bc0",
                     "c0vm  tests/task5/array4.bc0",
                     "c0vmd tests/task5/chararray4.bc0",
                     "c0vm  tests/task5/chararray4.bc0"],
                    "Array out-of-bounds errors",
                    expected_code=C0VM_SEGV()):
        score += 0.5

    if expect_successes(["c0vmd tests/task5/intarrays.bc0",
                         "c0vm  tests/task5/intarrays.bc0"],
                        "Arrays of int"):
        score += grind_deductions(["c0vm tests/task5/intarrays.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.25)

    if expect_successes(["c0vmd tests/task5/chararrays.bc0",
                         "c0vm  tests/task5/chararrays.bc0"],
                        "Arrays of char"):
        score += grind_deductions(["c0vm tests/task5/chararrays.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.25)

    if expect_successes(["c0vmd tests/task5/ptrarrays.bc0",
                         "c0vm  tests/task5/ptrarrays.bc0"],
                        "Arrays of int pointers"):
        score += grind_deductions(["c0vm tests/task5/ptrarrays.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.25)

    if expect_successes(["c0vmd tests/task5/stringarrays.bc0",
                         "c0vm  tests/task5/stringarrays.bc0"],
                        "Arrays of strings (uses native library)"):
        score += grind_deductions(["c0vm tests/task5/stringarrays.bc0"],
                                  score = 0.5,
                                  leaky = 0,
                                  safety = 0.25)

    # Last one-point check

    if expect_successes(["c0vm tests/task5/args.bc0 hello world",
                         "c0vmd tests/task5/args.bc0 hello world"],
                        "Using invokenative to check struct/array layout"):
        score += 1

    return score

#unused
def test_memory():
    score = 0

    if expect_successes([("c0vmd tests/task5/array1.bc0", 42),
                         ("c0vm  tests/task5/array1.bc0", 42),
                         ("c0vmd tests/task5/array2.bc0", 120976),
                         ("c0vm  tests/task5/array2.bc0", 120976),
                         ("c0vmd tests/task5/array6.bc0", 4950),
                         ("c0vm  tests/task5/array6.bc0", 4950),
                         ("c0vmd tests/task5/array7.bc0", 0),
                         ("c0vm  tests/task5/array7.bc0", 0),
                         "c0vmd tests/task5/chararray1.bc0",
                         "c0vm  tests/task5/chararray1.bc0",
                         "c0vmd tests/task5/chararray2.bc0",
                         "c0vm  tests/task5/chararray2.bc0",
                         "c0vmd tests/task5/chararray3.bc0",
                         "c0vm  tests/task5/chararray3.bc0"],
                        "Arrays"):
        score = score+2

    if expect_success("c0vm tests/task5/allarrays.bc0",
                      "Reading/writing different-length arrays of ints, chars, and pointers"):
        print "-"*50
        print "Valgrind #6 is a 1-pointer checking array usage initialization"
        score += grind_deductions(["c0vm tests/task5/allarrays.bc0"],
                                  score = 1, leaky = 0, safety = 1)


    if expect_successes([("c0vm tests/task5/zerostruct.bc0", 10),
                         ("c0vm tests/task5/zeroarray.bc0", 10),
                         ("c0vm tests/task5/zerostructarray.bc0", 10)],
                        "Arrays and structs and zero-initialization (xcalloc)"):
        print "-"*50
        print "Valgrind #7 is a 1-pointer checking mem initialization"
        score += grind_deductions(["c0vm tests/task5/zerostruct.bc0",
                                   "c0vm tests/task5/zeroarray.bc0",
                                   "c0vm tests/task5/zerostructarray.bc0"],
                                  score = 1,
                                  leaky = 0,
                                  safety = 1)

    if expect_codes(["c0vmd tests/task5/array3.bc0",
                     "c0vm  tests/task5/array3.bc0",
                     "c0vmd tests/task5/array4.bc0",
                     "c0vm  tests/task5/array4.bc0",
                     "c0vmd tests/task5/array5.bc0",
                     "c0vm  tests/task5/array5.bc0",
                     "c0vmd tests/task5/chararray4.bc0",
                     "c0vm  tests/task5/chararray4.bc0"],
                    "Array errors",
                    expected_code=C0VM_SEGV()):
        score = score+2

    if expect_successes(["c0vmd tests/task5/alloc8.bc0",
                         "c0vm  tests/task5/alloc8.bc0"],
                        "Struct offsets and invokenative"):
        score = score+1

    if expect_successes(["c0vmd tests/task5/alloc2.bc0",
                         "c0vm  tests/task5/alloc2.bc0"],
                        "Char pointers/arrays and invokenative"):
        score = score+1

    if expect_successes(["c0vm tests/task5/string1.bc0",
                         "c0vm tests/task5/string2.bc0",
                         "c0vm tests/task5/string3.bc0",
                         "c0vmd tests/task5/struct2.bc0",
                         "c0vm  tests/task5/struct2.bc0"],
                        "invokenative and the string library"):
        score = score+2

        print "-"*50
        print "Score before valgrind #8: "+str(score)
        print "Not checking for memory leaks anymore!"
        score = grind_deductions(["c0vm tests/task5/alloc1.bc0",
                                  "c0vm tests/task5/string1.bc0",
                                  "c0vm tests/task5/string3.bc0",
                                  "c0vm tests/task5/struct2.bc0"],
                                 score = score,
                                 leaky = 0,
                                 safety = 5)

    return score

def main():
    (task1, task2, task3, task4, task5) = (0, 0, 0, 0, 0)

    def report(num, score):
        print "-"*50
        print "Task "+str(num)+" score: "+str(score)
#        print "="*50

    print "="*50
    print "Testing that code compiles"
    if expect_exists("c0vm", "VM must compile without -DDEBUG")\
            and expect_exists("c0vmd", "VM must compile with -DDEBUG"):
        task1 = test_arithmetic(1)
        report(1, task1)

        task2 = test_locals(2)
        report(2, task2)

        if not CHECKPOINT:
            task3 = test_conditionals(3)
            report(3, task3)

            task4 = test_functions(4)
            report(4, task4)

            if POSTFINAL:
                task5 = test_memory_after_final_deadline(5)
                report(5, task5)
            else:
                print "="*50
                print "Task 5 (memory) graded after final submission deadline!"
                task5 = 0
    else:
        print "Skipping other tests..."
        print "="*50

    print '='*50
    print "Task 1: "+str(task1)+"/15"
    print "Task 2: "+str(task2)+"/10"
    total = task1 + task2
    if not CHECKPOINT:
        print "Task 3: "+str(task3)+"/7"
        print "Task 4: "+str(task4)+"/10"
        if POSTFINAL:
            print "Task 5: "+str(task5)+"/8"
        else:
            print "Task 5: 8 points, graded after the final deadline"
        total = task3+task4+task5

    print "\n*** FINISHED!"
    if CHECKPOINT:
        print "*** TOTAL CHECKPOINT SCORE: ",
        print total
    else:
        print "*** TOTAL POST-CHECKPOINT SCORE: ",
        print total

    # Print JSON results and exit
    if CHECKPOINT:
        print json.dumps({'scores': {'arithmetic': task1,
                                     'locals':     task2}})
    else:
        if POSTFINAL:
            print json.dumps({'scores': {'conditionals': task3,
                                         'functions':    task4,
                                         'memory':       task5}})
        else:
            print json.dumps({'scores': {'conditionals': task3,
                                         'functions':    task4}})
#                          'scoreboard': [task1+total,
#                                         nice_html(task1,15),
#                                         nice_html(task2,15),
#                                         nice_html(task3,20),
#                                         nice_html(task4,15),
#                                         nice_html(task5,10)]})


if __name__ == "__main__":
    print "TESTING..."
    main()
