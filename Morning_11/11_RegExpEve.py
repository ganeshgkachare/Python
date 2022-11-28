# # string pattern match 
# # first occurence 
# # pattern filter 
# # pattern split
# # pattern replace
# # patter  match

# # program1 

# # \w [a-z][A-Z][0-9]

import re
# str = 'qas man sun mop run'
# e1 = re.search(r'm\w\w',str)
# if e1:
#     print('pattern find')
#     print(e1.group())
# else:
#     print('patter not found')

# # program 2
# str2 = 'qas man sun mop run'
# e2 = re.findall(r'm\w\w',str2)
# #[] falsy value
# if e2:
#     print('pattern found')
#     for item in e2:
#         print(item)
# else:
#     print('pattern not found')

# #program 3
# str3 ='mas man sun mop run'
# e3 = re.match(r'm\w\w',str3)
# if e3:
#     print('match found')
#     print(e3.group())
# else:
#     print('match not found')

# #program 4
# str4 = "i am learning javascript"
# e4 = re.sub(r'javascript','java',str4)
# print(e4)

# # program5
# #\W non alphanumeric not [a-z][A-Z][0-9]
str5 = 'This ; is the "Core" python\'s book'
e5 =re.split(r'\W+',str5)
print(e5)


e5 =re.split(r'\W',str5)
print(e5)

print("--------------------")
# #-----------------------------------------------------
# #\w  ===>  [a-z] [A-Z][0-9]
# #\b     ===> " "
# #\W     ===> not [a-z][A-Z][0-9]
# #\d     ===> [0,9]

str6 = 'an apple a day keeps the doctor away'
e6 = re.findall(r'\ba[\w]*\b',str6)
print(e6)
# e6 = re.findall(r'\ba[\w]*\b',str6)
# print(e6)

# #* 0 or more reptitions  0 > 2
# #+ 1 or more repetation  1, more repetion

# # an 
# # apple
# #away
# #ay
# #a
print("lllllllllllllllllllllllllll")
#program6
str7 = "I belong to 21st century not 19th century"
e7 = re.findall(r'\d[\w]*',str7)
print(e7)
e7 = re.findall(r'\d[\w]+',str7)
print(e7)
e7 = re.findall(r'\d[\w+]',str7)
print(e7)
e7 = re.findall(r'\d[\w*]',str7)
print(e7)



# e8 = re.findall(r'\d',str7)
# print(e8)


# # +
# # *
# # \b at the  beginning and ending


# # \w [a-z][A-Z][0-9]
# # \W not [a-z][A-Z][0-9]
# # \b  " "
# # \d [0-9]

print("lllllllllllllllllllllllllll")
a= "This is python support session"
# b=re.findall(r"[a-r]",a)
# print(b)
b=re.findall(r"\w\wp\w+",a)
print(b)
# b=re.findall(r"/bp[\w]*",a)
# print(b)

