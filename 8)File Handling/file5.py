fn=input("Enter the name of the file you want to open : ")
st=input("Enter the string pattern you want to search : ")
f=open(fn,"r")
c=0
for line in f:
	word=line.split()
	for i in word:
		if i.strip(".")==st:
			c=c+1
print("Number of occurrence of the string pattern in file is : ",c)
		
