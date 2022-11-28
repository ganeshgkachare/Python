class num:
    for i in range(1,10):
        i*5

print(num.i)

for i in range(1,10):
    print(i*5)



#################################################
#  26.11.2022 08.45 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON 
#################################################
# Inheritance
    # single
        # Method over riding
    # multiple
        # MRO Method resolution Objective
        # super()
    # multi level

    # Next class how to inherit constructor
        # _init_ 


class Person:


    def person_info(self,name,age):
        self.name = name
        self.age =  age


class Employee(Person):
    def emp_info(self, salary):
        self.salary = salary


p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)


# example 

class Father:
    def f_info(self):
        print("I am Father")

class Child(Father):
    def c_info(self):
        print("I am child")



c1 = Child()
print(type(c1))

c1.f_info()
c1.c_info()


class Person:
    def person_info(self,name,age):
        self.name = name
        self.age =  age

    def character(self):
        print("Good Citizen")


class Employee(Person):
    def emp_info(self, salary):
        self.salary = salary

    def character(self):
        print("Good manager")

p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)


p1.character()
e1 = Employee()

e1.character()


# multiple
    # MRO Method resolution Objective
    # super()


class Person:
    def person_info(self,name,age):
        self.name = name
        self.age =  age

    def character(self):
        print("Good Citizen")


class Company1:
    def comp_info_reg(self):
        print("Google")
    def star(self):
        print("Star emp at Google")
    def views(self):
        print("You have 100 views in Google review")

class Company2:
    def comp_info_free(self):
        print("Youtube")
    def star(self):
        print("Star emp at Youtube")
    def views(self):
        print("You have 100 views in Youtube")



class Employee(Person, Company1,Company2):
# class Employee(Person, Company2,Company1):
    def emp_info(self, salary):
        self.salary = salary

    def character(self):
        print("Good manager")
        super().views()

print("-----------")

p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)


e1 = Employee()
e1.comp_info_free()
e1.comp_info_reg()

# e1.star() #google
e1.star() # changing the order

e1.character() # MRO will be used in case of conflict