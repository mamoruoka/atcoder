import heapq

h,w,T=map(int,input().split())
M=[input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if M[i][j]=='S':
            sr,sc=i,j
        if M[i][j]=='G':
            gr,gc=i,j
    
def dijkstra(x):
    dist=[[1<<30]*w for _ in range(h)] #全ての視点からの距離を無限(10**6)と仮定
    dist[sr][sc]=0 #始点の距離は0と確定
    q=[]
    heapq.heappush(q,(0,sr,sc))
    while q:
        v,r,c=heapq.heappop(q) #地点の確定
        if dist[r][c]<v:
            continue
        for j,k in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr=r+j
            nc=c+k
            if nr>=0 and nr<h and nc>=0 and nc<w:
                t=1
                if M[nr][nc]=='#':
                    t=x
                if dist[nr][nc]>v+t: #既に確定した距離より小さければ書き直す
                    dist[nr][nc]=v+t
                    heapq.heappush(q,(v+t,nr,nc)) 
    return dist[gr][gc]<=T

mi=0
ma=T+1
while ma-mi>1: #max=min+1になったらやめる
    mid=(ma+mi)//2
    if dijkstra(mid):
        mi=mid
    else:
        ma=mid
print(mi)