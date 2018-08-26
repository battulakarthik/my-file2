n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
c=0
for i in range(0,n):
    f=lst[i]
    for j in range(i+1,n):
        if m==f+lst[j]:
            c=1
if c==1:print("yes")
else:print("no")

