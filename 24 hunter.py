n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if lst[i]+lst[j]==m:
                c=1
if c==1:print("YES")
else:print("NO")
