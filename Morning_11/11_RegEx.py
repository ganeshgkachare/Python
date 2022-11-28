# "chinmay-deshpande-7709192441"
#pattern match
#pattern replace
#pattern split
#search
#findAll for particular (regular expression)

#search 
#findAll
#match
#sub()
#split()

import re
str = 'sun mop run man' 
 # m[a-z A-Z 0-9][a-z A-Z 0-9]
 #\w  [a-z A-Z 0-9]
 #\W ![a-z A-Z 0-9]
e = re.search(r'm\w\w',str)
#print(e)
#print(e.group())
if e:
    print('match found')
    print(e.group())
else:
    print('not found')

#program 2
str2 = 'sun mop run man mad' 
e2 = re.findall(r'm\w\w',str2)
#[] list is considered as falsy value in python
print(e2)
if e2:
    print('elements found')
    print(e2)
    for item in e2:
        print(item)
else:
    print('not found')

#program3
#match()
str3 = "qaq sad sun say some mad"
e4 = re.match(r's\w\w',str3)
if e4:
    print('pattern match')
    print(e4.group())
else:
    print('not found')

# search    object  none 
# findall   list     []
# match     object   None

#program 4
#replace
#sub
str4 = 'I am learning javascript'
e5 = re.sub(r'javascript','java',str4)
print(e5)


#program5
#Split()
str5 = 'This ; us the: "Core" Python\'s tutorial'
#str5 = 'ThisustheCorePythontutorial'
# [a-z] [A-Z] [0-9]
e7= re.split(r'\W+',str5)
print(e7)

# search    - object ---- none
# findall   - list   ---- []
# match     - obj    ---- none
# sub       - str    ----- str
# split     - list   ----- list