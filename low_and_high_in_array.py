nm=int(input())
if nm<=10000:
    storage= input()
    storage1=[int(x) for x in storage.split()]
    print(min(storage1),max(storage1))
