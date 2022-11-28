#################################################
#  27.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 FUNCTION  IN PYTHON
#  https://docs.python.org/3.10/library/functions.html
#################################################


# sum of two numbers

x = 100
y = 10
z = x + y 
print(z)

p = 200
q = 20
r =  p + q 
print(r)

a = 300
b  = 30
c = a + b
print(c)

# types of function
    # inbuilt fun
    # custom / user defined
    # lambda

list_num = [55,66,77,88]
print(len(list_num))
tup_num = (55,66,77,88)
print(len(tup_num))

# syntax 

'''
def name_of_function(x,y,z,....):
    code 

'''

# writing the 1st function
# def banner():
#     pass

# without paramaters
def banner():
    print(" Welcome to Minskole")
    print(" We are online")

# calling  a fun 

c = banner()
print(c)

print("********")

def sep():
    print("********")

sep()

def pallavi():
    print(" I am learnig Python")

pallavi()

# with paramaters

def fun_sum(x,y):
    z = x + y
    print(z)

fun_sum(100,10)
fun_sum(200,20)
fun_sum(300,30)

def fun_mul(a,b):
    c = a * b
    print(c)


fun_mul(5,10)
fun_mul(50,50)
fun_mul('a',5)
fun_mul('Monday',5)


q = fun_sum(10,100)
# print(2*q)
print(type(q))

# function that returns some value

def fun_sum_return(x,y):
    z = x + y
    return z # this will return the value of 'z'

q = fun_sum_return(10,100)
print(2*q)
print(type(q))


def mul1(a,b):
    d = a * b
    return d 

t = mul1(10,7)
print(t)

def _(b,c): # dont use '' to name a function
    return b+c

print(_(10,41))