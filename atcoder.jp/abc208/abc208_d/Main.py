n,m=map(int,input().split())
Map=[[10**11 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    Map[a][b] = c
for i in range(n+1):
    Map[i][i] = 0

ans=0
# ワーシャルフロイド法
# kを単調に増やしていくので第３項は省略できる
# 街iから街jまで街k-1を使ってかかった時間(Map[i][j])と街kを必ず経由して街iから街jまでかかる時間(Map[i][k] + Map[k][j])を比較
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            Map[i][j] = min(Map[i][k] + Map[k][j], Map[i][j])
            if Map[i][j] < 10**11:
                ans+=Map[i][j]


print(ans)
