n,m=map(int,input().split())
A=list(map(int,input().split()))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

Done=[False]*(max(A)+1)
Y=[True]*(m+1)
for a in A:
    # 素因数分解
    Z=prime_factorize(a)
    for z in Z:
        if Done[z]:
            continue
        Done[z]=True
        for i in range(z,m+1,z):
            Y[i]=False
                
ans=0
ANS=[]
for i in range(1,m+1):
    if Y[i]:
        ANS.append(i)
        ans+=1
print(ans)
for ans_ in ANS:
    print(ans_)