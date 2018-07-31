nm,k=input().split()
nm=int(nm)
k=int(k)
a=[int(x) for x in input().split()]
i=0
while i<k:
     if i+1<nm:
         a[i],a[i+1]=a[i+1],a[i]
         i+=1
     else:
         break

for i in range(0,nm):
    if i<nm-1:
        k=' '
    else:k=''
    print(a[i],end=k)
