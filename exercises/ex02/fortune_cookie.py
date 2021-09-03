"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730307473"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

number: int = randint(1, 3)

if number == 1:
    print("You will have a great year")
else:
    if number == 2:
        print("You will change the world")
    else:
        if number == 3:
            print("You are going to crush it!")
        else:
            if number == 4:
                print("I predict greatness from you!")            

print("Now go spread positive vibes!")