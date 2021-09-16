import queue
n,Q=map(int,input().split())
X=[[]for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    X[a-1].append(b-1)
    X[b-1].append(a-1)

q=queue.Queue()
Flag=[True]*n
Reached=[False]*n
q.put([0,True])
while not q.empty():
    idx, flag = q.get()
    Reached[idx]=True
    Flag[idx]=flag
    for i in X[idx]:
        if not Reached[i]:
            if flag:
                q.put([i, False])
            else:
                q.put([i, True])
ANS=[]
for i in range(Q):
    c,d=map(int,input().split())
    if Flag[c-1] == Flag[d-1]:
        ANS.append("Town")
    else:
        ANS.append("Road")

for ans in ANS:
    print(ans)