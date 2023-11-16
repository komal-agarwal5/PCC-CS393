tuple1=()
tuple2=()
n=int(input("Enter size of first tuple : "))
for x in range(0,n):
	num=input("Enter tuple 1 element : ")
	tuple1+=(num,)
print("Inputted tuple 1 is : ",tuple1)
m=int(input("Enter size of second tuple : "))
for x in range(0,m):
	num=input("Enter tuple 2 element : ")
	tuple2+=(num,)
print("Inputted tuple 2 is : ",tuple2)
temp=tuple1
tuple1=tuple2
tuple2=temp
print("Tuple 1 after swapping is  : ",tuple1)
print("Tuple 2 after swapping is  : ",tuple2)


