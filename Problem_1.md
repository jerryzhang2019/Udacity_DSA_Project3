
#Problem 1 - Squre root of an integer

Instead of using python's own library functions to solve this problem, I used the most basic mathematical algorithms.
One of the boundary values is that the input value is 0 or 1, and the return value is the input value itself-0 or 1. If the input value is 16, the return value is 4. If the input value is a number that cannot be squared, the result only takes the integer part and rounds off the fractional part.

The time complexity is O(log(n)) , because it's a half search, which is less than order O(n).

The space complexity is O(1), because I just used a list and index to search answer, not use more spcace.
