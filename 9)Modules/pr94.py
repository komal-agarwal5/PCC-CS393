import math
h=float(input("Enter height of the cylinder : "))
r=float(input("Enter radius of the cylinder : "))
vol=math.pi*(r**2)*h
sa=2*math.pi*r*(r+h)
print("Volume of cylinder is : ",vol)
print("Surface area of cylinder is : ",sa)

