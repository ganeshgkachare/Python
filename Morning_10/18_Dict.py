names = ["chinmay","sarika"]
marks = (11,22)

# why dict??

thisDict  = {}
print(type(thisDict))

# Defining the dict with values
    # dict does not stores the value by index

person = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "canDrive":True
}

#person[2] this will not work
# retrive 1
fn = person['firstName']
ag = person['age']
print(fn)
print(ag)

# retrive 2
fn2 = person.get('firstName')
fn3 = person.get('firstNamem')
print(fn2)
print(fn3)

# update
person['age'] = 40
print(person['age'])

# add
person['city'] = "pune"
print(person)

#delete
del person['age']
print(person)


vehicle = {
    'color':'red',
    'type':"sedane"
}

# retrive
print(vehicle['color'])
#update 
vehicle['color'] = "black"
#add
vehicle['model'] = "q7"
# delete
del vehicle['color']
print(vehicle)

# duplicate key in dictionary
animal = {
    'legs':2,
    'color':'red',
    'eyes':2,
    'legs':4
}
print(animal)

# dict with in operator
print("legs" in animal)
print("leg" not in animal)

animal = {
    #property - values
    #key  -     values
    'legs':2,
    'color':'red',
    'eyes':2,
    'legs':4
}

for key in animal:
    print(key,animal[key])


flower = {
    'name':"lotus",
    "color":"white",
    "region":"kashmir",
    "lifeShell":4
}

for prop in flower:
    print(prop,flower[prop])


# keys()
print(flower.keys())
# values()
print(flower.values())
# items()
print(flower.items())

# keys()
for x in animal.keys():
    print(x)
# values
for x in animal.values():
    print(x)
#items()
for x , y in animal.items():
    print(x,y)

j = {
    'studentOne':45,
    'studentTwo':90
}
k = j 
k['studentOne'] = 100
print(k)
print(j)

l = j.copy()
print(l)
print(j)
l['studentTwo'] = 70
print(l)
print(j)


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
print("--------------")
kk=sorted(j)
print(kk)
print(type(kk))

# names = ['poorva','ram','sham']
# names2 = names
# names2[0] = "abhisha"

# print(names)
# print(names2)

# a = names.copy()
# print(a)
# print(names)
# a[0] = "aviraj"
# print(a)
# print(names)