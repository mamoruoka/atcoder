import bisect
from array import array
 
L,Q = map(int,input().split())
l = array('i', [0,L])
 
for i in range(Q):
  c,x = map(int,input().split())
  if c == 1:
    # lにxを挿入して、さらにsortされた形にできる？
    bisect.insort(l,x)
  else:
    # 二分探索によりxの位置を測る
    pos = bisect.bisect_left(l,x)
    print(l[pos]-l[pos-1])
