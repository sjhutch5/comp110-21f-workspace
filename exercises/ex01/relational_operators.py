"""Boolean variable exercise program."""
__author__ = "730307473"

left_side: int = int(input("How many are on the left side? "))
right_side: int = int(input("How many are on the right side? "))
print("Left-hand side: " + str(left_side))
print("Right-hand side: " + str(right_side))

Less = left_side < right_side
GreaterEqual = left_side >= right_side
Equal = left_side == right_side
NotEqual = left_side != right_side


print(str(left_side) + " < " + str(right_side) + " is " + str(bool(Less)))
print(str(left_side) + " = " + str(right_side) + " is " + str(bool(GreaterEqual)))
print(str(left_side) + " == " + str(right_side) + " is " + str(bool(Equal)))
print(str(left_side) + " != " + str(right_side) + " is " + str(bool(NotEqual)))