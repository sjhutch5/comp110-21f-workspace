"""Counting letters in a string."""

__author__ = "730307473"


# Begin your solution here...
letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
count = 0

while i < len(word):
    if letter == word[i]:
        count = count + 1
    else:
        count = count
    i = i + 1

print("Count: " + str(count))