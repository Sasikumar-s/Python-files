no_of_qs = int(input())
max_time = int(input())
l1=[]
l2=[]
ft=st=0

for i in range(no_of_qs):
	a=int(input())
	l1.append(a)
for i in range(no_of_qs):
	a = int(input())
	if max_time>=a:
		l2.append(a)
	else:
		print("Enter limited time",max_time)
temp1=0
temp_l1=l1
temp2=0
l1.sort(reverse=True)
temp1=l1[0]
temp2=l1[1]
for i in range(no_of_qs):
	if temp_l1[i]==temp1:
		ft = i
	elif temp_l1[i]==temp2:
		st=i
	else:
		continue
print(l2[ft],l2[st])
if (l2[ft]+l2[st])<=max_time:
	print(temp2+temp1)
else:
	print("Not")