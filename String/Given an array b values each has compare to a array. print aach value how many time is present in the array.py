#Given an array b values each has compare to a array. print aach value how many time is present in the array
s1 = input("Enter string\t")
s2 = input("Enter which character to count\t")
for x in s2:
    print("{} = {}".format(x,s1.count(x)))