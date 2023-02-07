#################################################
#  07.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
# https://onecompiler.com/python/
#################################################

# NUMPY??
    # Library
    # Scientific computing

# How to install numpy using pip
# pip install numpy

# checking numy installation 
#  pip list


import numpy as np

z = [1,2,3,4,5,6,7,8,9]
print(type(z))

# to double each element in the list z

print(z*2) # this will not work


ans  = []
for i in z:
    ans.append(i**2)
print(ans)


# to perform element wise operation in a list, we have to use a loop
# to simplify this we transfrom the lsit into an array 

num = 100.25
print(type(num))

num1 = int(num)
print(type(num1))

print("*******")

# converting  list into an array 
z = [1,2,3,4,5,6,7,8,9]
a = np.array(z)
print(a)
print(type(a)) #<class 'numpy.ndarray'>


# using tuple
z1 = (1,2,3,4,5,6,7,8,9)
a1 = np.array(z1)
print(a1)
print(type(a1)) #<class 'numpy.ndarray'>


print("*******")
# creating 2d array

a1 = np.array([1,2,3,4,5,6,7,8,9])
print(a1)
a2 = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(a2)

# creating 3d array
a3 = np.array([[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]])
print(a3)

# Imp attributes

print(a1.ndim) 
print(a2.ndim)
print(a3.ndim) # x/y/z axis count

# a2 = np.array([[1.0,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
# print(a2.dtype.name)
# print(a2)

a2 = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(a2.dtype.name)
print(a2)


# a2 = np.array([['1',2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
# print(a2.dtype.name)
# print(a2)

print(a2.size) # elements count
print(a1.size)
print(a3.size)


print(a1.itemsize)


a2 = np.array([[1.0,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
print(a2.dtype.name)
print(a2)


z = [1,2,3,4,5,6,7,8,9]
a = np.array(z)
print(a)
print(type(a)) #<class 'numpy.ndarray'>
print(a.ndim)
print(a.dtype.name)
print(a.itemsize) # memory space occupied 

#using reshape and arange


############################################

'''
1. using below list try to create using 1d,2d and 3d array:
 s = [1,2,3]

2. Print imp attributes for each array created in above ques :
imp attributes are :
                    ndim
                    dtype.name
                    size
                    itemsize

share o/p screenshot
'''