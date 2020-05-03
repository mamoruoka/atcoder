import itertools
n,m,q=map(int,input().split())
X=[]
B=[]
for i in range(q):
    X.append(list(map(int,input().split())))
for A in itertools.combinations_with_replacement(range(1,m+1),n):
    ans=0
    for x in X:
        if A[x[1]-1]-A[x[0]-1]==x[2]:
            ans+=x[3]
    B.append(ans)
print(max(B))