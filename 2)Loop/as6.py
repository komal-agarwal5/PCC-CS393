n=int(input("Enter number of rows : "))
for x in range (n,0,-1):
    for y in range(0,x):
        print(x," ",end="")
    print()
