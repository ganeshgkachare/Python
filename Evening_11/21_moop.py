#################################################
#  21.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON
#################################################
# TYPES OF METHODS in OOP


# class StudentData:
#     # class attributes
#         #  only class can change 


#     # Instance Methods
    
#     # Instance  attributes
#         #object can change for itselgf


#     # class methods
#     pass



a = 100
print(type(a))

list_e = [10,20,30]
print(type(list_e))

# list_e.append()


x = list()
print(type(x))


p = int()
print(type(p))


# making ouser defined data type with help of CLASS

class Studentdata:
    # constructor
    def _init_(self,name,age):
        self.name = name
        self.age = age
        print("the id of self is : " ,id(self))


    def display(self):
       print("The data for student is  as : name  {} and age {}".format(self.name , self.age))


s1 = Studentdata('Rakesh' ,14)
s1.display( )
print("The ID of s1 is :" ,id(s1))

s2 = Studentdata("Rohan" , 15)
s2.display()
print("The ID of s2 is :" ,id(s2))




class Studentdata:
    school = "St MOunt XYZ"

    # constructor
    def _init_(self,name,age): #d-under methods
        # self.n = name # correct
        self.name = name
        # self.a = age # correct
        self.age = age
        print("the id of self is : " ,id(self))


    def display(self):
       print("The data for student is  as : name  {} and age {}".format(self.name , self.age))

    #
    @classmethod # is used to work with class variables/instance
    def infoSchool(cls):
        print(cls.school)




s3 = Studentdata("Mohan" , 32)
s3.display()

print(s3.school)
s3.school =  "St MOunt PQRS"
print(s3.school)
s3.infoSchool()