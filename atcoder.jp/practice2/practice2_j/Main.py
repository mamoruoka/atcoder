class SegTree:
    def __init__(self, n, A):
        # 葉のノード数は2**x個となるようにする
        # 初期化リストAを入れても足りない分は単位元を入れる
        self.leaf_size = 1 << (n - 1).bit_length()
        self.min_ele = -10**10
        self.tree = [self.min_ele] * 2 * self.leaf_size

        # 初期化(1-indexed)
        # 葉はself.leaf_size個のノード、それまでの親のノードはself.leaf_size-1個である
        for i in range(n):
            self.tree[self.leaf_size + i] = A[i]
        for i in range(self.leaf_size-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[i*2], self.tree[i*2+1])

    
    def segfunc(self, x, y):
        return max(x,y)

    # a_l~a_r-1までの最大値を返す
    def calc_max(self, l, r):
        l += self.leaf_size
        r += self.leaf_size
        res = self.min_ele
        while l<r:
            if l & 1:
                res = self.segfunc(self.tree[l], res)
                l += 1
            if r & 1:
                res = self.segfunc(self.tree[r-1], res)
            l >>= 1
            r >>= 1
        return res
                 
    def update(self, i, x):
        idx = self.leaf_size + i
        self.tree[idx] = x
        while idx > 1:
            # 共通の親を持つノードとのXORを計算する
            self.tree[idx >> 1] = self.segfunc(self.tree[idx], self.tree[idx ^ 1])
            idx >>= 1



n,q=map(int,input().split())

A=list(map(int,input().split()))
st=SegTree(n, A)
for i in range(q):
    t, x, y = map(int,input().split())
    if t == 1:
        st.update(x-1, y)
    elif t == 2:
        # x,yは1-indexedである
        print(st.calc_max(x-1, y))
    else:
        idx = x - 1
        ans = n + 1
        while idx < n:
            if y > st.tree[st.leaf_size+idx]:
                idx += 1
            else:
                ans = idx + 1
                break
        print(ans)
        

