#program 1
class Student:
    #properties
    name = "chinmay"
    age = 33
    #method
    def talk(self):
        print('Talks too much !')

chinmay  = Student()
print(chinmay.name) # chinmay
print(chinmay.age) #33
chinmay.talk()

amol = Student()
print(amol.name)
print(amol.age)
amol.talk()

print(amol.name)
amol.name = "amol"
print(amol.name)
print(amol.age)
amol.age = 32
print(amol.age)

# program2

class Vehicle:
    # fields
    color = "red"
    model ="SUV"

    # methods
    def start(self):
        print('starting')
    def stop(self):
        print('stopped')


#Object1
audi = Vehicle()
print(audi.color)
print(audi.model)
audi.start()
audi.stop()
audi.color = "black"

#Object2
bwm = Vehicle()
print(bwm.color)
print(bwm.model)
bwm.start()
bwm.stop()

#Contrcutor















#Human 
# Property -- age color height weight gender
# method - talk() , walk()

#Vehicle
#Property -- color modelNo
#Method start() method()

#Bank -
# accNo , IFSC code , branchName
# Method - withdrawl() deposit()