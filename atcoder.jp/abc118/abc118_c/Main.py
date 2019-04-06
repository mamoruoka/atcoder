n=int(input())
X=list(map(int,input().split()))
x=X[0]
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a


for i in range(1,n):
    x=gcd(x,X[i])
if x!=1:
    print(x)
else:
    print(1)
