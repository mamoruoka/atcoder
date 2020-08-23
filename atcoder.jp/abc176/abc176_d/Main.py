from _collections import deque
h,w=map(int,input().split())
c_h,c_w=map(int,input().split())
d_h,d_w=map(int,input().split())
M=[input() for i in range(h)]
V=[[10**9]*w for i in range(h)]

q=deque([[0,c_h-1,c_w-1]])

while q:
    warp,x,y=q.popleft()

    if V[x][y]!=10**9:
        continue
    V[x][y]=warp

    if x==d_h-1 and y==d_w-1:
        break

    for px in range(-2,3):
        for py in range(-2,3):
            if 0<=x+px<h and 0<=y+py<w:
                if px == 0 and py == 0:
                    continue
                if M[x + px][y + py] == '#':
                    continue
                if abs(px)+abs(py)<=1:
                    q.appendleft([warp,x+px,y+py])
                else:
                    q.append([warp+1,x+px,y+py])


if V[d_h-1][d_w-1]==10**9:
    print(-1)
else:
    print(V[d_h-1][d_w-1])