# # # Which of the following two Python codes will give same output?

# tupl=(5,3,1,9,0)
# print(tupl[:-1])
# print(tupl[0:5])
# print(tupl[0:4])
# print(tupl[-4:])
# class st:

class  Books:
    def __init__(self,pages):
        self.pages = pages
    def sum_pages(self,other):
        return self.pages + other.pages

    def __add__(self,other):
        return self.pages + other.pages

    def __sub__(self,other):
        return self.pages - other.pages

z1 = Books(300)
z2 = Books(50)



print("Using operator overloading:" , z1 + z2)

print(z1.sum_pages(z2))
print(z1 - z2) 