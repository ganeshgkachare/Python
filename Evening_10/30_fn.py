#################################################
#  31.10.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 FUNCTION  IN PYTHON
#  https://docs.python.org/3.10/library/functions.html
#################################################


# types of function
    # inbuilt fun
    # custom / user defined
    # lambda , nameless , anonymous

print("Hello World")
x = "Hello World"
print(len(x))
print(type((x)))
print(list(x))



x = 100
y = 20
print(x/y)

a = 66
b = 33
print(a/b)




# syntax 

'''
def name_of_function(x,y,z,....):
    code 

'''

# without paramaters , only using print

print("*******")


def separator():
    print("*********")



separator()


separator()

separator()

# with paramaters


def div_num(a, b):
    print(a/b)



div_num(100,20)
div_num(66,33)

ans  = div_num(66,33)
print(ans)



# function that returns some value
# returning multiple values 
def div_num(a, b):
    return a/b ,a + b,a * b



ans  = div_num(66,33)
print(ans)
print(ans[1])
print(type(ans))



# default values

print("Good Morning " , "Prakash")
print("Good Morning " , "Rohit")

def greeting(wish, name , city= 'Pune'):
    print(wish, name , "Welcome to " , city)

greeting("Good Morning ","Prakash")

greeting("Good Evening  " , "Rakesh")

greeting("Good Morning ","Rohit","Nashik")


separator()

# def greeting(wish= "Hi", name , city= 'Pune'): #non-default argument follows default argument
#     print(wish, name , "Welcome to " , city)
# greeting("Good Morning ","Rohit","Nashik")