#1. CREATE A DICT BY USING TWO LISTS WITH zip() FUNCTION
list_keys = ['A', 'E', 'I', 'O', 'U']
list_values = ['0', '1', '2', '3', '4', '5']
dict1 = dict(zip(list_keys,list_values))
print(dict1)
print("-------------------------------------------------")

#2 . CREATE A DICT USING tuples
x = (1 , True)
y = (2 , False)
z = (3 , False)
p = (4 , False)
dict2 = dict([x,y,z,p])
print(dict2)
print("-------------------------------------------------")

#3 . ADD  THE KEY : VALUE PAIR  {5 : True} IN ABOVE DICTIONARY AND PRINT
dict2.update({5 : True}) 
print(dict2)
print("-------------------------------------------------")

#4 . UPDATE THE VALUE OF   KEY 3 IN DICTIONARY AS  True USING .update()
dict2.update({3 : True}) 
print(dict2)
print("-------------------------------------------------")

#5 . RETRIEVE THE VALUE CORRESPONDING TO KEY y IN ABOVE DICT
# USING []
print(dict2[y[0]])
print("-------------------------------------------------")

# USING .get()
print(dict2.get(y[0]))