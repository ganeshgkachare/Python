# conditionals 

# operators 

# 1)comparison  operator
# 2)logical operator

# < , > , == , !=  <= , >=
# entity < entity  ==================> boolean
# <  ==> less than
# >  ==> greate than
# <=  ==> less than or equal to
# >=  ==> greater then or equal to
# ==  ==> equal tham
# !=  ==> not equal

a = 10
b = 20
print(a < b)
print(11 < 10)  # False
print(33 > 12)  # True
print(11 <= 11) # True
print(12 >= 11) # True
print(12 >= 12) # True
print(33 == 4)  # False
print(22 != 4)  # True
print(11 == 23) # False

# or and  not

# and
# True  and  True  ==> True
# False and  True  ==> False
# True  and  False ==> False
# False and  False ==> False

#or

# True  or  True  ==> True
# False or  True  ==> True
# True  or  False ==> True
# False or  False ==> False

# not 

#True ==> False
#False ==> True 

# True  and  True  ==> True
# False and  True  ==> False
# True  and  False ==> False
# False and  False ==> False

print(12 < 13 and 7 == 7)   # True
print(12 >= 13 and 7 != 6)  # False
print(12 == 11 and 7 == 8)  # False
print(12 > 11 and 7 == 8)   #False



print(12 < 13 or 7 == 7)    # True
print(12 >= 13 or 7 != 6)   # True
print(12 == 11 or 7 == 8)   # False
print(12 > 11 or 7 == 8)    # True

print(not True)
print(not False)
print(not 8==8)


# conditional statement 
# single input =====>    multiple statement
#numberOfT > 0 and  numberOfT <= 5  ===> 5%
#numberOfT > 5 and  numberOfT <= 10 ===> 10%
#numberOfT > 10                     ===> 30%

# if(condition):
#     # statement 1
# else:
#     # statement 2


numberOfT = 11
# if(numberOfT  > 0 and numberOfT <= 5):
#     print(" 5 % discount ")

# if(numberOfT  > 5 and numberOfT <= 10):
#     print('10 % disocunt')

# if(numberOfT  > 10):
#     print('30 % disocunt')


# if(numberOfT  > 0 and numberOfT <= 5):
#     print(" 5 % discount ")

# elif(numberOfT  > 5 and numberOfT <= 10):
#     print('10 % disocunt')

# elif(numberOfT  > 10):
#     print('30 % disocunt')


marksA = 67
# if(marksA > 90):
#     print('Grade A')
# if(marksA > 75):
#     print('Grade B')
# if(marksA > 65):
#     print('Grade C')

if(marksA > 90):
    print('Grade A')
elif(marksA > 75):
    print('Grade B')
elif(marksA > 65):
    print('Grade C')


# not operator with list 
# input


marksA = int(input("Enter your marks"))
if(marksA >= 90):
    print('Grade A')
elif(marksA >=75):
    print('Grade B')
elif(marksA >=65):
    print('Grade C')
elif(marksA >=40):
    print('Grade D')
else:
    print("Fail")

if(marksA >= 90):
    print('Grade A')
if(marksA >=75 and marksA<90):
    print('Grade B')
if(marksA >=65 and marksA<75):
    print('Grade C')
if(marksA >=40 and marksA<65):
    print('Grade D')
if (marksA<40):
    print("Fail")