
# t = (False,False,True,False,True)

# #1. CONVERT THE ABOVE  TUPLE INTO A LIST
# t_l=list(t)
# print(t_l)
# print(type(t_l))
# print("----------------------------------------")

# #2. FIND THE MEMORY ADDRESS OF BOTH TUPLE AND LIST
# print(id(t))
# print(id(t_l))
# print("----------------------------------------")

# #3. APPEND 99 AT THE END OF THE LIST
# t_l.append(99)
# print("----------------------------------------")

# #4. CONVERT BACK THE LIST  INTO TUPLE
# t=tuple(t_l)
# print(t)
# print(type(t))
# print("----------------------------------------")

# #5. NOW FIND THE MEMORY ADDRESS OF THIS TUPLE
# print(id(t))
# print("----------------------------------------")


s=input("string")
for i in range(len(s)):
    if s[i].isalnum() == True:
        print(True)
        break
    else :
        if s[i].salnum() == False:
            i = i +1
            if i == len(s):
                print(False)


for i in range(len(s)):
    if s[i].isalpha() == True:
        print(True)
        break
    else :
        if s[i].isalpha() == False:
            i = i +1
            if i == len(s):
                print(False)

for i in range(len(s)):
    if s[i].isdigit() == True:
        print(True)
        break
    else :
        if s[i].isdigit() == False:
            i = i +1
            if i == len(s):
                print(False)

for i in range(len(s)):
    if s[i].islower() == True:
        print(True)
        break
    else :
        if s[i].islower() == False:
            i = i +1
            if i == len(s):
                print(False)

for i in range(len(s)):
    if s[i].isupper() == True:
        print(True)
        break
    else :
        if s[i].isupper() == False:
            i = i +1
            if i == len(s):
                print(False)