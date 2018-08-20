n,m=map(int,input().split())
c=0
lst=[int(x) for x in input().split() ]
for i in range(0,n):
    if m==lst[i]:
        c=1
if c==1:
    print("yes")
else:print("no")
