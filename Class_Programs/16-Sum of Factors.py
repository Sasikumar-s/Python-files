a=int(input("Enter Input\t"))
s=0
for i in range(2,a):
	if a%i==0:
		s=s+i
print(s)