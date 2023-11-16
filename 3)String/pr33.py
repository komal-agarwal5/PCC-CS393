s1=input("Enter a string : ")
s2=input("Enter second string : ")
l1=len(s1)
l2=len(s2)
s1=sorted(s1)
s2=sorted(s2)
if l1==l2 and s1==s2 :
	print("String is anagram  ")
else:
	print("String is not anagram  ")

