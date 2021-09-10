a = int(input("Enter Input\t"))
l=[]
for i in range(a):
	ele = int(input())
	l.append(ele)
l.sort()
print(l)
if a==1:
	print("Invalid Input")
else:
	print(l[0],l[1])