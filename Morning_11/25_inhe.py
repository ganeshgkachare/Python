# Inheritance
# student -----> name , age , adharNo
# teacher -----> name , age , adharNo, salary
# professor ----> name , age , adharNo ,salary , spec.

class Student():
    def __init__(self ,name,age,adharNo):
        self.name = name
        self.age = age
        self.adharNo = adharNo

    def displayName(self):
        print(self.name)


# Case 3

class Teacher(Student):
    salary = 1000

chinmayT = Teacher("ram",34,124)
print(chinmayT.salary)
print(chinmayT.age)
print(chinmayT.adharNo)
print(chinmayT.salary)
chinmayT.displayName()


# case- | no relationship()
chinmayT = Teacher()
print(chinmayT.salary)

# case-I 
chinmay = Student("chinmay",32,123)
print(chinmay.name)
print(chinmay.age)
print(chinmay.adharNo)
chinmay.displayName()
###########################################################

class Student:
    def __init__(self,name, age , roll):
        self.name = name 
        self.age = age 
        self.rollNo = roll
    def displayName(self):
        print(self.name)

#Python also has a super() function that will make the child class
# inherit all the methods and properties from its parent

class Teacher(Student):
    def __init__(self,name,age,roll,salary):
        super().__init__(name,age,roll)
        self.salary = salary


amolT = Teacher("amol",25,23,1235)
amolT.name
amolT.age
amolT.roll
amolT.salary
amolT.displayName()


class Student():
    def __init__(self,fullName,age):
        self.fullName = fullName
        self.age = age

    def displayFullName(self):
        print(self.fullName)

class Teacher(Student):
    def __init__(self,fullName, age ,salary):
        super().__init__(fullName,age)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)


class Professor(Teacher):
    def __init__(self,fullName, age ,salary,spec):
        super().__init__(fullName, age ,salary)
        self.specialization = spec

    def displaySpec(self):
        print(self.specialization)


amit = Professor("chi",23,1000,'hindi') 

print(amit.fullName)
print(amit.age)
print(amit.salary)
print(amit.specialization)

amit.displayFullName()
amit.displaySalary()
amit.displaySpec()


#  1 parent two childs