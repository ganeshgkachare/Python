# 1. CREATE TEXT FILE WITH BELOW DATA IN IT AND NAME  IT AS colors.txt
# Brown
# Yellow
# Green
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\colors.txt","w")
f.write("Brown\nYellow\nGreen")
f.close()
print("-------------------------------")
# 2. READ THE FILE  colors.txt AND DISPLAY THE OUTPUT ON THE SCREEN
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\colors.txt","r")
print(f.read())
f.close()
print("-------------------------------")
# 3. ADD BELOW DATA IN THE FILE colors.txt WITHOUT REMOVING OLD DATA
# BLUE
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\colors.txt","a")
f.write("\nBLUE")
f.close()
print("-------------------------------")
# 4. DISLAY THE DATA OF THE FILE colors.txt USING FOR LOOP 
f = open(r"E:\Ganesh\Coding\python\Rahul_Sir_11\colors.txt","r")
for i in f:
    print(i)
print("-------------------------------")