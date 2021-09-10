a=int(input("Enter Input\t"))
count=0
for i in range(2,a):
	if(a%i==0):
		count+=1
print(count)