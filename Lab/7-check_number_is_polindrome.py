#To check number is polindrome
l=[]
a=int(input("Enter number"))
while a>0:
	q=a%10
	l.append(q)
	a=a//10
print(''.join(l))