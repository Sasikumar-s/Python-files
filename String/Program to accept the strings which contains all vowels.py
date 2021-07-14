#Python | Program to accept the strings which contains all vowels
s= input("Enter String")
s1=s.lower()
l = len(s1)
count=0
set1=("aeiou")
for x in s1:
    if((x=='a') or(x=='e') or (x=='i') or (x=='o') or (x=='u')):
        count+=1
if(count==5):
    print("Accepted")
else:
    print("Not accecpted")
    
