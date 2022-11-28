person = {
    'firstName':"chinmay",
    'lastName':'deshpande',
    'age':12,
    'skills':["python","java","javascript"]
}

# retrive
print(person['firstName'])
# update 
person['firstName'] = "Tanmay"
print(person)
# add
person['city'] = "pune"
print(person)
# delete
del person['city']
print(person)

# length()
print(len(person))

#in 

person2 = {
    'firstName':"chinmay",
    'lastName':'deshpande',
    'age':12,
    'skills':["python","java","javascript"]
}
print('age' in person2)
#not
print('city' not in person)

#copy
vehicle = {
    "color":"red",
    "typec":"seda"
}
vehicle2 = vehicle
vehicle2["color"] = "blue"

print(vehicle)
print(vehicle2)

# loops

student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
    'age':45
}

for x in student:
    print(x,student[x])

#dictionary methods

student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}

# clear()
# student.clear()
# print(student)

#copy
student3 = student.copy()
student3['age']= 45
print(student3)
print(student)


student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}

#get
q1 = student.get('firstName')
print(q1)

#loops
#keys()

student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}

for key in student.keys():
    print(key)

#values()
for val in student.values():
    print(val)

#items()
for key,val in student.items():
    print(key,val)

#update()
student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}
student.update({"firstName":"tanmay","age":56})
print(student)

#pop()
student.pop('age')
print(student)

# fromkeys()
keys = ["student1","student2","student3"]
y = None
d = dict.fromkeys(keys,y)
print(d)

# {
#     'student1':None
#     'student2':None
#     'student3':None
# }

# setDefault()

student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}

student.setdefault('city','pune')
print(student)