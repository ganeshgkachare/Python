#################################################
#  15.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
#################################################
import numpy as np

# Indexing and Slicing

list_one = [1,11,111,1111]
print(list_one[2])

arr1  =  np.array([1,2,3,4,5])
print(arr1)
print(arr1[2])
print(arr1[2:])

arr2  = np.arange(12).reshape(3,4)
print(arr2)
print(arr2[0])
print(arr2[1])
print(arr2[2])

print(arr2[0,0])
print(arr2[0,1])
print(arr2[1,3])
print(arr2[2,2])

print(arr2[1:,2:])
print(arr2[:,1:2])
print(arr2[:,1:3])

# copy

a = np.array([[ 0 , 1 , 2,  3],
 [ 4,  5,  6,  7],
 [ 8,  9, 10 ,11]])

print(a)
b = a  # Shallow COpy / View 
print(a[0,0])
a[0,0] = 99
print(a[0,0])

print(b)
print(id(a))
print(id(b))

print(b is a)


# deep copy
c =  a.copy()
print(c is a )
print(c is b )

c[0,0] = 999

print(a)
print(c)
print(b)
