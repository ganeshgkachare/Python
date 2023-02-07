#################################################
#  30.10.2022 9.00 AM
#################################################
#  TOPICS TO BE COVERED
#  👉 DICTIONARY  IN PYTHON
#  https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#################################################

# METHODS IN DICT

dict_student = {
    "Name" : "Vivek",
    "Class" :  "FYJC",
    "PIN" : 442404,
    "Sub" : ['P' ,"C" , "M" ,"IT"]
}


# setdefault  >  get + update 

print(dict_student.setdefault("PIN"))
print(dict_student.setdefault("Sub"))
print(dict_student.setdefault("Attend" , "Y"))
print(dict_student.setdefault("Attend1")) # make None as value for the given Key

print(dict_student)


# fromkeys

dist = ['dist1', 'dist2' ,'dist3','dist4','dist5']


# monsoon  = {
#     'dist1'	: 0,
#     'dist2'	: 0,
#     'dist3'	: 0,
#     'dist4'	: 0,
#     'dist5'	: 0,
# }

# monsoon = dict.fromkeys([KEYS] , "Default Values")

monsoon =  dict.fromkeys(dist , "data  pending")
print(monsoon)

print("******")
monsoon2 = dict.fromkeys(dist)
print(monsoon2)


print("******")
monsoon3 = dict.fromkeys(dist , [10,25,30])
print(monsoon3)



# print("******")
# monsoon4 = dict.fromkeys(dist , "Default Values1","Default Values2" )
# print(monsoon4)



# clear
print("******")
print(monsoon3)
monsoon3.clear()
print(monsoon3)


# pop 
print(monsoon2)
monsoon2.pop('dist3') # delete the key value pair
print(monsoon2)


# popitem

print(monsoon2)
monsoon2.popitem() # delete the latest  entry not the last 
print(monsoon2)



print(monsoon2)
monsoon2.popitem() # delete the latest  entry not the last 
print(monsoon2)


monsoon2.update({'dist1'	: 100,'dist11'	: 100,'dist111'	: 100,})
print(monsoon2)


print(monsoon2)
monsoon2.popitem() # delete the latest  entry not the last 
print(monsoon2)

# del
# print(monsoon2)
# del().monsoon2
# print(monsoon2)

print("******")
print(monsoon2)
del(monsoon2["dist11"])
#del monsoon2
print(monsoon2)