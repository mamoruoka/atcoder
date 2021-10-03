from collections import defaultdict
n=int(input())
X=defaultdict(int)
for i in range(n):
    a,b=map(int,input().split())
    X[a]+=1
    X[a+b]-=1

X = list(sorted(X.items(), key=lambda x:x[0]))

Ans=[0]*(n+1)
cnt=0
for i in range(len(X)-1):
    cnt+=X[i][1]
    Ans[cnt]+=X[i+1][0] - X[i][0] 
print(*Ans[1:])