#Python program to check if a string has at least one letter and one number

s = input("Enter string")   #sasi kumar
s2 = s.strip()
alpha = s2.isalpha()
#print(alpha)
numeric = s2.isnumeric()
#print(numeric)
if(alpha or numeric):
    print("False")
else:
    print("True")