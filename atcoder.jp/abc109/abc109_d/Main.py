h,w=map(int,input().split())
M=[]
for i in range(h):
    M.append(list(map(int,input().split())))

ANS=[]
cnt=0
for i in range(h):
    for j in range(w):
        if M[i][j]%2==1:
            for x,y in [(0,1),(1,0)]:
                if (0<=i+x and i+x<h) and (0<=j+y and j+y<w):
                    M[i+x][j+y]+=1
                    cnt+=1
                    ANS.append([i+1,j+1,x+i+1,y+j+1])
                    break
print(cnt)
for i in range(cnt):
    print(*ANS[i])