list=[]
n=int(input("Enter size of list : "))
for x in range(0,n):
	num=input("Enter a value for list : ")
	list.append(num)
print("Original list is : ",list)
temp=list[0]
l=len(list)-1
list[0]=list[l]
list[l]=temp
print("List with first and last element swapped is : ",list)
