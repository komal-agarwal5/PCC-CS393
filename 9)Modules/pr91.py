import random
import string
l=int(input("Enter length of random string : "))
str=""
for x in range(0,l):
	str+=random.choice(string.ascii_letters)
print("Random string is : ",str)
print("Random integer between two numbers : ")
r1=int(input("Enter starting range : "))
r2=int(input("Enter ending range : "))
num=random.randint(r1,r2)
print("Random number between ",r1," and ",r2," is : ",num)
mul=random.randint(0,10)*7
print("Random multiple of 7 between 0 and 70 is : ",mul)
