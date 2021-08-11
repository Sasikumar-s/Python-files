#Python program to capitalize the first and last character of each word in a string

s = input("Enter string")   #sasi kumar
l=[]
str1 = s.title()    #To change first letter in capitalize--> Sasi Kumar 
str2 = str1.split(' ')  #Seperate each word in string -->['Sasi','Kumar']
for n in str2:
    q=n[-1]    #Find last letter in each word --> i,r
    a=n[-1].upper() #change last word into capitalize  -->I,R
    w=n.replace(q,a) #Replace that letter in list-->Chage i to I and r to R
    l.append(w)   #append the string  -->['SasI','KumaR']
    final = ' '.join(l) #Remove the list.Eg:: ['SasI','KumaR']--> SasI KumaR
print(final)