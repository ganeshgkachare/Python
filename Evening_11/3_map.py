#################################################
#  03.11.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 FUNCTION  IN PYTHON
#  https://docs.python.org/3.10/library/functions.html
#  https://peps.python.org/pep-0257/
#################################################
# LAMBDA FUNCTION
#nameless
# anonymous
# ONE LINER FUNCTION

from functools import reduce


x = 100
y = 200
def sum_num(a,b):
    return a+b

print(sum_num(x,y))


# lambda x,y,z : expression
z = lambda a,b : a+b

print(z(100,200))
print((lambda a,b: a+b)(300,300))

def square_num(num):
    return num*num

print(square_num(5))

ans  = lambda num : num*num
print(ans(25))



print("*******")


# map
list_score = [42,71,41,12,8,99]

def double_score(x):
    # for i in x:
    return (2*x)

double_score(100)

# map (fun ,ite)
print(list(map(lambda a,b : a+b,[1,2],[2,3])))

print(map(double_score,list_score))
print(type(map(double_score,list_score)))
print(list(map(double_score,list_score)))
print(list(map(lambda x :2*x,list_score)))
print("------------------------------------------------------")


# filter
# filter (fn,iterable object)
def even_num(s):
    if s%2 !=0:
        return s


print(list(filter(even_num,list_score)))

# reduce
def all_sum(x):
    s = 0 
    for i in x:
        s = s + i
    return s

print(all_sum([1,2,3,4,5]))

print(reduce(lambda x ,y: x+y ,[1,2,3,4,5]))

print(reduce(lambda x ,y: x*y ,[1,2,3,4,5]))



#######################################################################
# map (fun ,ite)
numbers = (1, 2, 3, 4)
result = list(map(lambda x: x + x, numbers))
print(result)

# # a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
  
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

f= map(lambda x :  x % 2 == 0,seq)
print(list(f))

f= filter(lambda x :  x % 2 == 0,seq)
print(list(f))
