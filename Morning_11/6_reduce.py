
# #         0     1    2   3
from functools import reduce
import operator


listA = [1989,1990,1991,1992]
listB =[] #[33,32,31,30]
for item in listA:
    #print(2022-item)
    listB.append(2022-item)
print(listB)
# map
q2 = list(map(lambda x:2022-x,listA))
print(q2)


# program2
listC = [1,2,3,4,5,6,7,8,9,10]
#[3,6,9,12,15,18,21,24,27,30]
#map(fn,list)
q3 = list(map(lambda x:x*3,listC))
print(q3)

# program3
listD = [11,22,33]
#[21,32,43]
q4 = list(map(lambda x:x+10,listD))
print(q4)


# filter 
listE = [22,33,44,55,22,33,44,55,66]
listF = []
#[55,55,66]

for item in listE:
    if item > 50:
        listF.append(item)
print(listF)

# program 4
q5 = list(filter(lambda x:x > 50,listE))
print(q5)

listG = [33,44,55,22,3,477,88,99]
print(list(filter(lambda x : x%2 == 0,listG)))
print(list(filter(lambda x : x%2 != 0,listG)))

listF = ["chinmay","amol","amit"]
print(list(filter(lambda x : len(x)  == 4,listF)))

# program5
listG = [1,2,5] # 8
sum = 0

for item in listG:
    sum = sum + item
print(sum)
print("--------------------")
# print(reduce(lambda acc,nextval:acc+nextval,listG,5))
print(reduce(lambda x,y:x+y,listG,2))














print("-----------############---------")
print(reduce(operator.add,listG))
################################################################

a=[2,4,5,6,7,8,9]
print(list(map(lambda x : x % 2 ==0 , [2,4,5,6,7,8,9])))
print(list(filter(lambda x : x% 2 ==0 , [2,4,5,6,7,8,9])))











# def add(x,y):
#     return x + y
# print(add(23,4))
# print(add(34,5))

























































# syntx__________reduce(function, iterable[, initializer])




# # python code to demonstrate working of reduce()
# # using operator functions
 
# # importing functools for reduce()
# import functools
 
# # importing operator for operator functions
# import operator
 
# # initializing list
# lis = [1, 3, 5, 6, 2]
 
# # using reduce to compute sum of list
# # using operator functions
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(operator.add, lis))
 
# # using reduce to compute product
# # using operator functions
# print("The product of list elements is : ", end="")
# print(functools.reduce(operator.mul, lis))
 
# # using reduce to concatenate string
# print("The concatenated product is : ", end="")
# print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))