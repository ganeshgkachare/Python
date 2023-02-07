# # program 
# class Student:
#     def __init__(self):
#         self.name = "chinmay"
#         self.age = 20
#         self.marks = 900
#     def talk(self):
#         print('Hi my name is ',self.name)
#         print('Hi my age is ',self.age)
#         print('Hi my marks is ',self.marks)

# amit = Student()
# amol = Student()
# amit.talk()
# amol.talk()

# program 2

class StudentB:
    def __init__(self,name,age,marks):
        self.name = name
        self.marks = marks
        self.age = age
        
    def talk(self):
        print('Hi my name is ',self.name)
        print('Hi my age is ',self.age)
        print('Hi my marks is ',self.marks)

amol2 = StudentB("amol",34,900)
chinmay2 = StudentB("chinmay2",33,800)
amol2.talk()
chinmay2.talk()

# program3

class StudentC:
    # class level variable
    language = "hindi"

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age 
        self.marks  = marks


    # instance varaible
    def talk(self):
        print('Hi my name is ',self.name)
        print('Hi my age is ',self.age)
        print('Hi my marks is ',self.marks)
        print('Hi my marks is ',self.language)

    #class method 
    @classmethod
    def changeLang(cls):
        cls.language = "Marathi"



sarika = StudentC("sarika",24,700)
poorva = StudentC("sarika",24,700)

print(sarika.language)
print(poorva.language)

sarika.talk()

sarika.changeLang()
print(sarika.language)
print(poorva.language)
    
sarika.language = "english"
print(sarika.language)
print(poorva.language)

# Accessor and mutators
# get and set

class StudentD:
    def setName(self,name):
        self.name = name
  
    def getName(self):
        return self.name
    ####################################
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age

    ###################################
    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

chinmayD = StudentD()
chinmayD.setMarks(900)
chinmayD.setName("chinmay D")
chinmayD.setAge(32)

age = chinmayD.getAge()
marks = chinmayD.getAge()
name = chinmayD.getName()
print(age)
print(marks)
print(name)

# // hardcode value 
# // constructor (hardvalues)
# // passing parameter to constructor 
# // using mutators and accessors
class Bird:
    wings = 2

    @classmethod
    def fly(cls,birdName):
        print("I have",cls.wings,"wings",birdName)


Bird.fly('pigeon')
Bird.fly('sparrow')

print("---------")

# class Bird:
#     wings = 2

#     # @classmethod
#     def fly(birdName):
#         print("I have", wings ,"wings",birdName)


# Bird.fly('pigeon')
# Bird.fly('sparrow')