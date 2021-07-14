#Python program to print even length words in a string
string = input("Enter String")
a =string.split(" ")
for i in a:
    if(len(i)%2==0):
        print(i)
    else:
        pass