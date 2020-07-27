# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactlyese keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """

    tries = 0
    guess = 0
    # low = 0
    # high = 100
    # actual_number = 16
    #while (low <= high and guess !)
    
    guess = int((low + high)/2 )
    # guess = high
    # num_pool = []
    # while actual_number < average:
    while True:
        # try:
        ddd = {"guess": guess, "tries": tries}
        ddd.update(ddd)
        tries = tries +1
        # ddd.update(ddd.keys())
        # ddd["tries"] = [i+1 for i in ddd["tries"]]
        # tel["guess"] = ["guess"] + 1
        # new = [i+1 for i in ddd['tries']]
        # ddd.update({"tries": new})
        print(ddd)
        if actual_number == guess or guess == high or high == low or actual_number == low:
            return True
        elif actual_number - 1 == guess:
            guess = guess + 1
            return True
        elif actual_number + 1 == guess:
            guess = guess - 1
            return True
        elif actual_number < guess:
            guess = int((low + guess)/2 )
            high = guess
        elif actual_number > guess:
            guess = int((guess + high)/2 )
            low = guess
        else:
            return True
        # except Exception as e:
        #     print("that's not a number", e)





    # return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
