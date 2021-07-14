#count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
s1=[]
c=0
l=int(input("ENter how many string"))
for i in range(l):
	ele = input()
	s1.append(ele)
for x in s1:
	if(len(x)>=2):
		if(x[0]==x[-1]): #Check first==last element
			c+=1
print(c)