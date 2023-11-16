s=input("Enter a string of atleast 2 length : ")
l=len(s)
if(l<2):
	print("Invalid string")
else:
	b=l-2
	c=s[b:]
	n=c+c+c+c	
	print("New string is : ",n)
