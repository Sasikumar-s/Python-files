#Python program to find uncommon words from two Strings
s1 = input("Enter string\t")
s2 = input("Enter second string\t")
b=[]
for x in s1:
	if x not in s2:
		b.append(x)
for x in s2:
	if x not in s1:
		b.append(x)
print(''.join(b))