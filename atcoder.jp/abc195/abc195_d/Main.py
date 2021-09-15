import heapq
n,m,q=map(int,input().split())
Bu=[]
for i in range(n):
    w,v = map(int,input().split())
    Bu.append([w,v])
Bu.sort(key=lambda x:x[0])
X=list(map(int,input().split()))
Q=[]
for i in range(q):
    l,r=map(int,input().split())
    Y= X[:l-1] + X[r:]
    Y.sort()
    idx=0
    ans=0
    Z=[]
    heapq.heapify(Z)
    # 箱Y[i]よりも小さい荷物で最も価値のあるものをheapqで取りだす
    # 事前のBuのソートによって効率化している
    for i in range(len(Y)):
        while idx<n:
            if Bu[idx][0]<=Y[i]:
                heapq.heappush(Z, -Bu[idx][1])
                idx+=1
            else:
                break
        # 該当する荷物がない場合エラーとなる
        if len(Z)!=0:
            ans+=-1*heapq.heappop(Z)
    Q.append(ans)
for ans in Q:
    print(ans)




