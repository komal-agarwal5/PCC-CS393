tuple1=()
n=int(input("Enter size of tuple : "))
for x in range(0,n):
	num=input("Enter tuple element : ")
	tuple1+=(num,)
print("Inputted tuple is : ",tuple1)
list1=[]
m=int(input("Enter size of list : "))
for x in range(0,m):
	num2=input("Enter list element : ")
	list1.append(num2)
print("Inputted list is : ",list1)
for x in range(0,n):
	num=tuple1[x]
	list1.append(num)
print("Modified list is : ",list1)
temp=list(tuple1)
for x in range(0,m):
	num2=list1[x]
	temp.append(num2)
tuple1=tuple(temp)
print("Modified tuple is : ",tuple1)

