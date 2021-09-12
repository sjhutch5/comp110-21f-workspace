"""An exercise in remainders and boolean logic."""

__author__ = "730307473"


# Begin your solution here...
integer: int = int(input("Enter an int: "))
integer3 = integer % 2
integer4 = integer % 7
integer5 = integer3 + integer4

if integer3 + integer4 == 0:
    print("TAR HEELS")
else:
    if integer3 == 0:
        print("TAR")
    else:    
        if integer4 == 0:
            print("HEELS")
        else:
            print("CAROLINA")