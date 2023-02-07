#################################################
#  18.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 OOP IN PYTHON
#################################################

# Object Oriented Programming 
# Oriented =  way of writng the code 
# Object ???
# Everything in Python is an Object 

# visiting old terms 

a  = 100
list_num = [1,20,30,55,"Akash"]
name = " Prasenjeet"
print(type(a))
print(type(list_num))


# methods vs functions ???
print(len(list_num))
print(type(list_num))
print(name.upper())
# functions inside a class are methods !!!


# collecting data from students for admission
s1 = ["Vikas" , "N" , "PCM" , "IT"]
s2 = ["Rohan" , "N" , "PCB" , "Gardening"]
s3 = ["PCM" , "S" , "Saket"]

# better way of data collection 
s1 = {
    'name' : "Vikas",
    'Area' : "N",
    'Sub' :  "PCM",
    'Optional' : "IT"
}

s2 = {
    'name' : "Rohan",
    'Area' : "N",
    'Sub' :  "PCB",
    'Optional' : "Gardening"
}

s3 = {
    'name' : "Saket",
    'Area' : "S",
    'Sub' :  "PCM",
    'Optional' : "IT"
}

# we found the code is repetative in nature

class StudentData:

    name= "Vikas"
    Area = "N"
    Sub =  "PCM"
    Optional= "IT"
print("----------")

s4 =  StudentData()
print(s4.name)
print(s4.Area)
print(s4.Sub)
print(s4.Optional)


s5 = StudentData()
print(s5.name)
print(s5.Area)
print(s5.Sub)
print(s5.Optional)

# changing the values by the object
s5.name = "Rakesh"
s5.Area = "S"
print(s5.name)
print(s5.Area)
print("----------")
# original value in the class will remain unchanged
print(s4.name)
print(s4.Area)


print("***Attributes accessed by the Class")
print(StudentData.Area)
print(StudentData.Sub)

# new objects will also get the old values of the attributes

s6 = StudentData()
print(s6.name)
print(s6.Sub)