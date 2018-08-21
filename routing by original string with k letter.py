n,m=input().split()
m=int(m)
c=len(n)-m
print(n[-m:],end='')
print(n[:c])
