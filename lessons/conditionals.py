"""An example of conditional statements."""

SECRET: int = 3

print("I am thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed corrrectly!!!")
    print("Have a wonderful day")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low.")

print("Game over.")    