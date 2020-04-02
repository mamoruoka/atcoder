n,m,Q=map(int,input().split())
M=[[0]*n for _ in range(n)]
for i in range(m):
    l,r=map(int,input().split())
    M[r-1][l-1]+=1

for q in range(n):
    for p in reversed(range(1,n)):
        M[q][p-1]+=M[q][p]
for p in range(n):
    for q in range(n-1):
        M[q+1][p]+=M[q][p]        

for i in range(Q):
    p,q=map(int,input().split())
    print(M[q-1][p-1])