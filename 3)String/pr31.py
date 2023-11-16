s=input("Enter a string : ")
i=input("Enter string to be inserted : ")
l=int(len(s)/2)
new=s[0:l]+" "+i+" "+s[l:]
print("New string is : ",new)


