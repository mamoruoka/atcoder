n,m=map(int,input().split())
M=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    # 自分より番号が上のものだけを隣接成分として登録したい
    if a>b:
        b,a=a,b
    M[a-1].append(b-1)

ans=0
par=[-1 for _ in range(n)]
def find(x):
    if par[x]<0:
        return x
    par[x] = find(par[x])
    return par[x]
def union(x,y):
    px = find(x)
    py = find(y)
    # 親が一緒の場合何もしない
    if px==py:
        return False
    # 親が異なる場合、つまりまだつながっていないものどうしなら連結成分は一個減るはず
    if px>py:
        px,py=py,px
    par[px] += par[py]
    par[py] = px
    return True

A=[0]
for i in reversed(range(1,n)):
    # 最初は非連結を仮定
    ans+=1
    if len(M[i])!=0:
        # 自分より上の番号の隣接番号に対して
        for nxidx in M[i]:
            if union(i, nxidx):
                # 非連結同士を結ぶのなら答えは一つ減る
                ans-=1
    A.append(ans)

for a in reversed(A):
    print(a)