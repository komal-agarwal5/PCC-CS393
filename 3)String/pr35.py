s=input("Enter a string : ")
p=input("Enter prefix string : ")
str=s.split(" ")
new=""
for x in str:
	x=p+x
	new=new+" "+x
print("New string is : ",new)

