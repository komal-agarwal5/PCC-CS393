n=int(input("Enter number of lines to be read : "))
f=open("file1.txt","r")
s=""
for i in range(0,n):
	s+=f.readline()
print(s)
