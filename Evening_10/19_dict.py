#################################################
#  19.10.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 DICTIONARY  IN PYTHON
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#################################################


# # list_student = ['Akash','Nikita' ,'Monali']
# # list_marks = [58,78,98]
# # print(list_student[0])
# # print(list_student[1])
# # print(list_student[2])

# # print(list_marks[0])
# # print(list_marks[1])
# # print(list_marks[2])

# # Dictionary
# # key : Value

# # key -  UNIQUE and unhashable
# # Values - anything


# from this import d


dict_student = {
    'name' : 'Akash',
    'marks' :  58,
    'rank' : '4th',
    'one' : [1,2,4,5,6,78],
    'two': (7,77,77,777),
    # [1,11] : (5,5) # unhashable type: 'list
    (5,55,555) : 'Minskole'
    }

# # print(dict_student)


# # METHODS

# # ACCESSING/ RETRIEVING
# # EDIT
# # COPY/DELETE

# print(dict_student['marks'])

# # get
# print(dict_student.get('marks'))
print(dict_student.get('two')[3]) # HW  to access 777
print(dict_student['two'][3]) # HW  to access 777

# # item()
#                             #    0                     1        
# print(dict_student.items()) # [(key1 :value1),(key2 :value2)]
# # keys

# print(dict_student.keys())
# # values

# print(dict_student.values())

# print("***********")
# for i,j in dict_student.items(): #unpacking of tuples
#     # print(i,j)
#     print(i)
#     print(j)

# print("***********")

# dict_student_backup = dict_student.copy()
# print(dict_student_backup)


# print("***********")
# dict_student.update({'Place' : 'Pune'})
# print(dict_student)


# #removing objects

# dict_student.pop('rank')
# print(dict_student)


# dict_student.popitem() # remove the latest entry
# print(dict_student)


# dict_student.clear()
# print(dict_student)


# del(dict_student)
# # print(dict_student)
# print(dict_student_backup)




# dict_student = {
#     'name' : 'Akash',
#     'marks' :  58,
#     'rank' : '4th',
#     "nSem" : 90
# }

# dict_student.update({"nSem" : 99})

# print(dict_student)


a = dict(one = 1 , two = 2, three= 3)

print(a)

c = dict([('one' , 1 ), ("two" , 2),("three " , 3)])
print(c)

