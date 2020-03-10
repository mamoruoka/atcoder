h,w=map(int,input().split())
M=[]


M=[input() for _ in range(h)]

def bfs(x,y):
    dist=[[-1]*w  for _ in range(h)]
    seen=[[False]*w for _ in range(h)]
    stk=[(x,y,0)]
    while stk:
        px,py,dst=stk.pop(0)
        if seen[px][py]:
            continue
        seen[px][py]=True
        
        if M[px][py]=='#':
            dist[px][py]=0
            continue
        
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            if px+x<0 or px+x>=h or py+y<0 or py+y>=w:
                continue
            else:
                stk.append((px+x,py+y,dst+1))
        dist[px][py]=dst
    ans=0

    for i in range(h):
        ans=max(max(dist[i]),ans)
    return ans

ans=0
for i in range(h):
    for j in range(w):
        if M[i][j]=='#':
            continue
        ans=max(bfs(i,j),ans)

print(ans)