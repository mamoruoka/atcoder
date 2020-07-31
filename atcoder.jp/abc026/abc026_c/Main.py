n=int(input())
B=[[] for i in range(30)]

for i in range(n-1):
    B[int(input())].append(i+2)

M=[0]*(n+1)

for i in reversed(range(n+1)):
    if len(B[i])==0:
        M[i]=1
    else:
        X=[M[b] for b in B[i]]
        M[i]=max(X)+min(X)+1

print(M[1])
