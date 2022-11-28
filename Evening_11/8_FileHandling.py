# #################################################
# #  08.11.2022 9.00AM
# #################################################
# #  TOPICS TO BE COVERED
# # 👉 FILE HANDLING  IN PYTHON
# #################################################
# '''

# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================
# '''



# # FILE HANDLING 


# # we generally do below operations while creating a text file in windows
# # FILE CREATED
# # FILE OPENED
# # FILE WRITE
# # FILE READ
# # FILE EDIT
# # FILE CLOSE


# # Below codes WILL NOT WORK for ONLINE compilers !!!...


# # use "r" i.e raw string before path to avoid UNICODE error
# # f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\L40.py","w")
# # f.write('''Line2
# # Line3
# # Line4''')



# # help(open) # details of open method using help() function


# # reading  a file
# # f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\L41.py") # reading is by default if no 2nd argument is given in open()
# # f.read() #No such file or directory:


# # writing  in a file 
# # f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\L41.py","w")
# # f.write("One") #No such file or directory:


# # data1 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\L42.py","w")
# # data1.write("This is class for File handling")


# # help(pow)
# # help(print)

# f=open("E:\Ganesh\Coding\python\Rahul_Sir_11\FileDemo.py","w")
# f.write("Practice \n File Handling")
# f=open("E:\Ganesh\Coding\python\Rahul_Sir_11\FileDemo.py")
# print(f.read())

fname = ["File1","File2","File3","File4","File5"]
for name in fname:
          f=open(fr"E:\Ganesh\Coding\python\Rahul_Sir_11\file{name}.py","w")
          f.write(f"Practice \n File Handling \n File name {name}")
          print("-----------------------------------------")

for name in fname:
          f=open(fr"E:\Ganesh\Coding\python\Rahul_Sir_11\file{name}.py")
          print(f.read())
          print("-----------------------------------------")




a = r"Ganesh\nKachare"
print(a)
print(len(a))
b = r"Ganesh\tKachare"
print(b)
print(len(b))

# # FILE OPENED
# f =open("E:\Ganesh\Coding\python\Chinmay_Sir_11\gk.py","w")
# f.write("Sample file")
# f =open("E:\Ganesh\Coding\python\Chinmay_Sir_11\gk.py","r")
# print(f.read())