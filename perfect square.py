n,m=map(int,input().split())
c=0
for i in range(n+1,m):
    for j in range(0,i):
        if j*j==i:
            c+=1
print(c)
