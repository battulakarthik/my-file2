n,m=map(int,input().split())
c=0
for i in range(0,m):
    for j in range(0,m):
        if i*j==m:
            if i+j==n/2:
                c=1

if c==1:print("yes")
else:print("no")
