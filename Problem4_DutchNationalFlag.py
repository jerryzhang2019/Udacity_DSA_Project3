
# coding: utf-8

# In[6]:


#Problem 4: Dutch National Flag Problem
def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """    
    low = 0
    mid = 0
    high = len(input_list) - 1
    while mid <= high:
        if input_list[mid] == 0:
            swap(input_list, low, mid)
            low += 1
            mid += 1
        elif input_list[mid] == 2:
            swap(input_list, mid, high)
            high -= 1
        elif input_list[mid] == 1:
            mid += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

