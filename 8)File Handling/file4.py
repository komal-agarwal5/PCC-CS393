f1=open("file4(1).txt","r")
n=f1.readlines()
s=""
for i in n:
	s+=i
f1.close()
f2=open("file4(2).txt","w+")
f2.write(s)
f2.close()
print("Content has been copied")
