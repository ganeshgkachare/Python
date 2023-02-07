#################################################
#  12.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
#################################################
import numpy as np

# Revision

# Creating arrays
# array vs list 
        # fast
        # elementwise operation


list_e = [2,4,6,8]
print(2*list_e)

arr1 = np.array(list_e)
print(list_e)
print(arr1)
print(2*arr1)


tup_num = (1,2,3,4,5,6)

arr2 = np.array(tup_num)
print(arr2)


print(list(range(10)))

arr3 = np.arange(10).reshape(2,5)
print(arr3)

arr3 = np.arange(10).reshape(5,2)
print(arr3)


arr3 = np.arange(10,100).reshape(9,10)
print(arr3)


arr3 = np.arange(10,100,10).reshape(3,3)
print(arr3)

arr3 = np.arange(10,100,10.5).reshape(3,3) # Step size in fractions
print(arr3)

z = np.zeros(10)
print(z)

z = np.zeros([5,3])
print(z)


o = np.ones(10)
print(o)

o = np.ones([5,3])
print(o)


e = np.eye(5)
print(e)
print(e.ndim)
print(e.dtype)
print(e.size)


# 
#  
    # using native data types list and tupel
    # using arange and resaping array
    # using linspace
            #1d
            #2d
    # initial placeholder
            #zeros
            # ones
            # eye
            # random
# Imp attributes

            # print(z.ndim)
            # print(z.dtype)
            # print(z.size)

# operations on array
    # basic universal
    # aggregate



arr3 = np.arange(10,100,10).reshape(3,3)
print(arr3)

arr4 = np.arange(100,1000,100).reshape(3,3)
print(arr4)

print(arr3+arr4)
print(arr3-arr4)
print(arr3*arr4)
print(arr3/arr4)


print(np.sum(arr3))
print(np.sum(arr4))

print(np.min(arr3))
print(np.min(arr4))


print(np.max(arr3))
print(np.max(arr4))


print(np.max(arr3 ,axis=1))
print(np.max(arr3 ,axis=0))


print(np.min(arr3 ,axis=1))
print(np.min(arr4, axis=0))


# Indexing and Slicing

arr6  = np.arange(10,100,10)
print(arr6)
print(arr6[2])
print(arr6[5])
print(arr6[3:5])
print(arr6[3:])
print(arr6[:])
print(arr6[::-1])