# continue and break


for x in range(10):
    print(x)
    if(x == 3):
        break

for x in range(5): # 0 ,1 ,2,3,4
    if(x == 2):
        continue
    print(x)  # 0 1 3 4

for x in range(12):
    pass

#--------------------------------------------------------------------------------

# tuple
#          0          1       2     3
names = ["chinmay","poorva","ram","suman"]
for x in names:
    print(x)

names = ["ram","sita","ram","sham",10]
for x in names:
    print(x)

names[1] = "sam"
print(names)


# tuple

q = (11,22,33,44)
#q[2]= 33
print(q)
# append() , extend() ,insert(),remove(),pop(),clear()


q2 = ("chinmay","deshpande",24,56)
print(q2)
print(q2[0])

# slicing
#       0        1        2          3        4        5
q3 = ("pune","banglore","kolkata","raipur","nagpur","wardha")
#     -6       -5           -4        -3       -2       -1

print(q3[1])
print(q3[1:5])
print(q3[-6:5])
print(q3[1:4])
print(q3[::-1])
x = 10,
print(x)

y = ()
print(type(y))

# function to process the tuple
country = ("india","pakistan","srilanka","bangladesh","cuba")
q5 = len(country)
print(q5)

#min()
numbers =(33,44,55,66,7,55,66)
print(min(numbers))

#max()
print(max(numbers))

#count()
print(numbers.count(66))

#index()
#         0   1  2  3 4 5  6
numbers =(33,44,55,66,7,55)
q3 = numbers.index(44)
print(q3)

#sorted
numbers = (55,55,66,77,33,44,55,66)
y = sorted(numbers)
print(numbers)
print(tuple(y))


print("chinmay" not in ["chinmay","sarika","poorva","ram"])
print("chinmay" in ["chinmay","sarika","poorva","ram"])

numbers2 = (11,22,33,4)
if(22 in numbers2):
    print("availble")
else:
    print("not available")

#loop

animals = ("tiger","lion","rabbit")
for animal in animals:
    print(animal)

for i in range(len(animals)):
    #print(i)
    print(animals[i])
