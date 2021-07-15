#To find exponention (power of the number)

def power(base,exp):
	if (exp==1):
		return(base)
	else:
		return(base*power(base,exp-1))


base = int(input("Enter base value"))
exp = int(input("Enter expo value"))
result = power(base,exp)
print("Result{}".format(result))