# function returning more than one value 


def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return q1

q2 = calculator(12,1)
print(q2)
################################################
# list , tuple , dictionary , set
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return [q1,q2,q3,q4,q5]

listC = calculator(12,1)
print(listC)

###########################################
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return q1,q2,q3,q4,q5

listD = calculator(12,1)
print(listD)
#####################################################

def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {
        'addition':q1,
        'subtraction':q2,
        'multiplication':q3,
        'division':q4,
        'modulus':q5
        }

listE = calculator(12,1)
print(listE)



def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {q1,q2,q3,q4,q5}

listE = calculator(5,5)
print(listE)


# int 
# float 
# boolean 
# string 
# dictionary 
# tuple 
# list 
# set 

# number as a parameter and number as return type 
r1 = 10
r2 = 5
def Addition(x,y):
    #x = r1 # separate memory
    #y = r2 # separate memory
    return x + y
w3 = Addition(r1,r2)
print(w3)


# passing list as param

cities = ["pune","mumbai","nagpur","kolkalta"]
def AddCity(listC):
    # listC = cities # reference added to same memory
    listC.append("wardha")
    print(listC) 
AddCity(cities)
print(cities) 
print("--------------------------------------------------------------------")
#----------------------------------------------
# passing dict as param
# city ---- pune
info = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    'age':12,
}

def addCity(dictInfo):
    # dictInfo = info
    dictInfo['city'] = "pune"
    print(dictInfo) # output
addCity(info)
print(info) # output
print("--------------------------------------------------------------------")

# passing function as parameter to another funtion
# function class function
def sum(x,y):
    return x + y
def addition(a,b,fn):
    #fn = sum
    # def fn(x,y):
    #     return x+ y

    q9 = fn(a,b)
    print(q9)

addition(120,20,sum)

# print(sum) # printing function reference
# sum(12,3) # call function
