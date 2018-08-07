nm,k=input().split()
nm,k=int(nm),int(k)
c=[int(x) for x in input().split()]
c.sort()
print(c[nm-k])
