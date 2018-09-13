n,m=map(int,input().split())
mx=[]
a=[]
c=[]
for i in range(0,n):
    row=[int(x) for x in input().split()]
    mx.append(row)
for i in range(0,n):
    for j in range(0,m):
        if mx[i][j]==0:
            a.append(i)
            a.append(j)
            c.append(a)
            a=[]
for k in range(len(c)):
    i=c[k][0]
    j=c[k][1]
    for l in range(0,n):
        mx[l][j]=0
    for l in range(0,m):
        mx[i][l]=0
for i in range(0,n):
    for j in range(0,m):
        if j<m-1:
            k=' '
        else:k=''
        print(mx[i][j],end=k)
    print()
