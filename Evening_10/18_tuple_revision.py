#################################################
#  18.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 TUPLE  IN PYTHON
#################################################


# REVISION
# immutable
# hashable
#            0 1 2 3 4
list_even = [2,4,6,8,10]

#        0 1 2 3 4
t_odd = (1,3,5,7,9)

print(list_even)
print(t_odd)


print(list_even[3])
print(t_odd[3])


print(list_even[2:7])
print(t_odd[1:5])


print(list_even[0:3:2])
print(t_odd[0:3:2])



print(type(list_even))
print(type(t_odd))


#            0 1 2 3 4
list_even = [2,4,6,8,10]

#        0 1 2 3 4
t_odd = (1,3,5,7,9)



list_even[4] = 100
print(list_even)

# any type of editing is not supported in a tuple
# immutable
# t_odd[4] = 99 #does not support item assignment
# print(t_odd)

t_even = (2,4,6,8)


t_num = t_even + t_odd #concate
print(t_num)


# unique representation/address
# hashable / fingerprint
print(id(t_even))
print(id(t_odd))
print(id(t_num))


# mutable
# un hashable
#            0 1 2 3 4
list_even = [2,4,6,8,10]


print(list_even)
print(id(list_even))
list_even[0] = 22
print(id(list_even))
print(list_even)


# changable/mutable  : unhashable eg: list
# unchangable/immutable :  hashable eg : tuple




# workaround for editing a tuple


t_alpha = ('M', 'I', 'N', 'S', 'K', 'O', 'L', 'E')
print(t_alpha)
# converting to list

z = list(t_alpha)
print(z)

z.append("I")
print(z)

y = tuple(z)
print(y)


print("***********")

s1 = (1,2,3,4,5)
print(s1)
s2 = list(s1)
s2.append(6)
print(s2)
s3 = tuple(s2)
print(s3)



print(id(s1))
print(id(s2))
print(id(s3))


print(s1.count(5))
print(s1.index(2))




# packing/unpacking
#      0  1  2   3 
t1  = (5,55,555,5555)
print(t1[0])
print(t1[1])
print(t1[2])


a ,b, c ,d = t1

print(a)
print(b)
print(c)

# a ,b, c = t1 #too many values to unpack

# a ,b, c ,d,f = t1 #not enough values to unpack

#       0     1    2    3
city = ('P', 'U', 'N', 'E') #packing 

print(city[0])
print(city[3])
print(city[1])


a ,b ,c ,d = city #unpacking

print(a)
print(b)
print(c)
print(d)


# palce holder

a ,b ,_ ,_ = city # _ is a placeholder

print(b)
print(_) # latest value


t = 1
t = 2
t = 3
print(t) # latest value


t_num = (1,2,3,4,5,6,7,8,9)

a,b,c,d,e,f,g,h,i = t_num
_,b,_,d,_,f,_,h,_ = t_num # we need even numbers

print(b,d,f,h)
# print(d)
# print(f)
# print(h)