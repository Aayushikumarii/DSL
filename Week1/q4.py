x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
z=int(input('enter 3rd number'))
if(x>y):
	if(x>z):
		largest=x
	elif(z>x):
		largest=z
else:
	largest=y 
print(largest)