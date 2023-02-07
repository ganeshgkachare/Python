# pass continue break

s = "abs457B436"
for i in range(len(s)):
    if s[i].isupper() == True:
        print(True)
        #break
    elif s[i].isupper() == False:
        print(i)
        pass
    else:
        print(False)
print("stop")

print("--------------------------------")
for i in range(len(s)):
    if s[i].isupper() == True:
        print(True)
        #break
    elif s[i].isupper() == False:
        print(i)
        continue
    else:
        print(False)        
print("stop")