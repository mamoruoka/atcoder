n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
mod=998244353

dp=[1 for _ in range(max(B)+1)]

for i in range(n):
    # 1個前までの可能な数列の個数を累積和で管理する
    nx = [0] * (max(B)+1)
    for j in range(A[i],B[i]+1):
        nx[j] = dp[j]
    dp = nx
    # 次の所では到達範囲が延びているので最後までやる
    for i in range(max(B)):
        dp[i+1]+=dp[i]
        dp[i+1]%=mod

print(dp[max(B)])