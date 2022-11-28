#################################################
#  29.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
#  👉 DICTIONARY  IN PYTHON
#  https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#################################################

z  = {1,2,3}
print(z)
print(type(z))


print("*******")
z  = {}
print(z)
print(type(z))




# creating a dict

dict1 = {
    1 : "First",
    2 : "Second",
    3 : "Third",
    4 : "Forth"
}


print(dict1)
print(type(dict1))

dict2 = {
    "name" : "Poonam",
    "Class" : 5,
    "Pin" : 400075
}


print(dict2)
print(type(dict2))



dict3 = {
    # [1,2,3] : "one",
    "even" : [2,4,6,8,10],
    "odd" : [3,5,7,9]
}


print(dict3) #unhashable type: 'list
print(type(dict3))

print(dict1[1])
print(dict1[2])
print(dict1[3])


print(dict3["odd"])
print(dict3["even"])


dict2 = {
    "name" : "Poonam",
    "Class" : 5,
    "Pin" : 400075
}


dict2["Pin"] = 400076
print(dict2)

print("*******")

print(dict2.items())
print(type(dict2.items()))



dict2 = {
    "name" : "Poonam",
    "Class" : 5,
    "Pin" : 400075
}


for i in dict2.items():
    print(i)
print("*******")

for i in dict2.items():
    print(i[0])

