'''A Caesar cipher is a simple substitution 
cipher in which each letter of the plain 
text is substituted with a letter found by
 moving n places down the alphabet.
 For example, assume the input plain text 
 is the following:

		**abcd xyz

If the shift value, n, is 4, then the encrypted
text would be the following:

		**efgh bcd

'''
str1= input("Enter Input string \t")
list1=[]
final_word = ['x','y','z']
for i in str1:
	if i not in final_word:
		ass = ord(i)
		ass=ass+4
		converted = chr(ass)
		list1.append(converted)
	else:
		if i=='x':
			list1.append('a')
		elif i=='y':
			list1.append('b')
		else:
			list1.append('c')
print("Encrypted String is \t ",''.join(list1))
