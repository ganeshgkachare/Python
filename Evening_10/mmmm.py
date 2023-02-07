
def avg (*args):
    average =float(sum (args) / len(args))
    average = round(average,2)
    print(average)

avg(2,5)


class Car:
    def __init__(self,max_speed,units):
        self.max_speed=max_speed
        self.units=units
    def __str__(self):
        return "Car with the maximum speed of "+str(self.max_speed)+" "+ str(self.units)

class Boat:
    def __init__(self,max_speed):
        self.max_speed=max_speed
    def __str__(self):
        return "Boat with the maximum speed of "+str(self.max_speed)+" "+ "knots"