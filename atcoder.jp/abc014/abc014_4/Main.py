import numpy as np
import sys
sys.setrecursionlimit(10**7)

n=int(input())
Map=[[] for _ in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    Map[x-1].append(y-1)
    Map[y-1].append(x-1)

euler_tour=[]

Visited=[False]*n
# それぞれの頂点がeuler_tourリスト上で初めて出てきたときのidx
First_appear_idx=[0]*n
cnt = 0
def dfs(idx,d,prev):
    Visited[idx] = True
    euler_tour.append([idx, d])
    First_appear_idx[idx] = len(euler_tour) - 1
    for nxidx in Map[idx]:
        if not Visited[nxidx]:
            dfs(nxidx, d+1, idx)
    euler_tour.append([prev, d-1])
    
dfs(0,0,0)

euler_tour = np.array(euler_tour[:-1])


def sparse_table(d):
    n = len(d)
    # 深さの配列の長さnを超えないような値が2**max_kである
    max_k = (n).bit_length() - 1
    INF = 10 ** 18
    # 最小値を求めるので適当な大きな値を入れる
    table = np.full((n, max_k + 1), INF, dtype=np.int64)
    # 0列目には2**0の距離なのでそのまま入れる
    table[:, 0] = d

    for k in range(1, max_k + 1):
        # まだ範囲に入れていない所から始めればよい
        # その範囲は1ビット?ずつ増えていく
        k2 = 1 << (k - 1)
        k3 = (1 << k) - 1
        # 二つのテーブルの要素同士を比較する
        table[:n - k3, k] = np.minimum(table[:n - k3, k - 1], table[k2:n - k3 + k2, k - 1])
    return table

# table[i][j]=左端がd_iで長さが2**jである配列の最小値
table = sparse_table(euler_tour[:,1])


q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    a_idx = First_appear_idx[a-1]
    b_idx = First_appear_idx[b-1]

    if a_idx > b_idx:
        a_idx, b_idx = b_idx, a_idx

    # 区間の長さ未満のビット数
    # 8→4 9→4 16→5....と変換される
    l = (b_idx - a_idx).bit_length() - 1
    # a,bの共通最小祖先の根からの深さを求める
    # bは右端なので、2 ** lだけ引いた分が始点となる
    lca = min(table[a_idx][l], table[b_idx-2**l+1][l])
    # aの根からの距離+bの根からの距離-lca=a,bの最短距離
    print(euler_tour[a_idx][1] + euler_tour[b_idx][1] - 2 * lca + 1)
     

