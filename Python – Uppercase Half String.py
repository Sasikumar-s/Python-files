#Python – Uppercase Half String
string = input("Enter String")
count=0
res=[]
length=len(string)
a=length/2
for n in string:
    count+=1
    if(count<=a):
        res.append(n)
    else:
        print(n.upper())
print(res,end=" ")