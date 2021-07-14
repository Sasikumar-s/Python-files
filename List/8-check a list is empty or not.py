#check a list is empty or not
a=input("Enter String")
b=list(a)
if(len(b)==0):
	print("The list is empty")
else:
	print(''.join(b))