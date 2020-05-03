n,m=map(int,input().split())
H=list(map(int,input().split()))
X=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    X[a-1].append(b-1)
    X[b-1].append(a-1)
ans=0
for i in range(n):
    flag=True
    if len(X[i])==0:
        ans+=1
    else:
        for x in X[i]:
            if H[i]<=H[x]:
                flag=False
        if flag:
            ans+=1
print(ans)