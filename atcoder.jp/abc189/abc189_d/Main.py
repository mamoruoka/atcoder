n=int(input())
S=[input() for i in range(n)]
ans=0
Y=[[0,0] for _ in range(n+1)]
# 0がTrue 1がFalse
Y[0][0]=1
Y[0][1]=1
for i in range(n):
    if S[i]=="OR":
        Y[i+1][0] = Y[i][0]*2 + Y[i][1]
        Y[i+1][1] = Y[i][1]
    else:
        Y[i+1][0] = Y[i][0]
        Y[i+1][1] = Y[i][0] + Y[i][1]*2
print(Y[n][0])