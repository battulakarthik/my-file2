d=int(input())
nm=input()
k=[]
for i in range(0,d):
    if nm[i]=="a" or nm[i]=="e" or nm[i]=="i" or nm[i]=="o" or nm[i]=="u":
      gg=0
    else:k.append(nm[i])
k.reverse()
for i in range(0,len(k)):
    print(k[i])
