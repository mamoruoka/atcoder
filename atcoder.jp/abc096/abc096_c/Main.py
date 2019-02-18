h,w=map(int,input().split())
S=[]
for i in range(h):
    S.append(input())

ans='Yes'
for i in range(1,h-1):
    for j in range(1,w-1):
        if S[i][j]=='#' and S[i+1][j]=='.' and S[i-1][j]=='.' and S[i][j+1]=='.' and S[i][j-1]=='.':
            ans='No'

print(ans)