n,c=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(c)]
C=[list(map(int,input().split())) for _ in range(n)]

X1=[0]*(c+1)
X2=[0]*(c+1)
X0=[0]*(c+1)

for i in range(n):
    for j in range(n):
        if (i+1+j+1)%3==0:
            X0[C[i][j]]+=1
        elif (i+1+j+1)%3==1:
            X1[C[i][j]]+=1
        else:
            X2[C[i][j]]+=1
A=[]
for c1 in range(c):
    for c2 in range(c):
        if c2==c1:
            continue
        for c3 in range(c):
            if c3==c2 or c3==c1:
                continue
            ans=0
            for i in range(1,c+1):
                ans+=X0[i]*D[i-1][c1]+X1[i]*D[i-1][c2]+X2[i]*D[i-1][c3]
            A.append(ans)
print(min(A))
                