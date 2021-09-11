a = int(input("Enter Input\t"))
l=[]
for i in range(a):
	ele = int(input())
	l.append(ele)
for i in range(a):
	if(i!=a):
		if l[i]==l[i+1]:
			l[i]+=1
			break;
print(l)