from collections import deque
n,m=map(int,input().split())
X=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    X[a-1].append(b-1)
    X[b-1].append(a-1)

q=deque([])
D=[None]*n
D[0]=0
# 最短経路の数
Cnt=[0]*n
Cnt[0]=1
q.append(0)
while not len(q)==0:
    # disはidxに辿り着くまでの距離, cntはidxに辿り着く経路の数
    idx=q.popleft()

    for i in X[idx]:
        if D[i] is None:
            D[i]=D[idx]+1
            q.append(i)
            Cnt[i]=Cnt[idx]
        elif D[i]==D[idx]+1:
            Cnt[i]+=Cnt[idx]
            Cnt[i]%=(10**9+7)

print(Cnt[n-1])