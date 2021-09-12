"""Drawing forests in a loop."""

__author__ = "730307473"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

TREE2 = TREE + " "

depth: int = int(input("Depth: "))
depth1 = 1
i: int = 0

while depth1 <= depth:
    print(TREE * depth1)
    depth1 = depth1 + 1