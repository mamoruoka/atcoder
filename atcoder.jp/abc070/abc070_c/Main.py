n=int(input())
T=[]
for i in range(n):
    T.append(int(input()))
    
def gcd(a,b):
    while b:
        a,b=b, a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

T=list(set(T))
cnt=0
x=1
while True:
    x=lcm(x,T[cnt])
    cnt+=1
    if cnt==len(T):
        break

print(x)