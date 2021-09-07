str1= input("Enter Sentence\t")
s2 = str1.split(' ')
final = []
for i in s2:
	a=i[::-1]
	final.append(a)
print(' '.join(final))