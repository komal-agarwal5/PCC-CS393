list=[]
e=0
o=0
n=int(input("Enter size of list : "))
for x in range(0,n):
	num=int(input("Enter value : "))
	list.append(num)
print("Original list is : ",list)
for x in range(0,n):
	num=list[x]
	if(num>0):
		e=e+1
	else:
		o=o+1
print("Count of positive numbers is : ",e)
print("Count of negative numbers is : ",o)
