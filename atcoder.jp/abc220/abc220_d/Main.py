n=int(input())
A=list(map(int,input().split()))
X=[[0 for _ in range(n)] for _ in range(10)]

X[A[0]][0]=1
for i in range(1,n):
    for j in range(10):
        if X[j][i-1]!=0:
            X[(A[i]*j)%10][i] += X[j][i-1]
            X[(A[i]*j)%10][i] %= 998244353
            X[(A[i]+j)%10][i] += X[j][i-1]
            X[(A[i]+j)%10][i] %= 998244353

for i in range(10):
    print(X[i][n-1])