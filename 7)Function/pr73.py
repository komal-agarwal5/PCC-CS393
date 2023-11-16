def check(a):
	lower=upper=0
	for i in a:
		if i.islower():
			lower=lower+1
		elif i.isupper():
			upper=upper+1
	print('No. of Upper case characters:',upper)
	print('No. of Lower case characters:',lower)
			
a=input('Enter the string : ')
check(a)
