# 1. catch exception in below code using try... except 
# else print " Code Execution was successful"
try:
    list_z = [1,2,3,"a"]
    print(5/1)
    for i in range(3):
        if type(list_z[i]) == int:
            print("This is int")
        
        else:
            print("This is not int") 
except IndexError as e1:
    print("Error occured is:",e1)
except ZeroDivisionError:
    print("input should not be zero")
else:
    print (" Code Execution was successful")
finally:
    print("Code End")

print("Hi")

# 2. catch exception in below code using try... except
# else print " Code Execution was successful"
# also close the file irrespective of operation on file
# try:
#     f = open(r"one.txt")
#     print(f.read())
# except FileNotFoundError as e2:
#     print(f"Error occured is:",e2)
# else:
#     print (" Code Execution was successful")
# finally:
#     try:
#         f.close()
#         print("File closed")
#     except:
#         print("File not found" )


# # 3. catch exception in below code using try... except

# try:
#     print("Hello World)
# except :
#     print("Error occured is:")

