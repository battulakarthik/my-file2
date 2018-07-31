nm=int(input())
sq=0

for i in range(0,nm):
    dgt=nm%10
    sq=dgt**2+sq
    nm=nm//10
print(sq)
