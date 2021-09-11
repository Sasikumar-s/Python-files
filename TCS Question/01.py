a = int(input())
b = int(input())
c = int(input())
l1=[]
l2=[]
sum1=0
sum2=0
for i in range(a):
	ele = int(input())
	ele-=c
	l1.append(ele)
for i in range(b):
	ele = int(input())
	ele-=c
	l2.append(ele)
for i in l1:
	sum1 = sum1+i
for i in l2:
	sum2= sum2+i
if sum1>sum2:
	total = (sum2-sum1)-c
	print(total)
elif sum1==sum2:
	print("BALANCED")
else:
	total = (sum1-sum2)-c
	print(total)