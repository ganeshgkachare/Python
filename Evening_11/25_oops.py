#################################################
#  25.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################


#Revision
# Encap
    # Private and Protected attributes


class A:
    def __init__(self,salary):
        self.__salary  =  salary
    
    # getter
    def salary_info(self):
        return self.__salary

    # setter
    def salary_change(self,new):
        if new == 0:
            print("Salary can not be zero")
        else:
            self.__salary = new # private attribute is available/accessible inside a class


a1 = A(5000)
# print(a1.__salary)
print(a1._A__salary)


# name mangling # not recommended
# _salary = _A__salary
# _attribute  =  _ClassName__attribute

a1.salary_change(6000)
print(a1._A__salary)

print(a1.salary_info())

a1.salary_change(0)
print(a1.salary_info())


# Inheritance
    # single
    # multiple
    # multi level



# SINGLE INheritance
# code reuse

class Person:

    # def __init__(self) -> None:
    #     pass

    def person_info(self,name,age):
        self.name = name
        self.age =  age


class Employee(Person):
    def emp_info(self, salary):
        self.salary = salary




p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)


emp1 = Employee()
emp1.person_info("Rakesh", 32) # Employee  obj can acces the Person obj by inheritance 
emp1.emp_info(2000)

print(emp1.name , emp1.age , emp1.salary)



# print( init)
# _one
# __one
# one init #confusion 
# _one_ # not recommended