#################################################
#  23.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################

# Pillars of OOP
    # Abstraction
    # Encapsulation
    # Polymorphism
    # Inheritance


class StudentData:
    # here are 
    # class attributes
    # eg : school = "Bal Vidya mandir "


    def __init__(self,name, age, area, feepaid):
        # variables defined inside init are 
        # instance (object) attributes
        self.name =  name
        self.age =  age
        self.area = area
        self.feepaid =feepaid



rahul = StudentData("Rahul" , 14 , "Nashik" , True)

print(rahul.name)
print(rahul.age)
print(rahul.area)
print(rahul.feepaid)



rahul.feepaid = False
print(rahul.feepaid)

#making instance attribute private


class StudentData:
    # here are 
    # class attributes
    # eg : school = "Bal Vidya mandir "


    def __init__(self,name, age, area, feepaid):
        # variables defined inside init are 
        # instance (object) attributes
        self.name =  name
        self.age =  age
        self.__area = area
        self.__feepaid = feepaid # private

    def displayFee(self):
        print("Fee paid :" , self.__feepaid)
    

rahul1 = StudentData("Rahul" , 14 , "Nashik" , True)

print("***********")
rahul1.__feepaid =  "Nagpur"

rahul1.__area =  "Karjat"
print(rahul1.__area)

print("***********")
rahul1.displayFee()
print("***********")

class EmplData:
    def __init__(self,name,age, grade, workex):
        self.name = name
        # self.n = name
        self.__age =age
        self.__grade  =  grade # private/protected variable
        self.__workex = workex
    
    def display(self):
        print(self.__workex)


e1 = EmplData("Roshan", 47 , "E", 12)

# e1.__grade = "Z"
# print(e1.__grade)


# accessing a Private attribute 

        # attribute is hidded in python using "name mangling" 
        # Empldata_workex



e1.EmplData_workex = 10
print(e1.EmplData_workex)

# accessor and modifiers
        # getter and setter
        # display and change 


e1.display() # this is a getter

class PowerPlant:


    def __init__(self, location,capacity):
        self.__location =  location
        self.capacity = capacity

    
    def locate(self):
        print("Location is :" , self.__location)



p1 = PowerPlant("Chandrapur", "500W")
p1.locate()

p1.__location =  "Tarapur"