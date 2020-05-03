x=int(input())
p=0
q=0
flag=True
for a in range(1000):
    if flag:
        B=abs(a**5-x)
        for i in range(int(B**(0.2))+1):
            if i**5==B:
                q=i
                p=a
                flag=False
                break
for a,b in [(p,q),(-p,q),(p,-q),(-p,-q),(q,p),(-q,p),(q,-p),(-q,-p)]:
    if a**5-b**5==x:
        print(a,b)
        break