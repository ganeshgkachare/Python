#1. find data type of 
h0  = ()
h1  = ('GOA')
h2  = ('GOA',"PANJIM")
h3  = {"GOA"}
h4  = {"GOA","PANJIM"}
print(type(h0))
print(type(h1))
print(type(h2))
print(type(h3))
print(type(h4))
print("-----------------------------------------------------------")

#2 . ADD "400076" IN BEOW SET
pin_mum = {400074,400075,400077}
pin_mum.add(400076)
print(pin_mum)
print("-----------------------------------------------------------")

#3 . SORT THE ITEMS IN THE BELOW SET ALSO REMOVE '0' FORM THE SET
runs_vk = {45,78,45,12,2,89,103,0}
print(sorted(runs_vk))
runs_vk.remove(0)
print(runs_vk)
print("-----------------------------------------------------------")

#4 . REMOVE '0' FORM THE SET 
runs_vk = {45,78,45,12,2,89,103,0}
runs_vk.remove(0)
print(runs_vk)
print("-----------------------------------------------------------")