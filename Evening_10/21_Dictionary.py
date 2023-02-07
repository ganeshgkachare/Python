# #################################################
# #  21.10.2022 9.00AM
# #################################################
# #  TOPICS TO BE COVERED
# # 👉 DICTIONARY  IN PYTHON
# #################################################


# '''
# 1 .DATA TYPES IN PYTHON
# > NUMBERS
#     > INT
#     > FLOAT
#     > COMPLEX
# > BOOLEAN
# >STRINGS
# > LIST
# > TUPLE
# > SETS {}
# '''

# #  why dictionary ??
# # user defined defined 
# # faster search , faster code 
# # logical mapping 
# # INDEX =  0 1 2 3 4 5 6 7
# # KEYS  = a , b ,c ,d ,e ,f 
# # zillion, zebra , zero




# dict_student = {
#     'name' : 'Viplov',
#     'roll no.' : 54,
#     'Addr' : 'Jalpigudi',
#     'Hobby' :  'cricket',
#     # [101,55,21,9] : 'Scores' unhashable type: 'list'
#     # '(101,55,21,9)' : 'Score' ok... but not to be used
#     'Score' :[101,55,21,9],
#     1 : 'ONE'
# }


# print(dict_student['Addr'])

# #           0    1   2 
# list_num = ['a','b','c']
# print(list_num[2])


# dict_num ={
#         "NAME" : 'Alok',
#         "ADDR" : 'bangalore',
#         "GRADE" : 'c - grade'

# }

# print(dict_num['GRADE'])

# # rainfall in telangala 

# # creating dictionary using tuples

a = ("nirmal" , 33.33)
b = ("Nizamabad" , 55.25)
c = ("Jaynagar" , 101)

rain_data = dict([a,b,c])

print(rain_data)


# print(rain_data['Nizamabad'])


# using zip functio
print("***********")

# list_dist = ['nirmal','Nizamabad','Jaynagar']
# list_rain = [ 33.33 ,55.25, 101]

# rain_data_l = dict(zip(list_dist,list_rain))
# print(rain_data_l)

# rain_data_k = dict(zip(['nirmal','Nizamabad','Jaynagar'], [ 33.33 ,55.25, 101]))
# print(rain_data_k)


# list_dist = ('nirmal','Nizamabad','Jaynagar')
# list_rain = ( 33.33 ,55.25, 101)

# rain_data_l = dict(zip(list_dist,list_rain))
# print(rain_data_l)

# rain_data_k = dict(zip(('nirmal','Nizamabad','Jaynagar'), ( 33.33 ,55.25, 101)))
# print(rain_data_k)

# # checking memory location of dict

# print(id(rain_data))
# print(id(rain_data_l))
# print(id(rain_data_k))

# print(rain_data ==rain_data_l == rain_data_k)



# methods


# print(rain_data.get('Nizamabad'))
# print(rain_data['Nizamabad'])


# # print(rain_data['Hybd']) #KeyError does not exit

# print(rain_data.get('Hybd')) #None
# print(rain_data.get('Hybd','value does not exit for this Place')) #None
# print(rain_data.get('Nizamabad','value does not exit for this Place'))
# print(rain_data.get('Pune','NOt in Telangana'))


# # update
# rain_data['Nizamabad'] = 65.25
# print(rain_data)

# rain_data.update({'Nizamabad':75.25})
# print(rain_data)


# # rain_data['Adilabad'] = 88.23
# # print(rain_data)


# rain_data.update({'Adilabad':99.23})
# print(rain_data)


# setdefault

dict_student = {
    'name' : 'Viplov',
    'roll no.' : 54,
    'Addr' : 'Jalpigudi',
    'Hobby' :  'cricket',
    # [101,55,21,9] : 'Scores' unhashable type: 'list'
    # '(101,55,21,9)' : 'Score' ok... but not to be used
    'Score' :[101,55,21,9],
    1 : 'ONE'
}


dict_student.setdefault('pref')
print(dict_student)


score_team = {
    'Team B' : 0,
    'Team C' : 0,
    'Team D' : 0
}

score_team.setdefault("Team A" ,5)
print(score_team)

score_team.setdefault("Team E" ,0)
print(score_team)

# is dictionary ordered or unorderd ??? Python 3.6/7 is an ordered one






# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x = zip(a, b)

# #use the tuple() function to display a readable version of the result:
# print("--------------------------------")
# print(x)  #Not read
# print("--------------------------------")
# print(tuple(x))



















# using zip functio
print("***********")

list_dist = ['nirmal','Nizamabad','Jaynagar']
list_rain = [ 33.33 ,55.25, 101]

rain_data_l = dict(zip(list_dist,list_rain))
print(rain_data_l)

print("---------------------------")
b = zip(list_dist,list_rain)
print(b)

print("--------constructor-------------------")
print(dict(b))







#update

score_team = {
    'Team B' : 0,
    'Team C' : 0,
    'Team D' : 0
}
score_team["TeamE","TeamD"] = 5,8
print(score_team)
print("---------------------------")
score_team.update({"Team5":8,"Team6":9})
print(score_team)
print("---------------------------")
# score_team["TeamG"]["TeamH"] = 5
# print(score_team)






