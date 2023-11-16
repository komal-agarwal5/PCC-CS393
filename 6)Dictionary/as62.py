dict1={"name":"Harry","assignment" : [82, 56, 44, 30],"test" : [80, 80],"lab" : [67.90, 78.72]}
print("Data is : ",dict1)
ast=sum(dict1["assignment"])/len(dict1["assignment"])
tet=sum(dict1["test"])/len(dict1["test"])
lat=sum(dict1["lab"])/len(dict1["lab"])
av=(0.1*ast)+(0.7*tet)+(0.2*lat)
if av>=90:
	gr='A'
elif av>=80 and av<90:
	gr='B'
elif av>=70 and av<80:
	gr='C'
elif av>=60 and av<70:
	gr='D'
else:
	gr='FAIL'
print("Average marks of ",dict1["name"]," is : ",av)
print("Letter grade of ",dict1["name"]," is : ",gr)

