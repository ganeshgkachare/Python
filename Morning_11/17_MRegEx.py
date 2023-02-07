import re
# program 1
str = "an apple a day keeps doctor away"
e1 = re.findall(r'a[\w]*',str)
print(e1)

# program 2
e2 = re.findall(r'\ba[\w]*\b',str)
print(e2)

#program 3
#\w   ==> [a-z A-Z 0-9]
#\d
str2 = "The meeting will be conducted on 21st and 1st of every month"
e3 = re.findall(r'\d[\w]*',str2)
print(e3)

#program3 
str4 = "one two three four five six seven chinmay 8 9 10"
e4 = re.search(r'\b\w{5}\b',str4)
print(e4.group())

#program4
e5 = re.findall(r'\b\w{5}\b',str4)
print(e5)

#program5
e5 = re.findall(r'\b\w{4,}\b',str4)
print(e5)

#program6
e6 = re.findall(r'\b\w{3,5}\b',str4)
print(e6)

#program7
e7 = re.findall(r'\b\d{1,}\b',str4)
print(e7)

#program8
e7 = re.findall(r'\b\d\b',str4)
print(e7)

#program9

str5 = "chinmay7709192441"  
# \d+
e8 = re.search(r'\d+',str5)
print(e8.group())

e9 = re.search(r'\D+',str5)
print(e9.group())

#program 10
import re 
str6 = "anil ankur akshay anant akash arati abhijit abhay bomkesk a67"
#starting with a
print(re.findall(r'\ba[\w]*\b',str6))
#starting with an
print(re.findall(r'\ban[\w]*\b',str6))
#starting with  an or ak
print(re.findall(r'\ba[nkb][\w]*\b',str6))
#a followed by digit
print(re.findall(r'\ba[0-9][\w]*\b',str6)) 

#Program 11

#'/w' - [a-zA-Z0-9]
#/d [0-9]
#/D not[0-9]
# * 0 or more occurence
# + 1 or more more

strA = 'chinmay7709192441'
strB = re.search(r'\D+',strA)
print(strB)
print(strB.group())

strC = re.search(r'\d+',strA)
print(strC.group())


strD = "anil akhil ankit ankur arati abhijit arundhati bimal bikas"
e11 = re.search(r'\ba[\w]*\b',strD)
print(e11.group())

e12 = re.findall(r'\ba[\w]*\b',strD) # list
print(e12)

e13 = re.findall(r'\ban[\w]*\b',strD) # list
print(e13)

e14 = re.findall(r'\ba[nk][\w]*\b',strD) #an or ak
print(e14)

e15 =re.findall(r'\ba[nbk][\w]*\b',strD)
print(e15)

strE = 'Chinmay 7-11-1989 , Ram 11-7-1990 ,Sarika 17-7-1990'
e16 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',strE)
print(e16)

strF = "Hello world"
e17 = re.search(r'^He',strF)
print(e17.group())
if e17:
    print('Sentence starts with He')
else:
    print('Sentence does not starts with He')


# ^
# $

e18 = re.search(r'ld$',strF)
print(e18.group())
if e18:
    print('Sentence ends with ld')
else:
    print('Sentence does not ends with ld')


e19 = "chinmay got 56 marks and rahul got 90 marks"
#[56,90]

e20 = "The meeting will start at 9am and will end at 8pm . please join at 8am"
#[9am 8am 9pm]


#try handling 

#module

#7:30 pm -- 20