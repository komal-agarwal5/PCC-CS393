list=[]
n=int(input("Enter size of list : "))
for x in range(0,n):
	num=int(input("Enter value : "))
	list.append(num)
print("Original list is : ",list)
max1=list[0]
smax=list[0]
for x in range(0,n):
	num=list[x]
	if num>max1 :
		smax=max1
		max1=num
	elif num>smax and max1!=num :
		smax=num
	elif max1==smax and smax!=num:
		smax=num
print("Second maximum element is : ",smax)
