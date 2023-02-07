#################################################
#  28.11.2022 04.00 PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################

# Polymorphism
    #Overriding
        # user defind method
        # inbulit method/magic methods


    # Overloading
        # method
        # operator 


# Polymorphism in built in function

name  =  "Ravindra Kumar Saini"
print(len(name))
print(type(name))

list_e  =[2,4,6,8]
print(len(list_e))
print(type(list_e))

a = 100
b = 200
print(a+b)

x = "Ramesh"
y = "Jain"
print(x+y) #concatenation


#Overriding
    # user defind method

class India:
    def capital(self):
        print("New delhi")

class Nepal:
    def capital(self):
        print("kathmandu")

class SriLanka:
    def capital(self):
        print("Colombo")


ind = India()
nep = Nepal()
sl = SriLanka()


ind.capital()
nep.capital()
sl.capital()

#Overriding
    # user defind method


class Vehicle:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def speed(self):
        print("Max Speed in 200")

class Car(Vehicle):
    def speed(self):
        print("Max Speed in 120")
    # super().speed()


v = Vehicle("maruti", "White")
v.speed()

c = Car("tata" ,"Blue")
c.speed()



# inbulit method/magic methods

print(100)
print([10,20,30])
print("Have a good day")

#Example
class Person:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
    def __str__(self):
        return "{} {}".format(self.fn ,self.ln)
    
p1 = Person("Vikas" ,"Jain")

print(p1)

class double:
    def __init__(self,amount,days) -> None:
        self.amount= amount
        self.days = days
    def __len__(self):
        return 3*self.days
d1 =  double(5000,25)

print(len(d1))
