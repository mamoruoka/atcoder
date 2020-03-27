n=int(input())
X=[[] for _ in range(n)]
for i in range(n-1):
    u,v,w=map(int,input().split())
    X[u-1].append([v-1,w])
    X[v-1].append([u-1,w])
C=[-1]*n
q=[[0,0]]


while q:
    v,w=q.pop()
    if w%2==0:
        C[v]=0
    else:
        C[v]=1
    for pv,pw in X[v]:
        if C[pv]==-1:
            q.append([pv,pw+w])

for c in C:
    print(c)
    