nm,b=input().split()
a=[]
a.append(nm)
a.append(b)
list = [all(x[i] == x[i+1] for i in range(len(x)-1)) for x in zip(*a)]

c=a[0][:list.index(0) if list.count(0) > 0 else len(list)]
kk=len(nm)-len(c)
k=len(b)-len(c)
print(kk+k)
