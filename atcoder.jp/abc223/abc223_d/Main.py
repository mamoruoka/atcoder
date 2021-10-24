from collections import defaultdict, deque
import heapq
n,m=map(int,input().split())
# 入力次数(そのノードにどれだけのノードが入ってきてるか)
in_cnt = defaultdict(int)
# そのノードからどのノードに向かって出ているか
out = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    in_cnt[b-1]+=1
    out[a-1].append(b-1)

ANS=[]
q = [i for i in range(n) if in_cnt[i]==0]
heapq.heapify(q)
while len(q)!=0:
    # 常に入力次数が0のもの中で最小のものを取り出す
    # 入力次数が0＝こいつの親のノードは全て既にリストにある
    v = heapq.heappop(q)
    ANS.append(v+1)
    for nv in out[v]:
        in_cnt[nv]-=1
        # 入力次数が0になったらリストに入れる
        if in_cnt[nv]==0:
            heapq.heappush(q, nv)

if len(ANS)!=n:
    print(-1)
else:
    print(*ANS)




