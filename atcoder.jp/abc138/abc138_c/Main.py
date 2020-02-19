n=int(input())
V=list(map(int,input().split()))

V.sort()

s=(V[0]+V[1])/2

for i in range(2,n):
    s+=V[i]
    s/=2
print(s)