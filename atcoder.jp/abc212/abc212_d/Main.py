import heapq

q=int(input())
X=[]
Y=0
heapq.heapify(X)
for _ in range(q):
    s=input().split()
    if s[0]=="1":
        x=int(s[1]) - Y
        heapq.heappush(X, x)
    elif s[0]=="2":
        # 袋の中の玉に全てxを足すことは、次に入る玉にxを引くことに等しい(この操作を行っても袋の中の大きさの順序は変わらない)
        x=int(s[1])
        Y+=x
    else:
        print(heapq.heappop(X)+Y)
