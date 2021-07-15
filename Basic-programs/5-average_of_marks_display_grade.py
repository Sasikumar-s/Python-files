#Find average marks and dispaly grade
a = int(input("Enter mark 1"))
b = int(input("Enter mark 2"))
c = int(input("Enter mark 3"))
d = int(input("Enter mark 4"))
e = int(input("Enter mark 5"))
avg = ((a+b+c+d+e)/5)
print("Average",avg)
if(avg>=90):
	print("A Grade")
elif(avg>=70):
	print("B Grade")
elif(avg>=60):
	print("C Grade")
elif(avg>=40):
	print("D Grade")
