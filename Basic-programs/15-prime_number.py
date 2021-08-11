#To find prime number 

n = int(input("Enter your input"))
count =0
for i in range(1,n):
	if n%i==0:
		count+=1
		print(count)
if count<=2:
	print("This is prime number")
else:
	print("This is not prime number")