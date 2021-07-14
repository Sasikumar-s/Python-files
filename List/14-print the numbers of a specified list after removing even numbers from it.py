#print the numbers of a specified list after removing even numbers from it
a=[]
l=int(input("Enter len"))
for i in range(l):
	ele=int(input())
	a.append(ele)
b=[]
for x in a:
	if(x%2!=0):
		b.append(x)
print(b)