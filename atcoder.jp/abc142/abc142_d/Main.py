a,b=map(int,input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

s=gcd(a,b)
x=[]
while s%2==0:
    s//=2
    x.append(2)
f=3
while f*f<=s:
    if s%f==0:
        s//=f
        x.append(f)
    else:
        f+=2
if s!=1:
    x.append(s)
      
print(len(set(x))+1)