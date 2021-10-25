h,w=map(int,input().split())
M=[]
for i in range(h):
    M.append(input())

def calc_around(M,i,j):
    cnt=0
    for ix,iy in [(0,0),(0,1),(1,0),(1,1)]:
        if M[i+ix][j+iy]=="#":
            cnt+=1
    return cnt

ans = 0
for i in range(h-1):
    for j in range(w-1):
        black_cnt = calc_around(M,i,j)
        if black_cnt == 1 or black_cnt == 3:
            ans += 1
print(ans)