n=input()
X=[int(i) for i in n]
s=sum(X)

MOD=[0]*3
for i in n:
    MOD[int(i)%3]+=1

if s%3==0:
    print(0)
elif s%3==1:
    if MOD[1]>=1 and len(n)>=2:
        print(1)
    elif MOD[2]>=2 and len(n)>=3:
        print(2)
    else:
        print(-1)
else:
    if MOD[2]>=1 and len(n)>=2:
        print(1)
    elif MOD[1]>=2 and len(n)>=3:
        print(2)
    else:
        print(-1)