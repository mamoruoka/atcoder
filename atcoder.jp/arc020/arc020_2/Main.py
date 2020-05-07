import itertools
n,c=map(int,input().split())
A=[int(input()) for _ in range(n)]
X=[i for i in range(1,11)]
ans=n*c
for v in itertools.permutations(X,2):
    count=0
    for i in range(n):
        x=v[0] if i%2==0 else v[1]
        count=count+1 if A[i]!=x else count
    ans=min(ans,count)
print(ans*c)