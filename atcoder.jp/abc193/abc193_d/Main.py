import copy
K=int(input())
S=input()
T=input()

s_cnt=0
t_cnt=0

Sm=[0]*10
Tm=[0]*10
for i in range(4):
    Sm[int(S[i])]+=1
    Tm[int(T[i])]+=1
    
for i in range(1,10):
    s_cnt+=i*(10**Sm[i])
    t_cnt+=i*(10**Tm[i])

ans=0
for si in range(1,10):
    for ti in range(1,10):
        if si!=ti:
            if Sm[si]+1+Tm[si]>K:
                continue
            if Sm[ti]+Tm[ti]+1>K:
                continue
        else:
            if Sm[si]+2+Tm[si]>K:
                continue
        x=copy.copy(s_cnt)
        x+=si*(10**(Sm[si]+1)-10**Sm[si])

        y=copy.copy(t_cnt)
        y+=ti*(10**(Tm[ti]+1)-10**Tm[ti])
        
        if x>y:
            bunbo=(K*9-8)*(K*9-9)
            if si!=ti:
                bunsi=(K-Sm[si]-Tm[si])*(K-Sm[ti]-Tm[ti])
            else:
                bunsi=(K-Sm[si]-Tm[si])*(K-Sm[si]-Tm[si]-1)
            ans+=bunsi/bunbo


print(ans)

        