#Python – Avoid Spaces in string length
string = input("Enter String")
count=0
for n in string:
    if(n==' '):
        continue
    else:
        count+=1
print(count)