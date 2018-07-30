nm=int(input())
a = [int(x) for x in input().split()]

for i in range(0,nm):
    for j in range(i+1,nm):
        if a[i]==a[j]:
            k=a[i]
            print(k)
            count=1
            break
if count !=1 :
    print("unique")
