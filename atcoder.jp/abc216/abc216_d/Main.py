from collections import deque
n,m=map(int,input().split())
# それぞれの番号の玉がどの番号の玉の真上にあるか
M=[[] for _ in range(n)]
T=deque([])
# それぞれの番号の玉の真上に玉があるか(0~2)
indegree=[0 for _ in range(n)]
ans="Yes"
for i in range(m):
    k=int(input())
    A=list(map(int,input().split()))
    for i in range(k-1):
        M[A[i]-1].append(A[i+1]-1)
        indegree[A[i+1]-1]+=1

used_cnt=0
for i in range(n):
    if indegree[i]==0:
        T.append(i)

Topological_sort = []

while len(T)!=0:
    idx = T.popleft()
    for t in M[idx]:
        indegree[t] -= 1
        if indegree[t] == 0:
            T.append(t)
    Topological_sort.append(idx)



if sum(indegree)!=0:
    print("No")
else:
    print("Yes")



