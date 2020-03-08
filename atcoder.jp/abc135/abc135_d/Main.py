s=input()
dp=[[0]*13 for _ in range(len(s)+5)]
dp[0][0]=1
for i in range(len(s)):
    
    if s[i]!='?':  
        j=int(s[i])
        for k in range(13):
            dp[i+1][(k*10+j)%13]+=dp[i][k]
            dp[i+1][(k*10+j)%13]%=(10**9+7)
    else:
        for j in range(10):
            for k in range(13):
                dp[i+1][(k*10+j)%13]+=dp[i][k]
                dp[i+1][(k*10+j)%13]%=(10**9+7)

print(dp[len(s)][5])