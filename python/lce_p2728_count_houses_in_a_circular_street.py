"""
LCE 2728. Count Houses in a Circular Street (Premium)

You are given an object street of class Street that represents a circular street and a positive integer k which represents a maximum bound for the number of houses in that street
(in other words, the number of houses is less than or equal to k). Houses' doors could be open or closed initially.

Initially, you are standing in front of a door to a house on this street.
Your task is to count the number of houses in the street.

The class Street contains the following functions which may help you:
- void openDoor(): Open the door of the house you are in front of.
- void closeDoor(): Close the door of the house you are in front of.
- boolean isDoorOpen(): Returns true if the door of the current house is open and false otherwise.
- void moveRight(): Move to the right house.
- void moveLeft(): Move to the left house.

Return ans which represents the number of houses on this street.

Constraints:
- n == number of houses
- 1 <= n <= k <= 103

Topics:
- Array
- Interactive
"""


# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional["Street"], k: int) -> int:
        # move to each house (choose 1 direction) and ensure their doors are opened
        for _ in range(k):
            if not street.isDoorOpen():
                street.openDoor()

            street.moveRight()

        # move to each house (choose 1 direction) and ensure their doors are closed
        # if the doors are initially closed, it means we have reached the starting point
        ans = 0
        while street.isDoorOpen():
            street.closeDoor()

            street.moveRight()

            ans += 1

        return ans


# Time Complexity: O(k) - 177 ms -> 23.53%
# Space Complexity: O(1) - 18.56 MB -> 70.59%
