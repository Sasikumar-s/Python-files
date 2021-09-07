a=int(input("Enter Input\t"))
s=0
while(a!=0):
	rem = a%10
	s=s+rem
	a=a//10
print(s)