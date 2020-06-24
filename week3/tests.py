# -*- coding: UTF-8 -*-
"""Run the tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

from colorama import Fore
from colorama import Style
from func_timeout import func_timeout, FunctionTimedOut
from pathlib import Path
import importlib.util as importUtils
import math
import mock
import os
import random
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import (
    completion_message,
    ex_runs,
    finish_up,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    syntax_error_message,
    test,
)

EM = Fore.YELLOW
NORM = Fore.WHITE
TIMEOUT_IN_SECONDS = 3

WEEK_NUMBER = 3


def test_stubborn_asker(repo_path, low, high):
    """Test the stubborn asker function."""
    try:
        exercise1 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=1
        )
    except Exception as e:
        return syntax_error_message(4, e)

    mockInputs = list(range(low - 25, high + 20, 5))
    try:
        with mock.patch("builtins.input", side_effect=mockInputs):
            try:
                x = exercise1.stubborn_asker(low, high)
                if x is not None:
                    result = low <= x <= high
                    return result
                else:
                    print(
                        "Trouble testing the test_stubborn_asker.",
                        "Maybe you haven't started yet?",
                    )
            except Exception as e:
                print(e)
            return
    except Exception as e:
        print("exception:", e)


def test_not_number_rejector(repo_path):
    """Test the not number rejector function."""
    try:
        exercise1 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=1
        )
    except Exception as e:
        return syntax_error_message(1, e)

    mockInputs = ["aword", [1, 2, 3], {"an": "object"}, 40]
    with mock.patch("builtins.input", side_effect=mockInputs):
        try:
            my_args = "Testing some values:"
            r = func_timeout(
                TIMEOUT_IN_SECONDS, exercise1.not_number_rejector, args=[my_args]
            )
            return r
        except FunctionTimedOut:
            print(
                "{f}({args}) could not complete within {t} seconds and was killed.".format(
                    f=sys._getframe().f_code.co_name, args=my_args, t=TIMEOUT_IN_SECONDS
                )
            )
        except Exception as e:
            print("exception:", e)


def test_super_asker(repo_path, low, high):
    """Test the super asker function."""
    try:
        exercise1 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=1
        )
    except Exception as e:
        return syntax_error_message(1, e)

    dirty_things = ["aword", [1, 2, 3], {"an": "object"}]
    neat_range = list(range(low - 25, high + 20, 5))
    mockInputs = dirty_things + neat_range
    with mock.patch("builtins.input", side_effect=mockInputs):
        try:
            my_args = (low, high)
            message = func_timeout(
                TIMEOUT_IN_SECONDS, exercise1.super_asker, args=my_args
            )
            return message
        except FunctionTimedOut:
            print(
                "{f}({args}) could not complete within {t} seconds and was killed.".format(
                    f=sys._getframe().f_code.co_name, args=my_args, t=TIMEOUT_IN_SECONDS
                )
            )
        except Exception as e:
            print(e)


def test_example_guessingGame(repo_path):
    """Test the example_guessingGame function.

    This should always pass becasue it's provided code
    """
    try:
        exercise2 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=2
        )
    except Exception as e:
        return syntax_error_message(2, e)
    upperBound = 5
    guesses = list(range(5 + 1))
    mockInputs = [upperBound] + guesses
    with mock.patch("builtins.input", side_effect=mockInputs):
        try:
            my_args = None
            message = func_timeout(
                TIMEOUT_IN_SECONDS, exercise2.exampleGuessingGame, args=my_args
            )

            return message == "You got it!"
        except FunctionTimedOut:
            print(
                "{f}({args}) could not complete within {t} seconds and was killed.".format(
                    f=sys._getframe().f_code.co_name, args=my_args, t=TIMEOUT_IN_SECONDS
                )
            )
        except Exception as e:
            print(e)


def test_advanced_guessingGame(repo_path, mockInputs):
    """Test the advanced_guessingGame function."""
    try:
        exercise3 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=3
        )
    except Exception as e:
        return syntax_error_message(3, e)

    with mock.patch("builtins.input", side_effect=mockInputs):
        try:
            my_args = None
            message = func_timeout(
                TIMEOUT_IN_SECONDS, exercise3.advancedGuessingGame, args=my_args
            )

            return message == "You got it!"
        except FunctionTimedOut:
            print(
                "{f}({args}) could not complete within {t} seconds and was killed.".format(
                    f=sys._getframe().f_code.co_name, args=my_args, t=TIMEOUT_IN_SECONDS
                )
            )
        except Exception as e:
            print(e)


def test_binary_search(repo_path, low, high, actual):
    # TODO: I don't think this test is working
    """Test the binary search function.

    checks to see that it's searching better than O(log n)
    """
    try:
        exercise4 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=4
        )
        BASE2 = 2
        b = None
        try:
            my_args = (low, high, actual)
            b = func_timeout(TIMEOUT_IN_SECONDS, exercise4.binary_search, args=my_args)
            b["WorstCaseO"] = math.log(high - low, BASE2)
            if b is not None:
                if b["tries"] is not 0 and b["tries"] < b["WorstCaseO"]:
                    print("b", b)
                    print("snuck it in")
                    return True
                elif b["tries"] is 0:
                    print(
                        "Tries is 0, that probably means that you haven't started yet"
                    )
                else:
                    print(
                        (
                            "That took {t} tries, you "
                            "should get it in under {o} tries"
                        ).format(t=b["tries"], o=b["WorstCaseO"])
                    )
            else:
                return False
        except FunctionTimedOut:
            print(
                "{f}({args}) could not complete within {t} seconds and was killed.".format(
                    f=sys._getframe().f_code.co_name, args=my_args, t=TIMEOUT_IN_SECONDS
                )
            )
            return False
        except Exception as e:
            syntax_error_message(4, e)
            return False
    except Exception as e:
        syntax_error_message(4, e)
        return False


def vis_binary_search_performance(repo_path):
    """Provide a visualisation of the performance of the binary search."""
    try:
        exercise4 = loadExerciseFile(
            repo_path, weekNumber=WEEK_NUMBER, exerciseNumber=4
        )
    except Exception as e:
        return syntax_error_message(4, e)

    import matplotlib.pyplot as plt

    BASE2 = 2
    results = []
    testRuns = 1000
    for _ in range(testRuns):
        low = random.randint(-100, 100)
        high = random.randint(low + 2, 200)
        guess = random.randint(low + 1, high - 1)
        bs = exercise4.binary_search(low, high, guess)
        # print bs, low, high, guess
        tries = bs["tries"]
        worst = math.log(high - low, BASE2)
        ratio = tries / worst
        results.append(ratio)
    plt.hist(results)
    plt.title(
        "Proportion of worst case performance " "over {} iterations".format(testRuns)
    )
    print(
        """
This histogram shows the number of guesses that it took the search to
find the answer. The big O worst case is the base 2 log of the range that
you're guessing within. In other words, what power of two fills that space?
E.g. if your range is 16, then the worst case is 4 guesses: 2×2×2×2 = 16
Think back to when you were playing the game with your brain, sometimes
you'd go over the worst case because you aren't a perfect arithmatic
machine but the computer is, so it's always below that worst case limit.

            Close the histogram to finish running the tests."""
    )
    plt.show()


def theTests(path_to_code_to_check="../me"):
    """Run all the tests."""
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    testResults = []

    # Give each person 10 seconds to complete all tests.

    if ex_runs(path_to_code_to_check, exerciseNumber=1, weekNumber=WEEK_NUMBER):
        exercise1 = loadExerciseFile(
            path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=1
        )

        testResults.append(
            test(
                exercise1.loop_ranger(3, 8, 1) == [3, 4, 5, 6, 7],
                "Exercise 1: Loop ranger (3, 8, 1)",
            )
        )
        testResults.append(
            test(
                exercise1.loop_ranger(100, 104, 2) == [100, 102],
                "Exercise 1: Loop ranger (100, 104, 2)",
            )
        )

        testResults.append(
            test(
                exercise1.lone_ranger(3, 8, 1) == [3, 4, 5, 6, 7],
                "Exercise 1: Lone ranger (3, 8, 1)",
            )
        )
        testResults.append(
            test(
                exercise1.lone_ranger(100, 104, 2) == [100, 102],
                "Exercise 1: Lone ranger (100, 104, 2)",
            )
        )

        testResults.append(
            test(
                exercise1.two_step_ranger(100, 104) == [100, 102],
                "Exercise 1: Two step ranger (100, 104)",
            )
        )
        testResults.append(
            test(
                exercise1.two_step_ranger(0, 10) == [0, 2, 4, 6, 8],
                "Exercise 1: Two step ranger (100, 104)",
            )
        )

        # testResults.append(
        #     test(exercise1.gene_krupa_range(0, 10, 2, 1) ==
        #          [0, 2, 3, 5, 6, 8, 9],
        #          "Exercise 1: gene_krupa_range(0, 10, 2, 1)"))
        # testResults.append(
        #     test(exercise1.gene_krupa_range(0, 100, 30, 7) ==
        #          [0, 30, 37, 67, 74],
        #          "Exercise 1: gene_krupa_range(0, 100, 30, 7)"))

        testResults.append(
            test(
                test_stubborn_asker(path_to_code_to_check, 50, 60),
                "Exercise 1: Stubborn asker",
            )
        )

        testResults.append(
            test(
                test_stubborn_asker(path_to_code_to_check, 10, 20),
                "Exercise 1: Stubborn asker",
            )
        )

        testResults.append(
            test(
                test_not_number_rejector(path_to_code_to_check),
                "Exercise 1: not_number_rejector",
            )
        )

        testResults.append(
            test(
                test_super_asker(path_to_code_to_check, 50, 60),
                "Exercise 1: test_super_asker",
            )
        )

    testResults.append(
        test(
            test_example_guessingGame(path_to_code_to_check),
            "Exercise 2: example guessing game",
        )
    )

    if ex_runs(path_to_code_to_check, exerciseNumber=3, weekNumber=WEEK_NUMBER):
        exercise1 = loadExerciseFile(
            path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=3
        )

        lowerBound = 10
        upperBound = 15
        guesses = list(range(lowerBound, upperBound + 1))
        mockInputs = [lowerBound] + [upperBound] + guesses
        testResults.append(
            test(
                test_advanced_guessingGame(path_to_code_to_check, mockInputs),
                "Exercise 3: guessing game, U&L",
            )
        )

        mockInputs = ["ten"] + [lowerBound] + [upperBound] + ["cats"] + guesses
        testResults.append(
            test(
                test_advanced_guessingGame(path_to_code_to_check, mockInputs),
                "Exercise 3: guessing game, polite failures",
            )
        )

        secondGuess = 25
        guesses = list(range(lowerBound, secondGuess + 1))
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(
                test_advanced_guessingGame(path_to_code_to_check, mockInputs),
                "Exercise 3: guessing game, lowerBound " "bigger than upperBound",
            )
        )

        lowerBound = 10
        upperBound = 11
        secondGuess = 15
        guesses = list(range(lowerBound, secondGuess + 1))
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(
                test_advanced_guessingGame(path_to_code_to_check, mockInputs),
                "Exercise 3: guessing game, no " + "range to guess in (delta 1)",
            )
        )

        lowerBound = 10
        upperBound = 10
        secondGuess = 15
        guesses = list(range(lowerBound, secondGuess + 1))
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(
                test_advanced_guessingGame(path_to_code_to_check, mockInputs),
                "Exercise 3: guessing game, no " + "range to guess in (equal)",
            )
        )

    if ex_runs(path_to_code_to_check, exerciseNumber=4, weekNumber=WEEK_NUMBER):
        exercise1 = loadExerciseFile(
            path_to_code_to_check, weekNumber=WEEK_NUMBER, exerciseNumber=4
        )

        try_these = [(1, 100, 5), (1, 100, 6), (1, 100, 95), (1, 51, 5), (1, 50, 5)]
        for _ in range(10):
            try_these.append((0, 100, random.randint(1, 99)))

        for tv in try_these:
            try:
                testResults.append(  # *tv unpacks this tuple -------------- vv
                    test(
                        test_binary_search(path_to_code_to_check, *tv),
                        "Exercise 4: binary_search" + "({}, {}, {})".format(*tv),
                    )
                )
            except Exception:
                print("********\n\nfailed:", tv)
                print("tv failure", Exception)
                # raise ValueError("********\n\nfailed: {}".format(tv))
                testResults.append(0)

        # if the binary search is working, show a graph of guess numbers
        if test(test_binary_search(path_to_code_to_check, 1, 10, 5), ""):
            # If you aren't Ben, then show the histogram
            # if os.uname()[1] != "um":  # um is ben's computer
            print("binary search works!")

    message = "Rad, you've got all the tests passing!"

    return finish_up(testResults, message, nyan_cat())


if __name__ == "__main__":
    theTests()
