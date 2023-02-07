e = {2,3,4,5,6,7,8}
o = {6,7,8,9,10,11}


print("--------------intersection---------------")
print(e.intersection(o))
print(e&o)
print("--------------union---------------")
print(e.union(o))
print(e|o)
print("--------------diff---------------")
print(e.difference(o))
print(e-o)
print("--------------sy.diff---------------")
print(e.symmetric_difference(o))
print(e^o)
print("-----------------------------")
print(e.issubset(o))