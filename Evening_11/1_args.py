#################################################
#  01.11.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 FUNCTION  IN PYTHON
#  https://docs.python.org/3.10/library/functions.html
#  https://peps.python.org/pep-0257/
#################################################
# Functions

# name = "Rahul"
# x = 2000
# Biling  = "Hourly"

x = "Nitin"
for i in x:
    print(i) 



def fun_int(int1):
    print(int1)
fun_int(100)



def fun_str(some_string):
    ans  = some_string.lower()
    for i in ans:
        print(i)
    print(ans)

fun_str("nagpur")
fun_str("mahabaleshwar")
fun_str("MUMBAI")

# s =  "name"
# s.capitalize
# s.lower

def fun_list(list1):
    s = []
    
    for i in list1:
        if type(i) == int:
            s.append(2*i)
    
    print(s)

fun_list([1,2,3,"A","S","D"])


fun_list(["p","q","r"])



print("*****")


#positional arguments

def div_num(num,den):
    print(num/den)

div_num(100,500)
div_num(300,500)
div_num(500,500)
# div_num(500,100,300)

div_num(den=500,num=100)

def greet_cust(name,greet):
    print(name, "!!!" , greet)

greet_cust("Welcome" ,"Santosh")
greet_cust(greet="Welcome" ,name= "Santosh")

# default parameter/argument

def greet_cust(name="Customer",greet="Good Day"):
    print(name, "!!!" , greet)


greet_cust()
print("-------------------")
greet_cust("a")


# args

def sum_num(*numbers):
    print(type(numbers)) #<class 'tuple'>
    print(sum(numbers))

sum_num(100,200,300,400,1000)

def list_num2(*list1):
    s = []
    for i in list1:
        s.append(3*i)
    print(s)

l1 = [10,20,30]
l2 = [20,40,60]


list_num2(*l1,*l2)
list_num2([10,20,30],[20,40,60])



def sum_num(*args):
    print(type(args)) #<class 'tuple'>
    print(sum(args))

sum_num(100,200,300,400,1000)

def list_num2(*args):
    s = []
    for i in args:
        s.append(3*i)
    print(s)

l1 = [10,20,30]
l2 = [20,40,60]


list_num2(*l1,*l2)
list_num2([10,20,30],[20,40,60])