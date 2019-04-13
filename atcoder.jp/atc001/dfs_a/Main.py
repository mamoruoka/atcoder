import sys
sys.setrecursionlimit(1000000)

h,w=map(int,input().split())

M=[list(input()) for _ in range(h)]


def dfs(x,y):
    if x<0 or x>=h or y<0 or y>=w or M[x][y]=='#':
        return 
    if M[x][y]=='g':
        print('Yes')
        sys.exit()
    M[x][y]='#'
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
    
    
for i in range(h):
    for j in range(w):
        if M[i][j]=='s':
            x=i
            y=j

dfs(x,y)
print('No') 