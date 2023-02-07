
t = (False,False,True,False,True)

# #1. CONVERT THE ABOVE  TUPLE INTO A LIST
t_l=list(t)
# print(t_l)
# print(type(t_l))
# print("----------------------------------------")

# #2. FIND THE MEMORY ADDRESS OF BOTH TUPLE AND LIST
print(id(t))
print(id(t_l))
# print("----------------------------------------")

# #3. APPEND 99 AT THE END OF THE LIST
b=t_l.append(99)
print("----------jjjjjjjjjjjjj------------------------------")
print(t_l)
print(b)
print("----------------------------------------")

# #4. CONVERT BACK THE LIST  INTO TUPLE
# t=tuple(t_l)
# print(t)
# print(type(t))
# print("----------------------------------------")

# #5. NOW FIND THE MEMORY ADDRESS OF THIS TUPLE
# print(id(t))
# print("----------------------------------------")