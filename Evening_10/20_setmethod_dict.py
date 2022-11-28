#################################################
#  20.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 SET  IN PYTHON
# 👉 DICTIONARY  IN PYTHON
#################################################

# SET OPERATIONS mathematical


e = {0,2,4,6,8,10}

o = {0,1,3,5,7,9}

o1 ={3,5}
n1 = {'a','b'}

print("--------------intersection---------------")
print(e.intersection(o))
print(e&o)
print("--------------union---------------")
print(e.union(o))
print(e|o)
print("--------------diff---------------")
print(e.difference(o))
print(e-o)
print("--------------sy.diff---------------")
print(e.symmetric_difference(o))
print(e^o)
print("-------------subst----------------")
print(o1.issubset(o))

# print(e.union(o))
# print(e.intersection(o))
# print(o.intersection(e))

# print(e.difference(o))
# print(o.difference(e))

# print(e.symmetric_difference(o))
# print(o.symmetric_difference(e))

# # boolean

# print(o1.issubset(o))
# print(n1.issubset(e))

# DICTIONARY  IN PYTHON
# word : meaning, syn, details, eg:
# discipline unique


# word : meaning
# key : value
# uinque* : anything

z  = {'name' : 'Prakash'}
print(type(z)) #<class 'dict'>

z  = {'name' : 'Prakash',
    'roll no.' : 58 , 
    'Addr' : 'Nagpur'}

print(z)

# list
# tuple

#indexing is in form of numbers  !!!
# keys are like index


# accessing  the data in a dict :

dict1 = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}

print(dict1)

# discipline : good
# wrong  : good


# print(dict1['name'])
# print(dict1['Score'])
# print(dict1['roll no.'])
# print(dict1[1])

# print(dict1.keys())
# print(type(dict1.keys()))


# print(dict1.values())



# print(dict1.items())
# print("*****items*****")
# for i,j in dict1.items():
#     print(i,j)

# print("*****keys*****")
# for i in dict1.keys():
#     print(i)
# print("*****values*****")
# for i in dict1.values():
#     print(i)


# methods


dict1 = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}


dict1.update({2 : 'TWO',})
print(dict1)

# deleting object

dict1.pop('Addr')
print(dict1)