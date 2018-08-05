nm=int(input())
kk=[int(x) for x in input().split()]
c=kk
for x in range(0,nm):
    count=0
    for i in range(0,nm):
        if kk[x]==c[i]:
            count+=1
    else:
        if count==1:
            f=kk[x]
print(f)


