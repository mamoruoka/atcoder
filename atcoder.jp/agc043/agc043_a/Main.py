h,w=map(int,input().split())
S=[]
for i in range(h):
    S.append(input())
    
cnt=0
D=[[10**9]*w for _ in range(h)]
D[0][0]=0
for i in range(h):
    for j in range(w):
        for x,y in [(0,1),(1,0)]:
            if i+x>=h or j+y>=w:
                continue
            if S[i][j]!=S[i+x][j+y]:
                D[i+x][j+y]=min(D[i][j]+1,D[i+x][j+y])
            else:
                D[i+x][j+y]=min(D[i][j],D[i+x][j+y])
                
                
if S[0][0]=='#':
    print(1+D[h-1][w-1]//2)
else:
    print(D[h-1][w-1]//2+(S[0][0]!=S[h-1][w-1]))