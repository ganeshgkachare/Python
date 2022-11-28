#################################################
#  19.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON
#################################################
# OOP


class Student:
    pass   

s1 = Student()
print(type(s1))


class StudentData:
    # class attributes/variables
    name= "Vikas"
    Area = "Nagpur"
    Sub =  "PCM"
    Optional= "IT"

    # defining the method/behavour

    def display():
        print("This is a method ")


s4 =  StudentData()
print(s4.name)
print(s4.Area)
print(s4.Sub)
print(s4.Optional)

# changing the attribute 
s4.Area = "Jalandhar"
print(s4.Area)


s5 = StudentData()
print(s5.Area)


# after changing the attribute by class 
print(StudentData.Area)
StudentData.Area = "Pune"
print(s5.Area)
print(s4.Area)

s6 = StudentData()
print(s6.Area)


s6.Area = "Patna"
print(s6.Area)

StudentData.display()

# s4.display()



# understanding the self in python


class StudentData:
    # class attributes/variables
    name= "Vikas"
    Area = "Nagpur"

    # defining the method/behavour
    def I_Am(shaktiman):
        print(id(shaktiman))
        print("I will save the world")

# StudentData.I_Am()

gangadhar = StudentData()
print(gangadhar.name)
print(gangadhar.Area)
print("******")
gangadhar.I_Am()
print(id(gangadhar))


class StudentData:
    # class attributes/variables
    name= "Vikas"
    Area = "Nagpur"

    # defining the method/behavour
    def I_Am(self):
        print(id(self))
        print("I will save the world")

print("*******")
s10  = StudentData()
s10.I_Am()

# another way of calling the method
# background working 
#  
StudentData.I_Am(s10)

class Employees:
    name = "Rakesh"
    Profile  =  "SDE"

    def location(self):
        print('posted in Jaipur')
        transfer = 100
        print(transfer)



e1 =  Employees()
e2 = Employees()
e3 =  Employees()


e1.location()
e2.location()
e3.location()

Employees.location(e1)
Employees.location(e2)
Employees.location(e3)