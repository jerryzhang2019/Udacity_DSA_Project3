
#Problem 2 - Search in a Rotated Sorted Array

Find a number in the middle by walking through the array, then compare the middle value with the value you want to find, and then look up or down. Finally, the value found is returned equal to the target value. If the target value is not in the array, return -1
The time complexity is O(log(n)) , because it's a half search of array, which is less than order O(n).

The space complexity is O(1), because I just used a list and index to search answer, not use  extra more spcace.
