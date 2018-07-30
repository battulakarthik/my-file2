nm,k=input().split()
nm=int(nm)
k=int(k)
count=0
a = [int(x) for x in input().split()]
b=[int(x) for x in input().split()]
for i in range(0,k):
    for j in range(0,nm):
        if b[i]==a[j]:
            count+=1
if(count==len(b)):
    print("YES")
else:print("NO")

