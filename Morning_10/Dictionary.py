# # Defining the dict with values
#     # dict does not stores the value by index

# student=["abc","HSC",88]
# print(student[1])


# person = {
#     "firstName":"Ganesh",
#     (3,5,6):6,
#     "Age":22
# }

# print(person)
# print(type(person))


# # retrive Method
# #print(person[1]) #KeyError
# #retrive 1
# fn = person["firstName"]
# print(fn)
# print(person["Age"])

# # retrive 2
# fn2 = person.get('LaststName',"not found")
# fn3 = person.get('Age')
# print(fn2)
# print(fn3)
# print("---------------")
# print(person.get('firstName'))

# # update
# person["Age"]=23

# print(person)

# #Add
# person["lastName"]="kachare"
# print(person)

# person["lastNames"]="Kachare_G"
# print(person)
# print("---------------")

# #Delete
# del person["lastNames"]
# print(person)

#

# print(person)
# print("---------------")
# # duplicate key in dictionary (updated by last value)
# person["lastName"]="Kachare"
# print(person)
# print("---------------")

# # dict with membership operator (in,not in) (check keys)
# print("firstName" in person)
# print("Kachare" in person)
# print("Kachare" not in person)

# #Loops
# for key in person:
person = {
    "firstName":"Ganesh",
    "lastName":"Pawar",
    "Age":22
}

# keys()
print(person.keys())
print("---------------")
# values()
print(person.values())
print(type(person.values()))

# items()
print(person.items())


# keys()
for x in person.keys():
    print(x)

# values
for x in person.values():
    print(x)

#items()
for x , y in person.items():
    print(x,y)

# Nested Dictionary

family = {
    'son':"chinmay",
    'daughter':'gauri',
    'parent':{
        'mother':'kanchan',
        'father':'shirish'
    },
    'skills':["python","c++"]
} 
print(family['parent']['father'])
family['parent']['mother'] ='kanchan s' 
family['skills'].append('js')

a = sum([22,33,44])
print(a)


j = {
    'studentOne':45,
    'studentTwo':90,
    'studentThree':45
}
print(sum(j.values()))
