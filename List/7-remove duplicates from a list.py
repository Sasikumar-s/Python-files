#remove duplicates from a list
a=[]
l = int(input("Enter length"))
for i in range(l):
	ele = input()
	a.append(ele)
b=set(a)
print(b)