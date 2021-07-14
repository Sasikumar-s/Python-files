#Python Program to remove all duplicates from a given string
s1 = input("Enter string\t")
s2=[]

for x in s1:
	if x not in s2:
		s2.append(x)

print(''.join(s2))