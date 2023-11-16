n=int(input("Enter size of dictionary 1 : "))
dict1={}
for x in range(0,n):
	key1=input("Enter key : ")
	val1=input("Enter value : ")
	dict1[key1]=val1
m=int(input("Enter size of dictionary 2 : "))
dict2={}
for x in range(0,m):
	key2=input("Enter key : ")
	val2=input("Enter value : ")
	dict2[key2]=val2
print("Dictionary 1 is : ",dict1)
print("Dictionary 2 is : ",dict2)
list1=list(dict1.keys())
l=len(list1)
for x in list1:
	if x in dict2.keys():
		print("Key ",x," of dictionary 1 has value in dictionary 2 of : ",dict2[x])
	else:
		print("Key",x," of dictionary 1 not found in dictionary 2")
newdict = {**dict1 , **dict2}
print(newdict)


	
