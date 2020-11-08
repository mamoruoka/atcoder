import itertools
n=int(input())
A=[0]+list(map(int,input().split()))
B=list(itertools.accumulate(A))
C=list(itertools.accumulate(B))

M=[B[0]]
m=B[0]
for i in range(1,n+1):
    m=max(m,B[i])
    M.append(m)


S=[]
for m,c in zip(M[1:],C[:-1]):
    S.append(m+c)
print(max(S))