a=int(input("Enter Input\t"))
s=0
temp=a
while(a!=0):
	rem = a%10
	s= s+rem
	a=a//10
if (temp%s)==0:
	print("Harshaed Number")
else:
	print("Nor Harshaed Number")