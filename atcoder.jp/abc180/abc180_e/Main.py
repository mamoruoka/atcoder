import heapq
n=int(input())
# Map[i][j]は街iから街jに行くまでのコスト
Map = [[0 for _ in range(n)] for _ in range(n)]
City = []
for i in range(n):
    x,y,z=map(int,input().split())
    City.append([x,y,z])

# 各町は一回だけ通るだけでよい
for i in range(n):
    for j in range(n):
        if i == j:
            Map[i][j] = 10**10
        else:
            Map[i][j] = abs(City[i][0]-City[j][0]) + abs(City[i][1]-City[j][1]) + max(0, City[j][2]-City[i][2])

dp = [[10**18 for _ in range(n)] for _ in range(2**n)]

dp[0][0] = 0
# iがこれまで到達した拠点の集合(bitで表現)
# jが現在の位置
# kがこれから訪れる拠点
# これらは被っていても問題ない？
for i in range(2**n):
  for j in range(n):
    for k in range(n):
      dp[i|(1<<k)][k]=min(dp[i|(1<<k)][k], dp[i][j]+Map[j][k])

print(dp[2**n-1][0])

