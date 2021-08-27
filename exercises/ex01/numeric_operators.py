"""Integer/String variable exercise."""
__author__ = "730307473"

left_side: int = int(input("How many are on the left side? "))
right_side: int = int(input("How many are on the right side? "))
print("Left-hand side: " + str(left_side))
print("Right-hand side: " + str(right_side))

Exponentiation = left_side ** right_side
Division = left_side / right_side
Integer = left_side // right_side
Remainder = left_side % right_side


print(str(left_side) + " ** " + str(right_side) + " is " + str(Exponentiation))
print(str(left_side) + " / " + str(right_side) + " is " + str(Division))
print(str(left_side) + " // " + str(right_side) + " is " + str(Integer))
print(str(left_side) + " % " + str(right_side) + " is " + str(Remainder))