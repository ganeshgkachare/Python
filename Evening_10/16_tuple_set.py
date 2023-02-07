#################################################
#  16.10.2022
#################################################
#  TOPICS TO BE COVERED
# 👉 SETS  IN PYTHON
#################################################


'''
1 .DATA TYPES IN PYTHON
> NUMBERS 
    > INT       :1 2 3 4  400
    > FLOAT     :3.14 22.22 0.033
    > COMPLEX  : 1+2J
> BOOLEAN True/False 0/1
>LIST [any type of data ]
>STRINGS '' or " " or ''' '''
> TUPLE ()
> SETS {}
'''


# checking data types when singe element is there inside () or {}

# tuples

# k1 = (33)
# k2 = ('33')
# k3 = ("Pune")

# print(k1)
# print(type(k1))
# print(k2)
# print(type(k2))
# print(k3)
# print(type(k3))

print("********")


# k1 = (33,)
# k2 = ('33',)
# k3 = ("Pune",)

# print(k1)
# print(type(k1))
# print(k2)
# print(type(k2))
# print(k3)
# print(type(k3))

print("********")

# z1 = {33}
# z2 = {'33'}
# z3 = {"Pune"}
# print(z1)
# print(type(z1))
# print(z2)
# print(type(z2))
# print(z3)
# print(type(z3))

# z3 = {}
# print(z3)
# print(type(z3))



# SETS
# set is an 
# unordered 
# collection of 
# unique elements



# s1 = {0,1,2,3,4,5,6,7,99,99,22,22}
# print(s1)

# #empty set 
# s2 = set() #constructor
# print(s2)

# list_even = [2,4,6,8,88,88,88,88]
# print(set(list_even))

# name = "GayaTRi"
# print(set(name))

# bool1  = (False,)
# print(type(bool1))
# print(set(bool1))



# accessing data in a set

s1 = {0,1,2,3,4,5,6,7,99,99,22,22}

# print(s1[1]) # object is not subscriptable

# for i in s1:
#     print(i)

print("*****lenght**")
print(len(s1))

s2 = {1,1,1,1,1,1,1,1,1,1,1,1}
print(len(s2))


# methods for editing

s_7 = {7,77,777,7777}
s_8 = {8,88,888,8888}

# add the elemt 77777

s_7.add(77777)

print(type(s_7.add((7,7)))) # supports data types that are immutable
print(s_7)

s_8.add("EIGHT")
print(s_8)



# sorted

# s1 = {0,1,2,3,4,5,6,7,99,99,22,22}
# print(sorted(s1)) # returns a LIST


# s1 = {0,1,2,3,4,5,6,7,99,99,22,22,"pune"}
# print(sorted(s1)) # returns a LIST

b1 = {False,True, False, 2}
print(sorted(b1))


#remove
s1 = {0,1,2,3,4,5,6,7,99,99,22,22,"pune"}
s1.remove("pune")
print(s1)


# clear

s1 = {0,1,2,3,4,5,6,7,99,99,22,22,"pune"}
s1.clear()
print(s1)