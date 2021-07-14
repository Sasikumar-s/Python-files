#To find Root of a number
def root(n):
	if n>=0:
		return n
	else:
		return root(n**0.5)
a = int(input("Enter Value"))
c=root(a)
print(c)

#using build in method
import math
b=math.sqrt(a)
print(b)