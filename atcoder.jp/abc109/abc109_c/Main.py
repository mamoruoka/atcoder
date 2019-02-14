n,x=map(int,input().split())

X=list(map(int,input().split()))

dif=[]
for i in range(n):
    dif.append(abs(X[i]-x))

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    if b>0:
        return gcd(b,a%b)
    else:
        return a

ans=dif[0]
for i in range(1,n):
    ans=gcd(ans,dif[i])

    
    
print(ans)