a= input("Enter Input\t")
b = input("Enter next input\t")
c=a.split()
count=0
for i in c:
	if i==b:
		count+=1
print(count)