n,m=map(int,input().split())
X=[]
for i in range(m):
    a,b,c=map(int,input().split())
    X.append([a-1,b-1,c])
X.sort(key=lambda x:x[2])

par=[-1]*n
def root(x):
    if par[x]<0:
        return x
    par[x] = root(par[x])
    return par[x]
def unite(x,y):
    rx = root(x)
    ry = root(y)
    if rx==ry:
        return True
    if rx > ry:
        rx, ry = ry, rx
    par[rx] += par[ry]
    par[ry] = rx
    return False

ans=0
for i in range(m):
    a,b,c = X[i]
    if c<=0:
        unite(a,b)
    else:
        if unite(a,b):
            ans+=c
print(ans)
