#string = input()
#l=[]
#for i in string:
#	if i not in l:
#		l.append(i)
#	elif i in l:
#		l.remove(i)
#print(len(l))

string = input()
l=[]
for i in string:
	if i not in l:
	   l.append(i)
    else:
	  
	   count=count+1
	   if(count>1):
	    l.remove(i)
print(len(l))