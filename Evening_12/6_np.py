#################################################
#  06.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
# https://onecompiler.com/python/
#################################################

# NUMPY??
    # Library
    # Scientific computing

# use online compiler

import numpy as np

z = [1,2,3,4,5,6,7,8,9]
print(z)
print(type(z))
a = np.array(z)
print(type(a))

# Creating arrays

# 1D array
a1 = np.arange(15) # same as range 
print(a1)
print(type(a1))


a1 = np.arange(5) # same as range 
print(a1)
print(type(a1))

#2D array

z2 = [[1,2,3,4,5,6,7,8,9] , [1,2,3,4,5,6,7,8,9]]
a = np.array(z2)
print(a)
print(type(a))

# reshape to convert the array dimension
# 2D array

a = np.arange(15).reshape(1,15)
print(a)








#################################################################

# HW

'''
1. Write a code to generate below list using range 
w = [0, 1, 2, 3, 4, 5, 6, 7, 8]
p = [10, 15, 20, 25, 30, 35, 40, 45]

2. convert w and p into :
    1D array
3. reshape w  into  2D array of size(3,3) using reshape
    and p into array of size(2,4)
'''
