# Segment treeの右の子ノードが存在しないバージョン
class Bit:
    def __init__(self, n):
        self.size = n
        # 区間和を長さnの配列で管理する(index1が開始点)
        self.tree = [0] * (n + 1)

    # a1~aiまでの和を返す
    def sum(self, i):
        s = 0
        # tree[i]が管理する長さはiの最も下の立っているビットの位置に等しい
        # 現在のインデックスに区間の長さを引くことで左隣の区間に移動することができる
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        # iはnまでしか取ることができない
        while i <= self.size:
            self.tree[i] += x
            # tree[i]が管理する長さはiの最も下の立っているビットの位置に等しい
            # 現在のインデックスに区間の長さを足すことで親のインデックスに移動することができる
            i += i & -i


n,q=map(int,input().split())
bit=Bit(n)
A=list(map(int,input().split()))
# 初期化
for i in range(n):
    bit.add(i+1, A[i])
for i in range(q):
    t, x, y = map(int,input().split())
    if t == 0:
        bit.add(x+1, y)
    else:
        print(bit.sum(y) - bit.sum(x))