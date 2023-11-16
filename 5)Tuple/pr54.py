n=int(input("Enter size of tuple : "))
tuple1=()
tuple2=()
for x in range(0,n):
	num=int(input("Enter tuple 1 element : "))
	tuple1+=(num,)
for x in range(0,n):
	num=int(input("Enter tuple 2 element : "))
	tuple2+=(num,)
print("Tuple 1 is : ",tuple1)
print("Tuple 2 is : ",tuple2)
tuple3=()
for x in range(0,n):
	num=tuple1[x]%tuple2[x]
	tuple3+=(num,)
print("Tuple with modulo is : ",tuple3)
