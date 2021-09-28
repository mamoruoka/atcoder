import heapq
from collections import deque
q=int(input())
sort_list=[]
not_sort_list=deque([])
heapq.heapify(sort_list)
# ソートされた配列+まだソートされてない配列になるはず
for i in range(q):
    s = input().split()
    if s[0]=="1":
        not_sort_list.append(int(s[1])) 
        
    elif s[0]=="2":
        if len(sort_list)!=0:
            x = heapq.heappop(sort_list)
            print(x)
        else:
            x = not_sort_list.popleft()
            print(x)
    else:
        # まだソートされてない配列の中身をソートされた配列にする
        for it in not_sort_list:
            heapq.heappush(sort_list, it)
        not_sort_list = deque([])