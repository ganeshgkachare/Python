#################################################
#  09.11.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 FILE HANDLING  IN PYTHON
#################################################

# file handling
# file  vs folder 
# handling 


# FILE CREATION
# FILE OPEN
# FILE READ
# FILE WRITE 
# FILE CLOSE

# reading an existing file in python


data = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow1.txt")
print(data.read())
data.close()

#reading non existing file
# data = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt")
# print(data.read()) #FileNotFoundError:

# creating a file 

# mode of operation
'''

Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
'''

f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "w")
f.write("Wow2 data in the file")
f.close()


f1 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "r")
print(f1.read())
print(f1.mode)
f1.close()


# over writing data 
f2 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "w")
f2.write('''
Data1 
Data2
Data3
''')


f2.close()


f2 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "a")
f2.write("\nData4, \nData5")
f2.close()


# 
f2 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "r")
print(f2.read(15))
f2.close()

# printing line 
print("*******")
f2 = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "r")

print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.readline())

# resetting cursor position
f2.seek(0)
print("*******")

print(f2.readline())
print(f2.readline())


print("***using for loop****")

f2.seek(0)
for i in f2:
    print(i)


f2.seek(0)
print("***using readlines****")
# print(f2.readlines())
print(f2.readlines()[1])

f2.close()


# content manager

print("**# content manager readlines*****")

with open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\wow2.txt", "r") as f5:
    print(f5.read(5))
    print(f5.mode)




# print(f5.read()) # this will give error