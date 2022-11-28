# Rules of global Keyword
# The basic rules for global keyword in Python are:

# When we create a variable inside a function, it is local by default.
# When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
# We use global keyword to read and write a global variable inside a function.
# Use of global keyword outside a function has no effect.





#program7
# def printT():
#     t = 900
#     print(t) #900
# printT()
# print(t)

# z = 450
# def printZ():
#     z = 900
#     print(z)  # 900
# printZ()
# print(z) # 450

# x = 450
# def printX():
#     print(x)   # 450
# printX()
# print(x) # 450

def printR():
    global r 
    r= 100
    print(r) # 100
    r = 700

printR()
print(r) # 700

# program 8
# Lamda function
# f = lambda x:x*x
# print(f(5))

# q  = lambda j,y:j+y
# print(q(12,13))

# q2 = lambda x,y: x if x > y else y
# print(q2(22,399))


# program1
def addAll(a,b,c):
    print(a+b+c)
addAll(11,22,33)


# program2
def addAllB(*args):
    print(args)
    return sum(args)
q1 = addAllB(11,22,33,44,55,66,77,88,99,66,77,88,99,66,66)
print(q1)

#program3
def displayPV(**kwargs):
    print(kwargs.items())
    for k,v in kwargs.items():
        print(k,v)
displayPV(firstName="chinmay",lastName="deshpande",age=25)


# k = 10,11
# print(k)
# print(type(k))

# a1,b1 = k
# print(a1)
# print(b1)

#local and global

# program4

# only in local scope
def addA():
    a = 10
    print(a)
addA()
# print(a) not accessible


# program5
# only in global scope 
b = 90
def addB():
    print(b) # 90
addB()
print(b) # 90


# program6
# different in local and global scope
# c = 100
# def addC():
#     c = 89
#     print(c) #89

# print(c) # 100
# addC()
# print(c) 

# program 7
d = 100
def addD():
    print(d) 
   
print(d) # 100
addD()
print(d) # 100

# global

# e1 = 9000
# def addE():
#     global e1 
#     e1 =100
#     print(e1)
# print(e1) # 9000
# addE()
# print(e1)


# program 8
e2 = 9000
def addF():
    global e2 
    e2 = 100
    print(e2) # 100
print(e2) #9000
addF()
print(e2) # 100

# lambda
# filter reduce map

# program 9
def square(x):
    return x * x
print(square(12))
print(square(3))


q1 = lambda x:x*x
print(q1(12))
print(q1(6))

# program 10
a1 = lambda x,y:x+y
print(a1(12,3))


def findGreater(x,y):
    if(x > y):
        print("x is greater")
    else:
        print("y is greater")

findGreater(12,4)
q3 = lambda x,y: x if x > y else y
print(q3(12,66))




print("###########################################")


a=8

def num():
    global a
    a=5
    return(a)

print(a)  #2
print(num())  #

print(a)  #
