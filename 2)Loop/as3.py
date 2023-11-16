n=int(input("Enter a number : "))
p=1
for x in range(1,n+1):
    p*=x
if(n==0):
    print("Factorial is 1")
else:
    print("Factorial is : ",p)
