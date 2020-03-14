n=int(input())


A='abcdefghijklmnopqrstuvwxyz'
P=['a']
X=[[] for _ in range(n)]
X[0].append('a')
for i in range(n-1):
    P.append(A[i+1])
    for j in range(len(X[i])):
        flag=False
        for k in range(len(P)):
            X[i+1].append(X[i][j]+P[k])
            if not P[k] in X[i][j]:
                flag=True
            if flag:
                break
Y=X[n-1]
for i in range(len(Y)):
    print(Y[i])