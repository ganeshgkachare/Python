import email


q = "hello"
print(q)

q1 = 'hello'
print(q1)

#--------------------------------
# String stores the value by index

q3 = "bye"
print(q3[0])


# Loops
q4 = "chinmay"
for char in q4:
  print(char)

for x in range(len(q4)):
  #print(x)
  print(q4[x])

# slicing 
# 0 1 2 3 4 5 6 7 8 9
# c h a n d r a p u r

q5 = 'chandrapur'
q5 = q5[1:5]
print(q5)


# Methods
q6 = "pune"
q7 =len(q6)
print(q7)

# upper()

a1 = 'pune'
b1 = a1.upper()
print(b1)

#lower()
a2 = "Nagpur"
b2 = a2.lower()
print(b2)

#isupper()
a3 = "JAIPUR"
b3 = a3.isupper()
print(b3)

#islower()
a4 = "wardha"
b4 = a4.islower()
print(b4)

#capitalize()

a5 = "raipur"
b5 = a5.capitalize()
print(b5)

# startswith()

a6 = "delhi"
b6 = a6.startswith("de")
print(b6)

#endswith()

a7 = "akola"
b7 = a7.endswith("la")
print(b7)

#index()

a8 = "goa"
b8 = a8.index("o")
print(b8)

#count()

a9 = "abhisha"
b9 = a9.count('a')
print(b9)

#replace()
a10 = "I am learning javascript"
b10 = a10.replace('javascript','python')
print(b10)

# strip

a11 = " amol "
print(len(a11))

b11 = a11.strip()
print(b11)
print(len(b11))

# split()
a12 = "chinmaydeshpande010@gmail.com"
print("chinmaydeshpande010@gmail.com".split('@'))
print("chinmaydeshpande010@gmail.com".split('a'))
print("chinmaydeshpande010@gmail.com".split('d'))


email="ganeshgkachare@gmail.com"
print(email.split("@"))


#["chinmaydeshpande010","gmail.com"] 
#["chinm","ydeshp","nde010@gm","il.com"]
#["chinmay","eshpan","e010@gmail.com"]


a13 = "ninad1"
b13 = a13.isalpha()
print(b13)

a14 = "123a"
b14 = a14.isdigit()
print(b14)

a15 = 'chinmay010'
b15 = a15.isalnum()
print(b15)

a16 = "b "
b16 = a16.isspace()
print(b16)

# returns true if first  character of every method is capital
a17 = "Mother FaTher"
b17 = a17.istitle()
print(b17)