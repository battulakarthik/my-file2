n=input()
n=list(n)
m=[]
for i in range(0,len(n)):
    c=0
    for j in range(0,len(n)):
        for k in range(0,len(m)):
            if n[i]==m[k]:
                c+=1
        if i!=j and n[i]!=n[j]:
            c+=1
            if c<=1:m.append(n[i])
for i in range(0,len(m)):
    print(m[i],end='')

