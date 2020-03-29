from collections import deque

n=int(input())
X=[[] for _ in range(n)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    X[a-1].append([b-1,c])
    X[b-1].append([a-1,c])
    
distance=[-1]*n

q,k=map(int,input().split())

Que=deque([[k-1,0]])

while Que:
    b,c=Que.popleft()
    distance[b]=c
    for pb,pc in X[b]:
        if distance[pb]==-1:
            Que.append([pb,c+pc])

for i in range(q):
    x,y=map(int,input().split())
    print(distance[x-1]+distance[y-1])