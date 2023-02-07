# # #################################################
# # #  09.11.2022 9.00AM
# # #################################################
# # #  TOPICS TO BE COVERED
# # # 👉 FILE HANDLING  IN PYTHON
# # #################################################


# # # BASICS OF FILE HANDLING 
# # # MODES OF OPERARTION
# # # 

# # # REVISION

# to create an empty txt file
# f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","w")
# f.write("This is demo file \n Hello")
# f.close()
# f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","r")
# print(f.read())
# f.close()
print("------------------------------")
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","a")
f.write("\nGood Morning")
f.close()
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","r")
# print(f.read(3))
# print(f.read(3))
# print(f.read(3))
# f.seek(1)
# print(f.readline())
# print(f.readline())
# print("----------------------")
# f.seek(0)
# print(f.readlines())
print("-----------For Loop-----------")
for i in f:
    print(i)


# # f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py","w")
# # f.write("Line 1")
# # f.write("Line 2")
# # f.write("Line 3")
# # f.write("Line 4 , Line5 , Line6 ")
# # f.write("\nLine 7 , \nLine8 , \nLine9 ")
# # print(f.mode)
# # f.close()
# # print("-----------------appending a file --------------------------------------------------")
# # # appending a file 
# # f2 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py","a")
# # f2.write("\nLine10")
# # f2.close()
# # print("----------------reading data from txt file------------------------------------------")

# # # reading data from txt file


# # f3 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py") # default mode is "r" i.e read mode
# # print(f3.mode)
# # print(f3.read(10))
# # print(f3.read(10))
# # print(f3.read(10))
# # print(f3.read(10))
# # f3.close()
# # print("------------------resetting the cursor position-----------------------------------")

# # # resetting the cursor position

# # f3 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py") # default mode is "r" i.e read mode

# # print(f3.read(10))
# # print(f3.read(10))
# # f3.seek(0) # at the starting of the file
# # f3.seek(20) # at 20th character  of the file
# # print(f3.read(10))
# # f3.close()
# # print("---------------------reading multiple lines----------------------------------------")

# # # reading multiple lines
# # print("*******")
# # f4 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py","r")
# # print(f4.readline())
# # print(f4.readline())
# # print(f4.readline())
# # print(f4.readline())

# # f4.close()
# # print("--------------------using for loop-----------------------------------------------")

# # # using for loop
# # print("***using for loop****")
# # f4 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py","r")
# # for i in f4:
# #     print(i)

# # f4.close()
# # print("--------------------data in the form of list--------------------------------------")

# # # data in the form of list

# print("***using  readlines****")
# f5 = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\FileHandling.py","r")
# print(f5.readlines())
# # print(f5.readlines()[3])
# f5.close()




# # print("--------------------using content manager------------------------------------------")

# # # using content manager 
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","r")
with open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\demo.py","r") as f:
    print(f.read())
    print(f.mode)


print("-------------------------------------------------------------------")

# # # types of file is pyton
# # # text file  = human readable , txt , doc s, csv
# # # binary files = non readable  , img, jpeg, mp3


# # # binary 
# # # txt files are special binary files


