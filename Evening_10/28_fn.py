# #################################################
# #  28.10.2022 9.00AM
# #################################################
# #  TOPICS TO BE COVERED
# # 👉 FUNCTION  IN PYTHON
# #  https://docs.python.org/3.10/library/functions.html
# #################################################

# syntax 

'''
def name_of_function(x,y,z,....):
    code 

'''


def func2(x,y,z):
    pass

# print(func2()) # missing 3 required positional arguments:
print(func2(10,20,30)) 


def mul(a,b):
    z = a*b
    print(z)


mul(10,50)
mul(7,50)
print(mul(2,2))
print("---------------------------")
ans  = mul(4,44)
print(type(ans))
print(ans)


def mul(a,b):
    z = a*b
    return z

ans  = mul(14,44)
print(type(ans))
print(ans)

def allin1(a,b):
    z = a*b
    w = a+b
    y = a/b
    return z,w,y


ans  = allin1(10,50)
print(ans)
print(type(ans)) #tuple

print(ans[0])
print(ans[1])
print(ans[2])

# unpacking of tuple
ans1, ans2, ans3  = allin1(10,50)

print(ans1 , ans2 ,ans3)

# placeholder
ans1, _, _  = allin1(10,50) # not interested in ans2 and ans3

print(ans1 , _ ,_)


def func5(a):
    z = a*2
    return z


ans = func5("MINSKOLE")
print(ans)

# list/tuple as input


list_num = [1,2,3,4,5,6]

def func6(a):
    return a*2


ans = func6([1,2,3,4,5,6])
print(ans)
print(type(ans))



def double(z):
    s = []

    for i in range(len(z)):
        s.append(z[i]*2)
    return s

ans  = double([1,2,3,4,5,6])
print(ans)

ans1 = double([11,22,33,44])
print(ans1)

ans3 = double((11,22,33,44))
print(ans3)
print(type(ans3))


# returning multiple values when my i/p is list/tuple
def double(z):
    s = []

    for i in range(len(z)):
        s.append(z[i]*2)
    return s ,z

ans1 = double([11,22,33,44])
print(ans1)
print(type(ans1))
print(ans1[1]) # printin the value of z only


























































































print("******************default*********************")
def allin1(a,b):
    z = a*b
    w = a+b
    y = a/b
    return z,w,y
ans = allin1(5,2)
print(ans)
print(type(ans))
print("*****************ls**********************")
def allin1(a,b):
    z = a*b
    w = a+b
    y = a/b
    return [z,w,y]
ans = allin1(5,2)
print(ans)
print(type(ans))
print("****************tup***********************")
def add(a,b):
    w = a+b
    return w
ans = add(5,2)
print(ans)
print(type(ans))
print("*****************tup**********************")
def add(a,b):
    w = a+b
    return (w)
ans = add(5,2)
print(ans)
print(type(ans))
print("******************ls*********************")
def add(a,b):
    w = a+b
    return [w]
ans = add(5,2)
print(ans)
print(type(ans))
print("***************ls,int************************")
a=[5]
print(a,type(a))
a=(8)
print(a,type(a))