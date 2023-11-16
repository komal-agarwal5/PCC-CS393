list=[]
n=int(input("Enter size of list : "))
for x in range(0,n):
	num=input("Enter value : ")
	list.append(num)
print("Original list is : ",list)
l=0
r=len(list)-1
ll=len(list)//2
p=0
while p<ll:
	temp=list[l]
	list[l]=list[r]
	list[r]=temp
	l=l+1
	r=r-1
	p=p+1
print("Reversed list is : ",list) 
