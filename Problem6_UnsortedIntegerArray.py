
# coding: utf-8

# In[1]:


#Problem 6: Unsorted Integer Array
def get_min_max(ints):
    min = ints[0]
    max = ints[0]
    for num in ints:
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)

import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

#Test cases#1:
ints = [1,2,3,4,5]
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#Test cases#2:
ints = [1]
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#Test cases#3:
ints = []
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

