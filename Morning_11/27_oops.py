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
print("------------")

#case- | no relationship()
# chinmayT = Teacher()
print(chinmayT.salary)

# case-I 
chinmay = Student("chinmay",32,123)
print(chinmay.name)
print(chinmay.age)
print(chinmay.adharNo)
chinmay.displayName()
##########################################################

class Student:
    def __init__(self,name, age , roll):
        self.name = name 
        self.age = age 
        self.rollNo = roll
    def displayName(self):
        print(self.name)


class Teacher(Student):
    def __init__(self,name,age,roll,salary):
        super().__init__(name,age,roll)
        self.salary = salary



amolT = Teacher("amol",25,23,1235)
amolT.name
amolT.age
amolT.rollNo
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

print("--------")
amit = Professor("chi",23,1000,'hindi') 

print(amit.fullName)
print(amit.age)
print(amit.salary)
print(amit.specialization)

amit.displayFullName()
amit.displaySalary()
amit.displaySpec()


#  1 parent two childs

class Father():
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(self.firstName , self.lastName)
    

class Son(Father):

    def __init__(self,firstName,lastName,sname):
        super().__init__(firstName,lastName)
        self.sname = sname

    def sdisplay(self):
        print(self.sname , self.lastName)
    

class Daughter(Father):
    def __init__(self,firstName,lastName,dname):
        super().__init__(firstName,lastName)
        self.dname = dname

    def ddisplay(self):
        print(self.dname , self.lastName)

gauri = Daughter('shirish',"deshpadne","gauri")
chinmay = Son('shirish',"deshpadne","chinmay")

gauri.ddisplay()
chinmay.sdisplay()



# Method order resolution


class FatherA:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+self.lastName)
        print('Father method called')

class MotherA:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+self.lastName)
        print('Mother method called')

class SonB(MotherA,FatherA):
    pass
chinmay = SonB("shirish","deshpande")

chinmay.displayName()
print(chinmay.firstName)

#--------------------------------------------

class A(object):
    def method(self):
        print('A method called ') #3
        super().method()

class B(object):
    def method(self):
        print('B method called ') # 5
        super().method()

class C(object):
    def method(self):
        print('C method called ')  #6
     

class X(A,B):
    def method(self):
        print('X method called ')  # 2
        super().method()

class Y(B,C):
    def method(self):
        print('Y method called ')   # 4
        super().method()

class P(X,Y,C):
    def method(self):
        print('P method called ') #1 
        super().method()

p = P()
p.method()