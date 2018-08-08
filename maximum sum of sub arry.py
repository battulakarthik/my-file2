nm=int(input())
lst=[int(x) for x in input().split()]
c=0
for i in range(0,nm):
    c+=lst[i]
print(c)
