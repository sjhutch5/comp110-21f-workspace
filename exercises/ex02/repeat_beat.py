"""Repeating a beat in a loop."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0

beat2 = beat + " "

while i < number:
    print(beat2 * number)
    i = number
if number <= 0:
    print("No beat...")