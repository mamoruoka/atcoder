from collections import deque
n=int(input())
X=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    X[a-1].append(b-1)
    X[b-1].append(a-1)

# 予めソートしておくことにより効率化
for i in range(n):
    X[i].sort(reverse=True)

Visited=[False]*n
Origin=[0]*n
Y=deque([0])
ANS=[]
while len(Y)!=0:
    idx = Y.pop()
    ANS.append(idx+1)
    if Visited[idx]:
        continue
    Visited[idx]=True
    for i in X[idx]:
        if not Visited[i]:
            Y.append(idx)
            Y.append(i)

print(*ANS)

