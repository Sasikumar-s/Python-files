a=int(input("Enter Value \t"))
cube=0
temp=a
while(a!=0):
	rem =a%10
	cube = cube+(rem*rem*rem)
	a=a//10
if cube==temp:
	print("Armstrong Number")
else:
	print("Not Armstrong Number")