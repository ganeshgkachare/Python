#program

# class Student:
#     name ="chinmay deshpande"
#     age =10
#     rollNo =34

#     def displayName(self):
#         print("hello")

# s1 = Student()
# print(s1.name)
# print(s1.age)
# print(s1.rollNo)
# s1.displayName()


# s2 = Student()
# print(s2.name)
# print(s2.age)
# print(s2.rollNo)
# s2.displayName()

# s2.name = "amol r"
# s2.age = 23
# s2.rollNo = 33
# print(s2.name)
# print(s2.age)
# print(s2.rollNo)

# program 
class Student:
    #constructor
    def _init_(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age

    def displayName(self):
        print(self.name)

poorva = Student("poorva vyas",29,33)
amar = Student("amar r",34,56)

print(poorva.name)
print(poorva.age)
print(poorva.roll)

print(amar.name)
print(amar.age)
print(amar.roll)


# program


class Sample:
    def _init_(self):
        # instance  variable
        self.x = 10

    def modify(self):
        self.x = self.x+1

q1 = Sample()
q2 = Sample()

print(q1.x)
print(q2.x)

q1.modify()
print(q1.x)

print(q2.x)


class Student2:
    # class variable
    language ="hindi"
    def _init_(self,name,age,rollNo):
        self.name = name
        self.age = age
        self.rollNo = age

    def displayName(self):
        print(self.name)

vikas = Student2("vikas",23,34)
sarika = Student2("sarika",33,44)

print(vikas.language)
print(sarika.language)

print(sarika.name)
print(sarika.rollNo)
print(sarika.age)

print(vikas.name)
print(vikas.rollNo)
print(vikas.age)





class Student2:
    # class variable
    language ="hindi"
    def _init_(self,name,age,rollNo):
        self.name = name
        self.age = age
        self.rollNo = age

    def displayName(self):
        print(self.name)

    @classmethod
    def modifyLanguage(cls):
        cls.language = "marathi"

vikas = Student2("vikas",23,34)
sarika = Student2("sarika",33,44)

print(vikas.language)
print(sarika.language)

print(sarika.name)
print(sarika.rollNo)
print(sarika.age)

print(vikas.name)
print(vikas.rollNo)
print(vikas.age)

vikas.modifyLanguage()
print(vikas.language)
print(sarika.language)