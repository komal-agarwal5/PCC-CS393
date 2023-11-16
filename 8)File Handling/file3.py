n=int(input("Enter size of list : "))
list1=[]
for i in range(0,n):
	num=input("Enter content for list : ")
	list1.append(num)
print(list1)
f=open("file3.txt","w+")
for item in list1:
	f.write(item+"\n")
print("List has been added to text file")
f.close()
