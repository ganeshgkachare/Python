#################################################
#  13.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
#################################################
import numpy as np

# Indexing and Slicing

# arr6  = np.arange(10,100,10)
# print(arr6)
# print(arr6[0])
# print(arr6[5])
# # print(arr6[15])
# print(arr6[0:5])
# print(arr6[0:3])
# print(arr6[0:8:2])
# print(arr6[::-1]) # REVERSING THE ARRAY


arr7 = np.arange(12).reshape(3,4)
# print(arr7)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

'''
print(arr7[0])
print(arr7[1])
print(arr7[2])
print(arr7[0:2])
print(arr7[:])
print(arr7[0,0]) #0
print(arr7[0,1]) # 1
print(arr7[0,3]) # 3
print(arr7[1,2]) # 3
print(arr7[0:2,0:2])
print(arr7[1:,2:])
print(arr7[1:3,2:4])
print(arr7[1:,1:3])


# Indexing with booleans
# Masking 


print(arr7)
print(arr7>7)
print(arr7 % 2== 0)
print(arr7[arr7 % 2== 0])
print(arr7[arr7>7])
print(arr7[arr7<7])
print(arr7[arr7 % 2!= 0])
print(arr7[(arr7 % 2== 0) | (arr7 % 3== 0)]) #or
print(arr7[(arr7 % 2== 0) & (arr7 % 3== 0)]) # AND

arr7 = np.arange(24).reshape(3,4,2)
print(arr7)