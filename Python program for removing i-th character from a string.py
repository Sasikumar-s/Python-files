#Python program for removing i-th character from a string
s1 = input("Enter input\t")
char = int(input("Enter which char you want to delete\t"))
count=0
for x in s1:
	count+=1
	if count==char:
		s2=s1.replace(x,'')
print(s2)