import random
from datetime import datetime,timedelta,date
num1=random.randint(0,6-1)
print("Random integer between 0 and 6 excluding 6 is : ",num1)
num2=random.randint(5,10-1)
print("Random integer between 5 and 10 excluding 10 is : ",num2)
#num3=random.randint(0,10-3)+3
num3=random.randrange(0,11,3)
print("Random integer between 0 and 10 with a step of 3 : ",num3)
start=date(2022,11,14)
end=date(2023,8,2)
diff=(end-start).days
ran_days=random.randint(0,diff)
ran_date=start+timedelta(days=ran_days)
print("Random date between ",start," and ",end," is : ",ran_date)

