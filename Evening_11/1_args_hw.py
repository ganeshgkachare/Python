# 1. write a function to take email id from user and 
# separate the name ans domain

# Eg. raghav123@gmail.com
# output should be  [raghav123, gmail.com]
def email_id(arg):
    return arg.split("@")
print(email_id("raghav123@gmail.com"))

# 2. write a function to take 3 integers from user and 
# give average as output
def average(a,b,c):
    avg= (a+b+c)/3
    return avg
print(average(5,10,15))



# 3.  write a function to take student name and
# print "Good luck" with student name
# "Good luck" to be used as default argument
def fn(student_name,wish="Good luck"):
    print(student_name ,wish) 
fn("Ganesh")

# 4. use *args and find average of 5 nos 
# NOTE : dont use 5 directly, instead find
# the leng of the argument.
def avg(*args):
    avg=sum(args)/len(args)
    return avg
print(avg(1,2,3,4,5))


