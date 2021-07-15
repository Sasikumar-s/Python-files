#To check number is polindrome

a=int(input("Enter number"))
temp = a
rev=0
while a>0:
	dig=a%10
	rev = rev*10+dig
	a=a//10
if rev==temp:
	print("Given number is palindrome :",temp)
else:
	print("Given number is not a palindrome :",temp)