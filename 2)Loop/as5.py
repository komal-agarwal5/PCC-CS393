n=int(input("Enter a number if you want to proceed else enter 0: "))
c=0
sum=0
while n!=0:
	c+=1
	sum+=n
	n=int(input("Enter a number if you want to proceed else enter 0 : "))
print("Sum of numbers is : ",sum)
if(c==0):
	print("Average of numbers is : ",0)
else:
	avg=float(sum/c)
	print("Average of numbers is : ",avg)
