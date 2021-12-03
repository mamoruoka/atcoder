# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
        
    def sum(self, i):
        # 0-indexed
        s = 0
        while i >= 0:
            s += self.data[i]
            i = (i & (i+1)) -1
        return s
    
    def add(self, i, x):
        self.el[i] += x
        while i < self.n:
            self.data[i] += x
            i = i | (i+1)
    
    def lowerbound(self, s):
        x = -1
        y = 0
        for i in range(self.n.bit_length(), -1, -1):
            k = x + (1 << i)
            if k <= self.n and (y + self.data[k] < s):
                y += self.data[k]
                x += 1 << i
        return x + 1


input_count = 0
 
Q = int(input())
A = {}
N = 2**20
bit = BIT(N)

for i in range(N):
    bit.add(i, 1)

for q in range(Q):
    t, h = map(int,input().split())
    temp = (h%N) 

    # 値の更新
    if t==1:
        data = bit.el[temp]
        if data == 1:
            bit.add(temp ,-1)
            data = temp

        else:
            start = bit.sum(temp)
            data = bit.lowerbound(start+1)
            if data > N:
                data = bit.lowerbound(1)
            bit.add(data ,-1)

        A[data] = h

    # 指定個所の値出力
    else:
        if temp in A:
            print(A[temp])
        else:
            print(-1)
