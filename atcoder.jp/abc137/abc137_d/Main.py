import heapq

n,m=map(int,input().split())
X=[[] for _ in range(10**5+5)]
for i in range(n):
    a,b=map(int,input().split())
    X[a-1].append(-b)

ans=0
p=[0]*m
heapq.heapify(p)
for i in range(m):
    for j in range(len(X[i])):
        heapq.heappush(p,X[i][j])
    a=heapq.heappop(p)
    ans+=a*-1
print(ans)