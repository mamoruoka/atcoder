from collections import Counter
n,k=map(int,input().split())

A=list(map(int,input().split()))

l=len(set(A))

mycounter=Counter(A)
X=mycounter.most_common()[::-1]
cnt=0
if l<=k:
    print(0)
else:
    for i in range(l-k):
        cnt+=X[i][1]
    print(cnt)