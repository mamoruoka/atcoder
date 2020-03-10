h,w=map(int,input().split())
M=[input() for _ in range(h)]

L=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if M[i][j]=='#':
            L[i][j]=0
        elif j!=0:
            L[i][j]=L[i][j-1]+1
        else:
            L[i][j]=1
    
R=[[0]*w for _ in range(h)]
for i in range(h):
    for j in reversed(range(w)):
        if M[i][j]=='#':
            R[i][j]=0
        elif j!=w-1:
            R[i][j]=R[i][j+1]+1
        else:
            R[i][j]=1

U=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if M[i][j]=='#':
            U[i][j]=0
        elif i!=0:
            U[i][j]=U[i-1][j]+1
        else:
            U[i][j]=1

D=[[0]*w for _ in range(h)]
for i in reversed(range(h)):
    for j in range(w):
        if M[i][j]=='#':
            D[i][j]=0
        elif i!=h-1:
            D[i][j]=D[i+1][j]+1
        else:
            D[i][j]=1

ans=1
for i in range(h):
    for j in range(w):
        if M[i][j]=='#':
            continue
        ans=max(ans,L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
print(ans)