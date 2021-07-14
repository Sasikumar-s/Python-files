#print a specified list after removing the 0th, 4th and 5th elements
s1=list(input("Enter String"))
del s1[0]
del s1[4]
del s1[5]
print(''.join(s1))
