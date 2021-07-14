#Find GCD numbers
def GCD(a,b):
	if(b==0):
		return a
	else:
		return GCD(b,a%b)

a=int(input("Enter A value"))
b = int(input("Enter  B value"))
c=GCD(a,b)
print("GCD is: {}".format(c))