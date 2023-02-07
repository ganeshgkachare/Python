#################################################
#  08.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
# https://onecompiler.com/python/
#################################################

list_num = [1,2,3,4,5,6]

print(list_num*2)

ans = []
for i in list_num:
    ans.append(2*i)
print(ans) # elemnt wise operation


import numpy as np

x = np.array(list_num)
print(x)
print(list_num)
print(type(x))
# we can do element wise op on an array

print(x*2)
print(x**2)


# using tuple to create an array
tup_num = (1,2,3,4,5,6)
a = np.array(tup_num)
print(type(a))
print(a)


# Imp attributes

print(a.ndim) # 1D array , dimension of the aray
print(a.dtype) # data type 
print(a.size) # no of elements
print(a.itemsize) #4 blocks 


# creating array 

a = np.arange(10)
print(a)

a = np.arange(15,25)
print(a)


a = np.arange(0,100)
print(a)

# np.arange(start,stop,stepsize)
a = np.arange(0,100,5)
print(a)

a = np.arange(0,100,10)
print(a)

a = np.arange(0,10,.5) # fractional step count is allowed 
print(a)

# reshape(x) 1D
# reshape(x,y)2D
# reshape(x,y,z)3D
a = np.arange(9).reshape(9)
print(a)
print(a.ndim)

print("******")
a = np.arange(0,18,2).reshape(3,3)
print(a)
print(a.ndim)

print("*# initial placeholder**")

z = np.zeros(3)
print(z)
print(z.ndim)
print(z.dtype)
print(z.size)

z = np.zeros([3,3])
print(z)
print(z.ndim)
print(z.dtype)
print(z.size)


z = np.zeros([10,10])
print(z)
print(z.ndim)
print(z.dtype)
print(z.size)


o = np.ones([10,10])
print(o)
print(o.ndim)
print(o.dtype)
print(o.size)


e = np.eye(3)
print(e)

e = np.eye(10)
print(e)

r = np.random.rand(9).reshape(3,3)
print(r)
print(len(r))

r = np.random.randn(9)
print(r)
print(len(r))


# import matplotlib.pyplot as plt
# r = np.random.randn(9)
# x = list(range(0,9))
# plt.plot(x,r)
# plt.show()