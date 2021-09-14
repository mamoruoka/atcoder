n=int(input())
T=list(map(int,input().split()))
s=sum(T)
dp=[[0 for _ in range(s+1) ] for _ in range(n)]
dp[0][T[0]]=1
for i in range(1,n):
    dp[i][T[i]]=1
    for j in range(s+1):
        if dp[i-1][j]==1:
            dp[i][j]=1
            dp[i][j+T[i]]=1

for i in range(-(-s//2),s+1):
    if dp[n-1][i]:
        print(i)
        break

