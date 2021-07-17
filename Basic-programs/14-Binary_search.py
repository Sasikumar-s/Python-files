#Bainary search

def search(a,key):
	first=0
	last=l-1
	
	found = False
	while(first<=last and found	==False):
		mid=(first+last)//2
		if a[mid]==key:
			print("Your element is ",mid)
			found = True
		else:
			if key<a[mid]:
				last = mid-1
			else:
				first=mid+mid-1
	return found


l = int(input("Enter length of list"))
a=[]
for i in range(l):
	ele = int(input("Enter element"))
	a.append(ele)
key = int(input("Enter Search key"))
a.sort()
print(a)
print(search(a,key))