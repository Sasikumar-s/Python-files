#Sum of  the list
a=[]
l = int(input("Enter how many numbers"))
for i in range(l):
  ele=int(input())
  a.append(ele)
sum=0
for x in a:
  sum=sum+x
print(sum)