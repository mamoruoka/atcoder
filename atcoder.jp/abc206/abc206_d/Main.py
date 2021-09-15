n=int(input())
A=list(map(int,input().split()))

par=[-1]*(max(A)+1)
# 親検索
def root(x):
    if par[x]<0:
        return x
    par[x] = root(par[x])
    return par[x]
# グループ結合
def unite(x,y):
    rx = root(x)
    ry = root(y)
    if rx==ry:
        return
    if rx > ry:
        rx, ry = ry, rx
    par[rx] += par[ry]
    par[ry] = rx

for i in range(n):
    if A[i]!=A[n-1-i]:
        unite(A[i], A[n-1-i])

ans=0
for p in par:
    if p<0:
        ans+=abs(p)-1
print(ans)