nm=int(input())
lst=[int(x) for x in input().split()]
kk=sorted(lst)
kk.reverse()
for i in range(0,nm):
    print(kk[i],end='')
