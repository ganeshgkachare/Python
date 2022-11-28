# #################################################
# #  31.10.2022 4.00PM
# #################################################
# #  TOPICS TO BE COVERED
# # 👉 FUNCTION  IN PYTHON
# #  https://docs.python.org/3.10/library/functions.html
# #################################################


# # List as an argument

# print(10/2)
# print(12/2)

# print(10%2)
# print(12%2)
# print(13%2)


# print(13%2 == 0)
# print(13%2 == 0)
# print(20%2 == 0)


# a = 203

# if a%2 == 0:
#     print("Even number :")
# else:
#     print("Odd number :")


# a = [10,22,45,78,77,44,11]
# b = []
# for i in a:
#     if i%2 == 0:
#         b.append(i)
# print(b)


# def even_filter(x):
#     b = []
#     for i in x:
#         if i%2 == 0:
#             b.append(i)
#     print(b)

# even_filter([10,22,45,78,77,44,11])
# even_filter([1,11,111,2,2,22,222])



# list_num = [100,200,300,400]

# def double(z):
#     d = []
#     for i in z:
#         d.append(2*i)
#     return d


# print(double([100,200,300,400]))
# print(double(list_num))



# # *args
# # variable lenght argument 


# list_staff = [1,2,3,4,5,6,7,8,9]

# # def concat(x,y,z,w):
# #     return x+y+z+w

# # # print(concat("A","B","C"))
# # print(concat("A","B","C", "D"))



# def concat_name(a,b):
#     return a+b


# # print(concat_name("Rahul","Chaudhary"))
# # print(concat_name("Vikas","Chaudhary"))
# # print(concat_name("Vikas","Suresh","Chaudhary","One"))



# def concat_name(*args):
#     s = []
#     for i in args:
#         s.append(i.upper())
#     return s

# print(concat_name("Vikas","Suresh","Chaudhary","One", "Two"))


# def func1(x,y):
#     print(x,y)

# func1(12,25)

# Special Symbols Used for passing arguments:-

# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)

# def concat_name(args):     #Exception has occurred: TypeError  
#     s = []                 #concat_name() takes 1 positional argument but 5 were given
#     for i in args:
#         s.append(i.upper())
#     return s
# print(concat_name("Vikas","Suresh","Chaudhary","One", "Two"))    #above error here














def concat_name(*args):
    s = []
    for i in args:
        s.append(i.upper())
    return s

print(concat_name("Vikas","Suresh","Chaudhary","One", "Two"))



def concat_name(*args):    # *args used when we don't know how many arguments will be given (it create tuple)
    s = []
    for i in args:
        s.append(i.upper())
    return s

print(concat_name("Vikas","Suresh","Chaudhary","One", "Two"))

print("-------------------------------------------")
def concat_name(args):    
    s = []
    for i in args:
        s.append(i.upper())
    return s
print(concat_name("Vikas"))

def concat_name(*args):    
    s = []
    for i in args:
        s.append(i.upper())
    return s
print(concat_name("Vikas"))   # i.e we convert string into tuple
print("-------------------------------------------")

a="Vikas","Sagar"
b="Sagar"
print(a,type(a))
print(b,type(b))

s = []
for i in a:
    s.append(i.upper())
print(s) 

s = []
for i in b:
    s.append(i.upper())
print(s)


