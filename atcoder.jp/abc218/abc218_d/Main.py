from collections import defaultdict
n=int(input())
M=defaultdict(set)
for i in range(n):
    x,y=map(int,input().split())
    M[x].add(y)
ans=0
m = [x for x in M.values()]
for i in range(len(m)-1):
    for j in range(i+1, len(m)):
        a = len(m[i]&m[j])
        ans += (a*(a-1))/2
print(int(ans))

