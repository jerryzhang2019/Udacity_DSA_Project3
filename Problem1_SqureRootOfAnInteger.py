
# coding: utf-8

# In[1]:


#Problem 1: Square Root of an Integer
def sqrt(number):
    if number is None:
        return 0
    if number < 0:
        return 'The input value is negative, please re-enter'
    
    x = number
    y = (x + 1) // 2
    while y < x :
        x = y
        y = (x + number // x) // 2  
    return x

print(sqrt(None)) # 0
print(sqrt(-1))   #The input value is negative, please re-enter
print(sqrt(0))    #0
print(sqrt(1))    #1
print(sqrt(9))    #3
print(sqrt(16))   #4
print(sqrt(27))   #5

print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

