#Minimum in list of number also find maximum number in list

l = int(input("Enter length of list"))
a=[]
for i in range(l):
	ele = int(input())
	a.append(ele)
max=a[0]
for i in range(0,l):
	if max<a[i]:
		max=a[i]
min=a[0]
for i in range(0,l):
	if min>a[i]:
		min=a[i]
print("maximum number",max)
print("Minimum number",min)