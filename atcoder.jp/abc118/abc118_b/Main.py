n,m=map(int,input().split())
M=[0]*m
for i in range(n):
    x=list(map(int,input().split()))
    k=x[0]
    A=x[1:]
    for j in range(k):
        M[A[j]-1]+=1

print(M.count(n))