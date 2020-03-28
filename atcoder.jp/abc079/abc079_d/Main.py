h,w=map(int,input().split())
C=[]
for i in range(10):
    C.append(list(map(int,input().split())))
A=[]
for i in range(h):
    A.append(list(map(int,input().split())))

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j]=min(C[i][j],C[i][k]+C[k][j])
cnt=0
for i in range(h):
    for j in range(w):
        if A[i][j]==-1 or A[i][j]==1:
            continue
        cnt+=C[A[i][j]][1]
print(cnt)