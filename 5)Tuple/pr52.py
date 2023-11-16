tuple1=()
newt=()
n=int(input("Enter size of tuple : "))
for x in range(0,n):
	num=input("Enter tuple element : ")
	tuple1+=(num,)
print("Inputted Tuple is : ",tuple1)
s=int(input("Enter starting index for copying elements : "))
l=int(input("Enter ending index for copying elements : "))
le=len(tuple1)
if s>le or l>le or s<0 or l<0:
	print("Invalid input")
else: 
	newt=tuple1[s:l+1]
	print("New tuple is : ",newt)

