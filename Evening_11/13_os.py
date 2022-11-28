# # #################################################
# # #  13.11.2022 04.00PM
# # #################################################
# # #  TOPICS TO BE COVERED
# # # 👉 DIRECTORY HANDLING  IN PYTHON
# # #################################################

# # OS module

import os
# help(os)
# for i in dir(os):
#     print(i)


# # cwd current working directory
print(os.getcwd())

# # getting list of available directories

# for i in os.listdir():
#     print(i)

# # # changing the working directory

os.chdir(r"D:\SQL")
print("-------")
print(os.getcwd())

# for i in os.listdir():
#     print(i)

# # # creating a folder/dir 

os.mkdir("osdemo3\gk")
# for i in range(6):
#     os.mkdir("Staff{}".format(i))

# # # to create multilevel dir/folders
os.makedirs(r'\osdemo6\abcd\as\sd\sd2')

# # # removing the dir
os.rmdir(r'D:\osdemo6\abcd\as\sd\sd2')

# # # removing parent directories
os.removedirs(r'D:\osdemo6\abcd\as\sd') # not recommended