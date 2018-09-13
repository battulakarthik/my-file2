n=input()
n=list(n)
f=[]
for i in range(0,len(n)):
    c=0
    for j in range(0,len(n)):
        for k in range(0,len(f)):
            if n[i]==f[k]:
                c+=1
        if i!=j and n[i]!=n[j]:
            c+=1
            if c<=1:f.append(n[i])
for i in range(0,len(f)):
    print(f[i],end='')

