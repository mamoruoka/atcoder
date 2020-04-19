n,k=map(int,input().split())

ans=0
A=[i for i in range(n+1)]
for i in range(1,n+1):
    A[i]+=A[i-1]

B=[i for i in range(n+1)]
for i in reversed(range(n)):
    B[i]+=B[i+1]

for i in range(k,n+2):
    ans+=B[-i]-A[i-1]+1
print(ans%(10**9+7))