#################################################
#  22.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 DICTIONARY  IN PYTHON
#################################################

'''
1 .DATA TYPES IN PYTHON
> NUMBERS
    > INT
    > FLOAT
    > COMPLEX
> BOOLEAN
>STRINGS
> LIST
> TUPLE
> SETS {}
> dictionary {}
'''


# HOW TO CREATE A DICTIONARY
a_var = dict(name = "rahul", age = 32 ,job = 'teacher')

d_tup = dict([('name',"Akash"),('age',35),('job',"Instructor")])

b_basic = {'name': 'Nikhita' , 'age': 26 , 'job' : 'SOftwareTeste'}




list_keys = [1,2,3,4,5,6]
list_values= ["one","two","three","four","five","six"]

c_zip = dict(zip(list_keys ,list_values))


# x_basic = dict('name': 'Nikhita' , 'age': 26 , 'job' : 'SOftwareTeste')

print(a_var)
print(d_tup)
print(b_basic)
# print(x_basic)
print(c_zip)


z = {}
print(type(z))






