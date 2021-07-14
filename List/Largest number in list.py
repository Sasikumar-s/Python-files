#Largest number in list
a=[]
b=[]
l=int(input("Enter length"))
for i in range(l):
  ele=int(input())
  a.append(ele)
a.sort()
print("Largest number ",a[-1])

#Without BUIDIN function
max=a[0]
for x in a:
	if(x>max):
		max=x
print("Without build in function",max)

#program to get the smallest number from a list
min=a[0]
for x in a:
	if(min<a):
		min=a
print("Minimum number=",min)