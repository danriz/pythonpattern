import math
nmycar='-'
arr=[[nmycar for i in range (7)] for j in range (7)]

m=0
n=7
k=math.ceil(7/2)
for h in range (4):
    for x in range (m,n):
        arr[m][x]=k
        arr[n-1][x]=k
        arr[x][n-1]=k
        arr[x][m]=k
    m=m+1
    n=n-1
    k=k-1

for x in range (len(arr)):
    for y in range (len(arr[0])):
        print(str(arr[x][y]).rjust(3),end='')
    print()
