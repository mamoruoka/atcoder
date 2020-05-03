from _collections import defaultdict
n,k=map(int,input().split())
X=defaultdict(int)
for i in range(k):
    d=int(input())
    A=list(map(int,input().split()))
    for a in A:
        X[a]+=1
print(n-len(X))