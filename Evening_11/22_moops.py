#################################################
#  22.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################


# Pillars of OOP
    # abstraction
    # Encapsulation
    # Polymorphism
    # Inheritance


# Encapsulation

class Employee:
    name = "Ekta"
    age = 25
    Grade  = "Z"



e1 = Employee()
print(e1.age)
print(e1.name)
print(e1.Grade)


s1 = Employee()
s1.name = "Sakshi"
s1.age = 24
s1.Grade = "Y"

print(s1.age)
print(s1.name)
print(s1.Grade)

# constructor/initialization
# const is a special method/dunder/magic 
# no default  values

class EmplData:
    def __init__(self,name,age, grade):
        self.name = name
        # self.n = name
        self.age =age
        self.grade  =  grade
        
    def display(self):
        print("The Emply name is {} , age is  {}years  and grade pay is {}".format(self.name,self.age,self.grade))



e1 = EmplData("Roshan", 47 , "E")
print(e1.name , e1.age ,e1.grade)
e1.display()

e2  = EmplData("Ramesh" , 32 , "A")
e2.display()
print(e2.name , e2.age ,e2.grade)
e2.grade = "B"
print(e2.grade)


# Encapsulation


class EmplData:
    def __init__(self,name,age, grade, workex):
        self.name = name
        # self.n = name
        self.__age =age
        self.__grade  =  grade # private/protected variable
        self.__workex = workex

    def display(self):
        print("The Emply name is {} , age is  {}years  and grade pay is {}".format(self.name,self.__age,self.__grade))


e1 = EmplData("Roshan", 47 , "E", 12)
# print(e1.name , e1.age ,e1.grade)
e1.display()

print("***###****")
# print(e1.__age)

e1.display()
# print(e1.workex)
print("****&&***")
e1.workex = 5
print(e1.workex)


print("*******")
# Nothing in Python is private or hidden 
# how to access pvt attributes 
# classsName_attrName



print(e1._EmplData__workex)
print(e1._EmplData__grade)