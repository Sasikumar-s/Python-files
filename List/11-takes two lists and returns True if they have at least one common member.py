#Python function that takes two lists and returns True if they have at least one common member
def check(a,b):
	for x in a:
		if(x in b):
			print("True")
			return
s1=[];s2=[]
print("Enter first string")
for i in range(5):
	ele = input()
	s1.append(ele)
print("Enter Second string")
for j in range(5):
	ele = input()
	s2.append(ele)
check(s1,s2)