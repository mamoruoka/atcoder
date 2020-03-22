n,m=map(int,input().split())

if n>=2 and m>=2:
    print(n*(n-1)//2+m*(m-1)//2)
elif n<=1 and m>=2:
    print(m*(m-1)//2)
elif n>=2 and m<=1:
    print(n*(n-1)//2)
else:
    print(0)