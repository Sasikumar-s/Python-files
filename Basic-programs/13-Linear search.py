#Linear search

def search(list,item):
	found= False
	for i in range(l):
		if a[i]==item:
			found=True
			print("Position ",i)
			return found


l = int(input("How many elements"))
a=[]
for i in range(l):
	ele = int(input())
	a.append(ele)
item = int(input("Enter Which element to search"))
print(search(a,item))