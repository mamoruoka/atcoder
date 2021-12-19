import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
M=[[] for _ in range(n)]
ans="Yes"

par=[-1]*n
def find(n):
    if par[n]<0:
        return n
    par[n]=find(par[n])
    return par[n]
def union(x,y):
    px,py=find(x),find(y)
    if px==py:
        return False
    if px>py:
        px,py=py,px
    par[px]+=par[py]
    par[py]=px
    return True

for i in range(m):
    a,b=map(int,input().split())
    M[a-1].append(b-1)
    M[b-1].append(a-1)
    if not union(a-1,b-1):
        ans="No"

if ans=="Yes":
    for i in range(n):
        if len(M[i])>2:
            ans="No"
            break

print(ans)