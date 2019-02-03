n=int(input())
X=list(map(int,input().split()))

max_x=max(X)
if max_x<(sum(X)-max_x):
    print('Yes')
else:
    print('No')