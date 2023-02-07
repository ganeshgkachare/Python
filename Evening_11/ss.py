# While Groot is good at heart, he is not intelligent. He loves pies but cannot find the right amount of sweetness. Groot doesn't want to eat a too sweet or bland pie. If a pie is too sweet, he wants to eat it with a pie that is bland to get to the right amount of sweetness he desires.
# Task:
# You must write a function or method that returns which pies Groot has to consume to get the right amount of sweetness.
# Input:
# One of the inputs is the sweetness values of the available pies and the other is the desired sweetness.
# Example:
# findPies([1, 2, 3, 2, 1], 6)

# returns [0, 1, 2] or [2, 1, 0]
#           0  1  2  3  4  5
# findPies([8, 4, 3, 2, 6, 5], 6)
# returns [1, 3] or [4]

def fn (ls,sweet=6):
    pie_ind=[]
    pie=[]
    for i in ls:
        if i <sweet and sum(pie)<=sweet:
            pie.append(i)
            if sum(pie)>sweet:
                pie.remove(i)
                pass
        if i ==sweet:
            pie_ind.append([ls.index(i)])
    pi=[]
    for j in pie:
        pi.append(ls.index(j))
    pie_ind.append(pi)
    return(pie_ind)

print(fn([1, 2, 3, 2, 1], 6))
print(fn([8, 4, 3, 2, 6, 5], 6))

