#Check if a given string is binary string or not
s1 = input("ENter string\t")
p={'0','1'}
n=set(s1)
if(n==p or n=={'0'} or n=={'1'}):
	print("Yes")
else:
	print("No")