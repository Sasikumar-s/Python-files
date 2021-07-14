#find the list of words that are longer than n from a given list of words
s1=[]
count=0
l=int(input("Enter how many string"))
for i in range(l):
	ele = input()
	s1.append(ele)
max_len = int(input("Enter maxinum length"))
for x in s1:
	if(len(x)>max_len):
		count+=1
print(count)