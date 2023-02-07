#################################################
#  29.11.2022 04.00 PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################

# Polymorphism
    #Overriding
        # user defind method
        # inbulit method


    # Overloading
        # method
        # operator 

# Method overloading


print(100)
print(100,200)
print(100,200,300)


def add1(x,y):
    print(x+y)

add1(10,20)
# add1(10,20,30)


# Ex
class maths():
    def area(self,a):
        print(a*a)

s1 = maths()
s1.area(10)

# we need to write extra logic for overloading 
# over riding : same name 
class maths():
    def area(self,a,b=0):
        if b > 0:
            print(a*b)
        else:
            print(a*a)


m1 = maths()
m1.area(23,33)
m1.area(23)

# ex:
class Greet:
    def Hello(self,name=None):
        if name is not None:
            print("Hello "+ name)
        else:
            print("Hello")

g1 =  Greet()
g1.Hello()
g1.Hello("Sanket")

# method overloading using magic methods


#Example
class Person:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln

    # def show_name(self):
    #     print("{} {}".format(self.fn ,self.ln))

    def __str__(self):
        return "{} {}".format(self.fn ,self.ln)
    
p1 = Person("Vikas" ,"Jain")
x = "Ramesh"
print(x)

# p1.show_name()
print(p1)
print("--------------")

p2 = Person("Sunil" , "Yadav")
print(p2)

class  Books:
    def __init__(self,pages):
        self.pages = pages
    def sum_pages(self,other):
        return self.pages + other.pages

    def __add__(self,other):
        return self.pages + other.pages

    def __sub__(self,other):
        return self.pages - other.pages

z1 = Books(300)
print(z1.pages)

z2 = Books(50)
print(z2.pages)

print("--------------")
print("Using operator overloading:" , z1 + z2)

print(z1.sum_pages(z2))

print(z1 + z2) 
print(z1 - z2) 
print("--------------")
print(10+20)
print((10).__add__(20))
