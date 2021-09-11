a=int(input())
l=[]
for i in range(a):
	ele = int(input())
	l.append(ele)
b=int(input())
l.sort()
print(l[b-1])