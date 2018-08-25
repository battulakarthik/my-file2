n=int(input())
m=input()
c=[]
for i in range(n-1,-1,-1):
    if m[i]=='0':
        for j in range(i,-1,-1):
            if m[j]=='1':
                c.append(m[j])
        else:break
for i in range(0,len(c)):
    if i<len(c)-1:k=' '
    else:k=''
    print(c[i],end=k)
