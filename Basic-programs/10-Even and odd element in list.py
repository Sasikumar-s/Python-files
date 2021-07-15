#Even and odd element in list

l = int(input("Enter length"))
a=[]
even=[]
odd=[]
for i in range(l):
	ele = int(input())
	a.append(ele)
for x in a:
	if x%2==0:
		even.append(x)
	else:
		odd.append(x)
print("Odd elements {} and even list {}".format(odd,even))