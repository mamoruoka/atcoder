n,k=map(int,input().split())
A=list(map(int,input().split()))

if n==k:
    print(1)
else:
    if (n-k)%(k-1)!=0:
        print(int((n-k)/(k-1))+2)
    else:
        print(int((n-k)/(k-1))+1)