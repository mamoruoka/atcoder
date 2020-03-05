import heapq

n,m=map(int,input().split())

A=list(map(int,input().split()))

A=[i*-1 for i in A]

heapq.heapify(A)

for i in range(m):
    x=heapq.heappop(A)
    if x%2==0:
        heapq.heappush(A,x//2)
    else:
        heapq.heappush(A,x//2+1)
print(-1*sum(A))