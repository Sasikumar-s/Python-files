a= input("Enter Input")
l=[]
for i in a:
	b=ord(i)
	if b>=65 and b<=90:
		b=b+32
		c=chr(b)
		l.append(c)
	else:
		b=b-32
		c=chr(b)
		l.append(c)
print(''.join(l))