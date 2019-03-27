import math

n,m=map(int,input().split())

if n==m+1 or n==m-1:
    print((math.factorial(m)*math.factorial(n))%(10**9+7))
elif n==m:
    print((2*(math.factorial(m)**2))%(10**9+7))
else:
    print(0)