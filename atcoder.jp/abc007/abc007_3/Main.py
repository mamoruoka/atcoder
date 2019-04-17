r,c=map(int,input().split())
sx,sy=map(int,input().split())
gx,gy=map(int,input().split())

M=[list(input()) for _ in range(r) ]

D=[[1<<30]*c for _ in range(r)]

D[sx-1][sy-1]=0

que=[]
que.append([0,sx-1,sy-1])
while que:
    v,x,y=que.pop(0)
    for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
        if x+j<0 or x+j>=r or y+k<0 or y+k>=c or M[x+j][y+k]=='#':
            continue
        M[x+j][y+k]='#'
        if D[x+j][y+k]>v+1:
            D[x+j][y+k]=v+1
        que.append([v+1,x+j,y+k])
print(D[gx-1][gy-1])