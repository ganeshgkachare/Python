#################################################
#  02.11.2022 4.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 FUNCTION  IN PYTHON
#  https://docs.python.org/3.10/library/functions.html
#  https://peps.python.org/pep-0257/
#################################################


# DOC STRING 

# this is a new line !!!
'''
Line 1
Line 2
Line 3 
'''

def sum_num(a,b):
    '''
    This is a calculator app
    It takint
    O/p is a floates inp as 
    Wont work with complex num
    '''
    print(a+b)
    print(a-b)
    print(a*b)
    print(a%b)




# sum_num(10,20)


# UNDERSCORE _
# DUNDER _var_  DUNDER VAR 
print(sum_num.__doc__) # DUNDER DOC   
print(list.__doc__)


print(len.__doc__)
print(print.__doc__)


# default argumnet

def greet_customer(name, greet= "Welcome"):
    print(greet, name)


greet_customer("Hi!!", "Ravi")


# *args

def students_data(name,age, area):
    print(name,age, area)

def students_data(*args):
    print(type(args))
    print(args)

    
students_data("W", 17, "Pune", 10)


#kwargs
print("----------------------------------------------------")
def school_data(**kwargs):
    print(type(kwargs))
    for key, values in kwargs.items():
        print(key, values)

school_data(name = "wasim",age=17, area="Pune", Subj = ['p', 'c', 'm'])


dict1 = {
    'job' : "SDE",
    'Grade' : "Y",
    'WEX' : 7

}

school_data(**dict1)

