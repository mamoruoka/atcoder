import itertools
n=int(input())
D={'M':0,'A':0,'R':0,'C':0,'H':0}
for i in range(n):
    x=input()
    if x[0]=='M':
        D['M']+=1
    elif x[0]=='A':
        D['A']+=1
    elif x[0]=='R':
        D['R']+=1
    elif x[0]=='C':
        D['C']+=1
    elif x[0]=='H':
        D['H']+=1

X=D.values()
Y=list(itertools.combinations(X,3))
cnt=0
for i in range(10):
    cnt+=Y[i][0]*Y[i][1]*Y[i][2]

print(cnt)
