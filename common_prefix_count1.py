nm=int(input())
a=[]
for i in range(0,nm):
    a.append(input())
list = [all(x[i] == x[i+1] for i in range(len(x)-1)) for x in zip(*a)]

cmfr=a[0][:list.index(0) if list.count(0) > 0 else len(list)]
print(len(cmfr))
