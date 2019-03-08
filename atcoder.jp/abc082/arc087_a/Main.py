import collections

n=int(input())

A=list(map(int,input().split()))

X=collections.Counter(A)
K=list(X.keys())
V=list(X.values())
cnt=0
for i in range(len(X)):
    if K[i]>V[i]:
        cnt+=V[i]
    elif K[i]<V[i]:
        cnt+=V[i]-K[i]

print(cnt)