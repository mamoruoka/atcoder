n,k=map(int,input().split())
if k%2!=0:
    count=int(n/k)
    print(count**3)
else:
    x=int(n/k)
    y=int(2*n/k)-x
    print(x**3+y**3)