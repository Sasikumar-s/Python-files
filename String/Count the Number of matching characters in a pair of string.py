#Python | Count the Number of matching characters in a pair of string
s1=input("Enter string 1")
s2 = input("Enter string2")
s1_low=s1.lower()
s2_low=s2.lower()
a=[]
for x in s1_low:
    if x not in a:
        a.append(x)
res1=''.join(a)
b=[]
for x in s2_low:
    if x not in b:
        b.append(x)
res2=''.join(b)
count=0
for x in res1:
    if x in res2:
        count+=1
print(count)