import numpy as np
n=int(input())
S=[input() for i in range(n)]
T=[input() for i in range(n)]
X=[]
Y=[]
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            X.append([i,j])
        if T[i][j] == "#":
            Y.append([i,j])
R=np.matrix([[0,-1],[1,0]])
X=np.array(X)
Y=np.array(Y)

def correspond(x, y):
    # 位置関係を両社同じにするためにsortする(開始点を(0,0)になるようにしてsetでも良い)
    x=np.array(sorted(x,key=lambda x:(x[0],x[1])))
    y=np.array(sorted(y,key=lambda x:(x[0],x[1])))
    Z = x - y
    # 全ての要素について差分(=平行移動量)が等しいならYes
    return np.all([np.all(z==Z[0]) for z in Z])

if len(X)!=len(Y):
    print("No")
else:
    ans="No"
    for _ in range(4):
        for i in range(len(X)):
            X[i] = np.dot(X[i], R)
        if correspond(X, Y):
            ans = "Yes"
    print(ans)

