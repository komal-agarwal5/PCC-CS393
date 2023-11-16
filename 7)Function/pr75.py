def make_sum(l):
   s=0
   for i in l:
       s=s+i
   print('The required sum is',s)

n=int(input('Enter the value of n:'))
i=1
l=[]
while i<=n:
	num=int(input('Enter the number'))
	i=i+1
	l.append(num)
make_sum(l)
