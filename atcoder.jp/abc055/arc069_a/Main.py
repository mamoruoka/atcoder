n,m=map(int,input().split())

if n*2>=m:
    print(m//2)
else:
    x=m-n*2
    print(n+x//4)