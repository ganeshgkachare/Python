import re 
# [a-z A-Z 0-9]
str = 'an apple a day keeps doctor away'
e  = re.findall(r'a[\w]*',str)
print(e)

e2 = re.findall(r'\ba[\w]*\b',str)
print(e2)

#program2
str2 = 'The meeting will be conducted on 1st and 21st of every month'
e3 = re.findall(r'\d[\w]*',str2)
print(e3)

#program3
str2 = "one two three four five six seven 8 9 10"
e4 = re.search(r'\b\w{5}\b',str2)
print(e4.group())

e5 = re.findall(r'\b\w{5}\b',str2) #[a-zA-z0-9]
print(e5)

#program4 (four or more)
e6 = re.findall(r'\b\w{4,}\b',str2)
print(e6)

#program5(minimum3 and maximum5)

e6 = re.findall(r'\b\w{3,5}\b',str2)
print(e6)

#str2 = "one two three four five six seven 8 9 10"
e7 = re.findall(r'\b\d{1,}\b',str2)
print(e7)