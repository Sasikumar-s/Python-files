#Armstrong Number
num  = int(input("Enter number "))
temp= num
sum = 0
l=[]
while num>0:
	r = num%10
	l.append(r)
	num = num//10
for x in l:
	x=x*x*x
	sum = sum+x
if sum==temp:
	print("This is armstrong number :",temp)
else:
	print("Tnis is not Armstrong number :",temp)