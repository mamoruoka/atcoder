n,a,b=map(int,input().split())

x=n//(a+b)

if n-x*(a+b)>a:
    print(x*a+a)
else:
    print(x*a+n-x*(a+b))