def segfunc(x,y):
    return x^y
ide_ele = 0

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):

        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        # 葉の数は2**(n - 1).bit_length() (nを2**?になるまで拡大している)
        self.num = 1 << (n - 1).bit_length()
        # 単位元で初期値をセットしているので葉がn個を超えても問題ない
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉(木の末端)にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 葉から親に向かって構築していく
        # ノード[i]の子供はノード[2*i]とノード[2*i+1]である
        # ノード[0]は存在しない
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        # k番目の値を更新
        k += self.num
        self.tree[k] ^= x
        while k > 1:
            # 共通の親を持つノードとのXORを計算する
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る(rは含まない)
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        # lとrが隣り合うまでノード[l]とノード[r-1]から遡る
        while l < r:
            # lが奇数の場合
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n,q=map(int,input().split())
A=list(map(int,input().split()))
st=SegTree(A, segfunc, ide_ele)
for i in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        st.update(x-1, y)
    else:
        res=st.query(x-1,y)
        print(res)
