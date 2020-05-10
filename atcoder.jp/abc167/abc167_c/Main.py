n,m,x=map(int,input().split())
X=[]
for i in range(n):
    X.append(list(map(int,input().split())))

ans=10**9
for i in range(2**n):
    s=format(i,'b')
    Z=s.zfill(n)
    cost=0
    M=[0]*m
    for j in range(n):
        if Z[j]=='1':
            cost+=X[j][0]
            for k in range(m):
                M[k]+=X[j][1+k]
    if all([m>=x for m in M]):
        ans=min(ans,cost)

if ans==10**9:
    print(-1)
else:
    print(ans)