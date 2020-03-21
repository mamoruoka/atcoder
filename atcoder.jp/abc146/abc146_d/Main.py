n=int(input())
X=[[] for _ in range(n)]

for i in range(n-1):
    a,b=map(int,input().split())
    X[a-1].append([b-1,i])

ANS=[0]*(n-1)
VC=[0]*n
k=1
for v,c in enumerate(X):
    t=1
    for b, i in c:
        if VC[v]==t:
            t+=1
        VC[b]=t
        ANS[i]=t
        k=max(k,t)
        t+=1
print(k)
for i in range(n-1):
    print(ANS[i])