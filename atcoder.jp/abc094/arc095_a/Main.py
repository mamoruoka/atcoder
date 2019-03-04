n=int(input())

X=list(map(int,input().split()))
sort_X=sorted(X)
for i in range(n):
    if X[i]<sort_X[int(n/2)]:
        print(sort_X[int(n/2)])
    else:
        print(sort_X[int(n/2)-1])