from collections import deque
H,W=map(int,input().split())
M=[input() for _ in range(H)]
D=[[10**5]*W for _ in range(H)]

cnt=0
for i in range(H):
    cnt+=M[i].count('#')

visited=[[0]*W for _ in range(H)]
q=deque([[0,0,0]])

while q:
    x,y,dist=q.popleft()
    if visited[x][y]==1:
        continue
    visited[x][y]=1
    D[x][y]=dist
    
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        if x+i>=H or y+j>=W or x+i<0 or y+j<0:
            continue
        if M[x+i][y+j]=='#':
            continue
        q.append([x+i,y+j,dist+1])
if D[H-1][W-1]==10**5:
    print(-1)
else:
    print((H*W-1-D[H-1][W-1])-cnt)