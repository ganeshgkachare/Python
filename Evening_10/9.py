

# range
# sequence types

#syntax
# range(start,stop)

x = range(0,11)
print(list(x))


# 3 . PRINT THE FOLLOWING USING range()

# h = "HYDERABAD"
# c = "CHENNAI"
# d = "DELHI"



# for i in h:
#     print(i)

    
# for i in c:
#     print(i)


# for i in d:
#     print(i)



# STRING FORMATTING

#  .format()
# f-string


#  sample ans of above output : 

# s = "sun"
# m = "moon"
# e = "earth"
# print("{0} is farthest from {1} and nearest is {2}".format(s,e,m))


# print(f"{s} is farthest from {e} and nearest is {m}")
# print(f"{e} is farthest from {m} and nearest is {s}")

# # repeat

# # methods
# # finding content
# code1 =  'ZAQ!@WSX'
# # edit 
# name1 = "Ganesh"
# print(name1.upper())
# # boolean
code1 =  'ZAQ!@WSX'
print(code1.isspace())


# #strip()

# ans1 = "     The sum of odd num is even      "

# print(ans1)
# print(ans1.strip())


# Challenge

code1 = "123456"

print(code1.isdigit())
print(code1.isnumeric())
print(code1.isdecimal())


# split

date1 = "12.08.1995"
print(date1.split("."))
print(type(date1))



#type conversion/casting

name1 = "Rahul"

print(name1)
print(list(name1))

n = ['R', 'a', 'h', 'u', 'l']