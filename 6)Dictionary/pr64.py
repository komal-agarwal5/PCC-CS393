str=input("Enter a sentence : ")
l=str.split()
n=int(input("Enter size of dictionary : "))
dict1={}
c=int(0)
for x in range(0,n):
	key1=input("Enter key : ")
	val1=input("Enter value : ")
	dict1[key1]=val1
print("Original string is : ",str)
print("Inputted dictionary is : ",dict1)
list1=[]
for word in l:
	if word in dict1:
		list1.append(dict1[word])
		c=c+1
	else:
		list1.append(word)
if(c==0):
	print("No matching word found")
else:
	print("Replaced string is : "," ".join(list1))

