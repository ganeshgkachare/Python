# 'chinmay-deshpande-7709192441'
# ['chinmay','deshpande','7709192441']
# if you want to match pattern , regular expression

# search
# program
# A Regular Expression (RegEx) is a sequence of 
# characters that defines a search pattern
import re
print("------------search----------------")
# If the search is successful, re.search() returns a 
# match object; if not, it returns None.
# match = re.search(pattern, str)
str = "sun mop run"  # 'm\w\w' // [a-z][A-Z][0-9] // nor special symbol
# re.search(regex,str)
e = re.search(r'm\w\w',str)
print(e)
print(e.group())
print("-------")
#program2
str2 = "i am leanring langauge"
e2 = re.search(r'an\w\w',str2)
print(e2.group())

print("------------findall----------------")
# The re.findall() method returns a list of strings
#  containing all matches.
# If the pattern is not found, re.findall() 
# returns an empty list.
# program3
str3 = "sun mop run man mat" 
e3 = re.findall(r'm\w\w',str3)
print(e3)
for item in e3:
    print(item)

#program4
str4 = "sun sand surface sub"
e4 = re.findall(r'su\w',str4)
print(e4)
for item in e4:
    print(item)

print("------------match----------------")

#program5
str5 = "sun sand surface sub"
e6 = re.match(r's\w\w',str5)

if e6:
    print('occurence found')
    print(e6.group())
else:
    print('no occurence')

print("------------sub----------------")
# The syntax of re.sub() is: re.sub(pattern, replace, string)
# The method returns a string where matched occurrences are 
# replaced with the content of replace variable.
#program6
str6 = "I am learning javascript"
e7 = re.sub(r'javascript','java',str6)
print(e7)

#split()