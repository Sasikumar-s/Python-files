#3D matrix multiplex

a=[[1,2,3,4],[5,6,7,8],[9,8,7,6]]
b=[[1,2,3],[3,2,1],[9,8,7]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			result[i][j] += a[i][k]*b[k][j]
for r in result:
	print(r)
