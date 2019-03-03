n=int(input())

X=[0]*(n+1)
X[0]=2
X[1]=1
for i in range(2,n+1):
    X[i]=X[i-1]+X[i-2]

print(X[n])