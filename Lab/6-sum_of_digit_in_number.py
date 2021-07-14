#Sum of the digit in number
a = int(input("Enter a number"))
sum=0
while a>0:
	q=a%10
	sum=sum+q
	a=a//10
print(sum)