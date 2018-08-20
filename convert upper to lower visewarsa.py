nm=input()
lst=[x for(x) in nm]
f=[]
for i in range(0,len(nm)):
    c=str(lst[i])
    if c.islower():
        f.append(c.upper())
    else:
        f.append(c.lower())
for i in range(0,len(nm)):
    print(f[i],end='')
