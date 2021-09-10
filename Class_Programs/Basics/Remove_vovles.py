a = input("Enter input\t")
l=[]
l2=['a','e','i','o','u']
for i in a:
	if i not in l2:
		l.append(i)
print(''.join(l))