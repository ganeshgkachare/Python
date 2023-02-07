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

str5 = "chin may abcd 7709192441Ganesh"  
# \d+
e8 = re.search(r'\d+',str5)
print(e8.group())

e9 = re.search(r'\D+',str5)
print(e9.group())

e9 = re.findall(r'\D+',str5)
print(e9)
print("-----------------")
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


a="anil ankur akshay anant akash arati abhijit abhay bomkesk a67"
b=re.findall(r'[amGH]',a)
print(b)