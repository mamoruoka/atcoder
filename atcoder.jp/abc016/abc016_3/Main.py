n,m=map(int,input().split())

M=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    M[a-1].append(b-1)
    M[b-1].append(a-1)

for i in range(n):
    A=[]
    for j in M[i]:
        A.extend(M[j])
    print(len(set(A)-{i}-set(M[i])))