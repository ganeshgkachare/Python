#################################################
#  17.10.2022 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 TUPLE  IN PYTHON
#################################################

# revision 

'''
1 .DATA TYPES IN PYTHON
> NUMBERS 
    > INT       :1 2 3 4  400
    > FLOAT     :3.14 22.22 0.033
    > COMPLEX  : 1+2J
> BOOLEAN True/False 0/1
>LIST [any type of data ]
>STRINGS '' or " " or ''' '''
> TUPLE ()
'''


#immutable
#hashable 

#            0 1 2 3 4
list_even = [2,4,6,8,10]
print(list_even)

#using indexing 

print(list_even[2])

# start: stop n-1
print(list_even[1:4]) #4,6,8
print(list_even[:]) #4,6,8

# step/jump
#start:end:jump
print(list_even[0::2]) #2 6 10
print(list_even[0::3]) #2 8


# reversal
print(list_even[::-1])


# editing the values inside a list

#            0 1 2 3 4
list_even = [2,4,6,8,10]

list_even[4] = 100
print(list_even)


list_even[0] = 200
print(list_even)


#
#        0 1 2 3 4
t_odd = (1,3,5,7,9)
print(type(t_odd))


print(t_odd)
print(t_odd[4]) #9
print(t_odd[0]) #1


# slicing 
# start:end
print(t_odd[2:]) # 5 7 9


# negative 
# reversal
print(t_odd[::-1])




# # editing the values inside a tuple
#        0 1 2 3 4 5 6 
t_odd = (1,3,5,7,9,9,9)

# t_odd[4] = 90  #9 > 90 does not support item assignment
# print(t_odd)



# methods in a tuple


print(t_odd.count(9))
print(t_odd.count(45))

print(t_odd.index(7)) #enter the elemnt
print(t_odd.index(9)) #1st occurance of the element



#        0 1 2 3 4 5 6 
t_odd = (1,3,5,7,9,9,9)

print(min(t_odd))
print(max(t_odd))
print(sorted(t_odd)) #return you a list

t_buy = (99,55,44,11,22,33,44,55)
print(sorted(t_buy , reverse=True))


t_buy = (99,55,44,11,22,33,44,55, 'R', 'P','S') # not supported bcz diff types of data


# print(sorted(t_buy))


# t_s = ('R', 'P','S') #same type
# print(sorted(t_s))


# membership operator

t_buy = (99,55,44,11,22,33,44,55, 'R', 'P','S')

print("Q" in t_buy)
print("S" in t_buy)
print("T" not in t_buy)



# using loops to print
t_buy = (99,55,44,11,22,33,44,55, 'R', 'P','S')
for i in t_buy:
        print(i)