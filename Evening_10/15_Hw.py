#1 . UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT

z = ([22,33], [True,False],[0,1],[111,999])
a,b,c,d=z
print(c[0])
print("--------------------------------------------------")

#2. UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT 
#t_num = (1,2,3,4,5,6,7,8,9)
#    ,,c,,,_ = t_even

#3. convert the list into sets:

name1 = ['R', 'A', 'H', 'U', 'L']
name1_set = set(name1)
print(name1_set)
print(type(name1_set))
print("--------------------------------------------------")

name2 = ['A', 'K', 'S', 'H', 'A', 'Y']
name2_set = set(name2)
print(name2_set)
print(type(name2_set))
print("--------------------------------------------------")

bool3 = [True, False, False, False, True]
bool3_set = set(bool3)
print(bool3_set)
print(type(bool3_set))
print("--------------------------------------------------")

#4. find length of the set
#    use for loop to print the items of  the set

d = set([True, False, False, False, True])
print(len(d))
for i in d:
    print(i)
print("--------------------------------------------------")
