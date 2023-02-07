

# Download
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
#  N = int(input())
#     List=[]
#     for i in range(N):
#         a=input().split()
#         if a[0] == "insert":
#             List.insert(int(a[1]),int(a[2]))
#         elif a[0] == "append":
#             List.append(int(a[1]))
#         elif a[0] == "pop":
#             List.pop()
#         elif a[0] == "print":
#             print(List)
#         elif a[0] == "remove":
#             List.remove(int(a[1]))
#         elif a[0] == "sort":
#             List.sort()
#         else:
#             List.reverse()




# for i in range(len(s)):
#     if s[i].isalpha() == True:
#         print(True)
#         break
#     elif s[i].isalpha() == False:
#         pass
#     else:
#         print(False)
        
# for i in range(len(s)):
#     if s[i].isdigit() == True:
#         print(True)
#         break
#     elif s[i].isdigit() == False:
#         pass
#     else:
#         print(False)
        
# for i in range(len(s)):
#     if s[i].islower() == True:
#         print(True)
#         break
#     elif s[i].islower() == False:
#         pass
#     else:
#         print(False)
            
            
# for i in range(len(s)):
#     if s[i].isupper() == True:
#         print(True)
#         break
#     elif s[i].isupper() == False:
#         print("Upper case is missing")
#     #else:
#      #   print(False)
            
# s = "aBs457"      
# List_U=[]
# for i in range(len(s)):
#     if s[i].isupper() == True:
#         List_U.append(True)
#         #print(List_U)
#     else:
#         List_U.append(False)
#         #print(List_U)
# a=any(List_U)
# if a == True:
#     print(True)
# else:
#     print(False)

#########################################

## pass continue break

# s = "abs457B436"
# for i in range(len(s)):
#     if s[i].isupper() == True:
#         print(True)
#         #break
#     elif s[i].isupper() == False:
#         print(i)
#         pass
#     else:
#         print(False)
# print("stop")

# print("--------------------------------")
# for i in range(len(s)):
#     if s[i].isupper() == True:
#         print(True)
#         #break
#     elif s[i].isupper() == False:
#         print(i)
#         continue
#     else:
#         print(False)        
# print("stop")

################################################

# a=(1)
# print(type(a))
# print("----------------------")

# a=(1,2)
# print(type(a))
# print("----------------------")

# b= 2,3
# print(type(b))
# print(b)
# #?????
# print("----------------------")

# print(bool(0))
# print(bool(1))
# print(bool(2))
# print(bool(4))
# print(int(True))
# print(int(False))
# print("------------------S----")

# print(bool(""))
# print(bool(" "))
# print(bool("tytdj"))
# print(bool("f"))
# print(bool("False"))
# print(bool("True"))
# print("----------------------")

# c = [0,1,2,3,4]
# d = bool(c)
# print(d)
# print("-----###############-----------")

# s=[0,0,0,0]
# ss= bool(s)
# print(ss)
# print("----------------------")

# bool convert only argument

# a="abcd"
# a[2]=k
# print(a)


print(sum((2,3)))
print(sum([2,3,5]))
print(sum((2,3,5)))
print(sum({2,3,5}))
a={2,3,5}
for i in a:
    print(i)