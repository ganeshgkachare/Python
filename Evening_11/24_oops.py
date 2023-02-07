#################################################
#  24.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################
# encapsulation

class PowerPlant:
    name  = "CSTP"

    def __init__(self, location,capacity, employees,):
        # self.location =  location # public
        self.__location =  location # private , sensitive info
        self.capacity = capacity
        self.employees = employees
        print(id(self.__location))

    # getter
    # accessor
    def locate(self):
        return self.__location

    #setter
    # modifier
    def locate_change(self,new):
         self.__location  = new
         return self.__location




p1 = PowerPlant("Nasik", '500MW' , 150)


print(p1.capacity)
print(p1.employees)
# print(p1.location) # this will give error

p1.__location = "tarapur" #this created a new atrribute 
print(p1.__location) # no attribute 

print(id(p1.__location))

p1.hello = "nagpur"
print(p1.hello)

# accessing a private variable 

# through method inside the class

print(p1.locate())

# through name mangling 

print(p1._PowerPlant__location)
print(id(p1._PowerPlant__location))


# changing  a private variable 

# through name mangling 

p1._PowerPlant_location = "Satara" #changing
print(p1.locate()) # accessing thr method
print(p1._PowerPlant_location) # acc through name mangling 





# through method inside the class
# _classname__identifier
print('-------')
p1.locate_change("Chennai")
print(p1.locate())
print(id(p1._PowerPlant__location))
print(p1._PowerPlant__location)
print('-------')


