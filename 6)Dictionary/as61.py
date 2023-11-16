n=int(input("Enter size of dictionary : "))
dict1={}
for x in range(0,n):
	key1=input("Enter key : ")
	val1=input("Enter value : ")
	dict1[key1]=val1
print("Inputted dictionary is : ",dict1)
x=dict1.keys()
list1=sorted(x)
dict2={}
for i in range(0,n):
	key2=list1[i]
	val2=dict1[key2]
	dict2[key2]=val2
print("Sorted by key is : ",dict2)
dict3={}
k1=[]
v1=[]
k1=list(dict1.values())
v1=list(dict1.keys())
for i in range(0,n):
	key3=k1[i]
	val3=v1[i]
	dict3[key3]=val3
y=dict1.values()
list2=sorted(y)
dict4={}
for i in range(0,n):
	val4=list2[i]
	key4=dict3[val4]
	dict4[key4]=val4
print("Sorted by value is : ",dict4)
	

