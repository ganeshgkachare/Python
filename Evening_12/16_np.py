#################################################
#  16.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
#################################################
import numpy as np


# SHAPE MANIPULATION
# reshape
arr2 =  np.arange(12).reshape(3,4)
print(arr2)


arr2 =  np.arange(12).reshape(4,3)
print(arr2)


arr2 =  np.arange(12).reshape(12,1)
print(arr2)

arr2 =  np.arange(12).reshape(1,12)
print(arr2)

arr3 = np.arange(10,50,5).reshape(2,4)
print(arr3)

arr3 = np.arange(10,50,5)
print(arr3.size)


arr4 = np.linspace(10,11,12).reshape(4,3)
print(arr4)


# flatten ? can changes the values in original array Copy : Deep ? slow
# ravel ? returns a shallow copy ? fast || use this 

arr5 = np.array([[10, 15, 20 ,25],
 [30 ,35, 40 ,45]])

print(arr5)
print(arr5.flatten())

arr6 = np.array([[10, 15, 20 ,25],
 [30 ,35, 40 ,45]])

print(arr6.ravel())
print(arr6)


# transpose


arr8 = np.linspace(10,100,12).reshape(3,4)
print(arr8)
print(arr8.transpose())

#Splitting the arrays


arr8 = np.arange(12).reshape(3,4)

print(arr8.shape)
print(np.split(arr8,3))

print("****vsplit****")
print(np.split(arr8,3,axis=0))
print(np.vsplit(arr8,3))


print("****hsplit****")
print(np.split(arr8,4,axis=1))
print(np.split(arr8,2,axis=1))
np.hsplit(arr8, 2)


# broadcasting


list_zero = [0,0,0,0,0,0]
print(list_zero)
print(list_zero[3])
list_zero[3]= 3
print(list_zero)

# print(list_zero[3:])
# list_zero[3:] =  9


arr1  = np.array(list_zero)
print(arr1)

print(arr1[3:])
arr1[3:] = 9
print(arr1)

print("******")
a1 = np.arange(1,5).reshape(4,1)
print(a1)
print(a1.shape)
a2 = np.arange(1,5).reshape(1,4)
print(a2)
print(a2.shape)

a = a1 + a2


print(a)
print(a.shape)