'''
1. Create a class with below attribute 

group  =  'dog'
age   =  7
class  = 'canine'

also create a method named Display() to print below

"Dog is man's Best friend"

call above attributes and methods by creating object named

Tommy

'''
class c1:
    group  =  'dog'
    age   =  7
    clas  = 'canine'
    def Display():
        return "Dog is man's Best friend"

Tommy=c1
print(Tommy.group)
print(Tommy.age)
print(Tommy.clas)
print(Tommy.Display())