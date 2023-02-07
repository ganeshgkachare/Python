# print(list(range(10,1,-1)))
# print(reversed(list(range(1,11))))
# a=print(list(reversed(range(1,11))))
# print(a)
# b="a;b;c;"
# c=b.split(";")
# print(c,len(c))

# for i in range(5):
#     print(i)
# else:
#     print("Done")

# x=1j
# print(x**2==-1)

# z= "my name is ganesh"
# print([1,2,3]*3)

###########################

myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)


str1 = "my isname isisis jameis isis bond";
sub = "is"
print(str1.count(sub, 4))

print("John" > "Jhon")
print("Emma" < "Emm")
#("a    b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z")

str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

str = "My salary is 7000"
print(str.isalnum())

# strOne = str("pynative")
# strTwo = "pynative"
# print(strOne == strTwo)
# print(strOne is strTwo)

str = "my name is James bond"
print (str.capitalize())
print (str.title())


str1 = "My salary is 7000";
str2 = "7000"
# Space is not an alpha numberic character
print(str1.isdigit())
print(str2.isdigit())


a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)