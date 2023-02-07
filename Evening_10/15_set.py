#################################################
#  15.10.2022
#################################################
#  TOPICS TO BE COVERED 
#  TUPLES  IN PYTHON
# PACKING/UNPACKING TUPLES  IN PYTHON
# SETS  IN PYTHON
#################################################


a = False
b = True
# c = "Prakash"
print(int(a))
print(int(b))

# z = 123
# # print(int(c))
# print(str(z))
# print(list(c))



# PACKING/UNPACKING TUPLES  IN PYTHON

# a = "Minskole"
# b ="Pune"

# a , b,c = "Minskole","Pune", 400093

# print(a)
# print(b)
# print(c)

# t_even = (2,4,6,8,10,12) #packing 
# # accessing the values in normay way
# print(t_even[0])
# print(t_even[1])
# print(len(t_even))

# print("***#unpacking****")
# a ,b, c,d,e,f = t_even #unpacking

# print(f)
# print(e)

# t_even = (2,4,6,8,10,12)
# a,b,c,,,_ = t_even #_ is used a splace holder


# print(_)
# print(a)
# print(b)
# print(c)
# print(_)

# a,b,c,,,,k = t_even # is used a splace holder
# a,b,c,, = t_even #_ is used a splace holder





#SETS



# SET IS A COLLECTION 
# OBJECTS 
# ORDER ??


# set is an unordered collection of unique elements

# using set() to create a set
a = set()
print(a)
print(type(a)) # <class 'set'>

# unique collection
list_buy = [1,12,15,14,12,48,48,48,48]


s = set(list_buy)
print(s)

list_new = [12,14,1.44,3.14,"NUm1", True, (True,False),[33,66,99]]

# v = set(list_new)
# print(list_new) # unhashable type: 'list'



list_new = [(True,False),(True,False),(True,False), False, True,12,22]
v = set(list_new)
print(v)


# set is an unordered collection of unique elements
name = "NAMAN"
print(set(name))


# set is an unordered collection of unique elements
# creating  a set data type

s = {11,22,33,44,55}
print(s)


# print(s[0]) #'set' object is not subscriptable
# print(s[2])

# we can not call elements of  a set by calling the index position

# but we can use loop for calling
for i in s:
    print(i)