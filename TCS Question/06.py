a=int(input())
b=a*a
rem = b%10
if(a>=1):
	if rem==a:
		print("Correct number")
	else:
		print("Incorrect number")
else:
	print("Wrong number")