m=int(input("Enter first number : "))
n=int(input("Enter second number : "))
c=0
print("Prime numbers within range is : ")
for x in range(m,n+1):
	c=0
	for y in range (2,x):
		if(x%y==0):
			c=c+1
	if(c==0 and x!=0 and x!=1):
		print(x)
