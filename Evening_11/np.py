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