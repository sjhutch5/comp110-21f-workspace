"""Finding duplicate letters in a word."""

__author__ = "730307473"

word: str = input("Enter a word: ")
length: int = 0
i: int = 0
k: int = 0
count: int = 0

while i < len(word) - 1:
    k = i + 1
    while k < len(word):
        if word[i] == word[k]:
            count = count + 1
        k = k + 1
    i = i + 1

if count > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")