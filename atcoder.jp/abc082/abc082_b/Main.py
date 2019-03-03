s=input()
t=input()
S=list(s)
S.sort()
x=''.join(S)
T=list(t)
T.sort(reverse=True)
y=''.join(T)

A=[x,y]

A.sort()

if A[0]==x and x!=y:
    print('Yes')
else:
    print('No')