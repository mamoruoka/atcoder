K=int(input())


ANS=[[[] for _ in range(10)] for _ in range(10)]
for i in range(10):
    ANS[0][i].append(str(i))
for i in range(1,10):
    for j in range(10):
        if 1<=j and j<=8:
            for k in [j-1,j,j+1]:
                for v in ANS[i-1][k]:
                    ANS[i][j].append(str(j)+v)
        elif j==0:
            for k in [j,j+1]:
                for v in ANS[i-1][k]:
                    ANS[i][j].append(str(j)+v)
        elif j==9:
            for k in [j-1,j]:
                for v in ANS[i-1][k]:
                    ANS[i][j].append(str(j)+v)

X=[]
for i in range(10):
    for j in range(1,10):
        for k in ANS[i][j]:
            X.append(int(k))
X.sort()
print(X[K-1])    