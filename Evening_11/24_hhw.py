'''
1.  For below  object roshan of class bank 

make the pin a private variable

Change pin to 1111 thorugh name mangling and print the new value through name mangling

Change pin to 2222  thorugh setter method and print the new value through getter method

roshan = bank("Roshan", 555 , 1000 , 1234)
'''

class bank:
    def __init__(self,name, acc , bal, pin ):
        self.name  = name
        self.acc  = acc
        self.bal  = bal
    #make the pin a private variable
        self.__pin  = pin

    #setter
    def changePin(self,newPin):
         self.__pin  = newPin
         return self.__pin

    #getter
    def showNewPin(self):
        return self.__pin

roshan = bank("Roshan", 555 , 1000 , 1234)

# Change pin to 1111 thorugh name mangling and print the new value through name mangling
print("------mangling--------")
roshan._bank__pin=1111
print(roshan._bank__pin)

# Change pin to 2222  thorugh setter method and print the new value through getter method
print("------set--get------")
roshan.changePin(2222) #setter
print(roshan.showNewPin()) #getter