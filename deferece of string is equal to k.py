n,m,k=input().split()
k=int(k)
cc=0
for i in range(0,len(n)):
    if n[i]!=m[i]:
        cc+=1
if cc==k:
    print("yes")
else:print("no")
