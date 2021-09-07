a=int(input("Enter Value A\t"))
b=int(input("Enter value B\t"))
a2=a*a
b2=b*b
rev=0
while(a2!=0):
	rem = a2%10
	rev = rev*10+rem
	a2=a2//10
if rev==b2:
	print("This is Adam number")
else:
	print("This is not Adam number")