from collections import defaultdict
import sys
sys.setrecursionlimit(8**6)
n = int(input())
C = list(map(int, input().split()))
X = defaultdict(list)
for c in C:
    X[c] = 0
M = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    M[a-1].append(b-1)
    M[b-1].append(a-1)

Visited = [False]*n
ANS = []


def dfs(idx):
    Visited[idx] = True
    X[C[idx]] += 1
    if X[C[idx]] < 2:
        ANS.append(idx+1)
    for nxidx in M[idx]:
        if not Visited[nxidx]:
            dfs(nxidx)
    # 戻る直前の処理
    X[C[idx]] -= 1

dfs(0)

for i in sorted(ANS):
    print(i)