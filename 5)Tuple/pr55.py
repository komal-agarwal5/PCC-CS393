n=int(input("Enter size of tuple : "))
tuple1=()
for x in range(0,n):
	num=int(input("Enter value of tuple : "))
	tuple1+=(num,)
print("Inputted tuple is : ",tuple1)
list1=[]
for x in range(0,n):
	tuple2=()
	tuple2+=(tuple1[x],)
	num=pow(tuple1[x],3)
	tuple2+=(num,)
	list1.append(tuple2)
print("List of tuples is : ",list1)
