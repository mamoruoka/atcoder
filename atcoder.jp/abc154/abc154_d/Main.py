n,k=map(int,input().split())
P=list(map(int,input().split()))
for i in range(n):
    P[i]=0.5*(P[i]+1)
x=sum(P[:k])
s=[x]

for i in range(1,n-k+1):
    x=x-P[i-1]+P[i+k-1]
    s.append(x)

print(max(s))