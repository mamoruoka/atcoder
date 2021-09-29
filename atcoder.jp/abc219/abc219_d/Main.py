n=int(input())
x,y=map(int,input().split())
N=[]
for i in range(n):
    a,b=map(int,input().split())
    N.append([a,b])
M=[[[10**5 for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
M[0][0][0]=0
for i in range(1,n+1):
    a,b=N[i-1]
    for ix in range(x+1):
        for iy in range(y+1):
            if M[i-1][ix][iy] != 10**5:
                # i番目の弁当箱を選ばない場合
                M[i][ix][iy] = min(M[i-1][ix][iy], M[i][ix][iy])
                # i番目の弁当箱を選ぶ場合
                M[i][min(ix+a,x)][min(iy+b,y)] = min(M[i][min(ix+a,x)][min(iy+b,y)], M[i-1][ix][iy]+1)

if M[n][x][y]!=10**5:
    print(M[n][x][y])
else:
    print(-1) 
