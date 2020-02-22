#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example of recursive function to find the factorial of a number
def calc_factorial(x):
    """Recursive function to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return(x*calc_factorial(x-1))
    
#Driver
number = 10
print("The factorial of ", number, "is ", calc_factorial(number))

#Programiz


# In[ ]:




