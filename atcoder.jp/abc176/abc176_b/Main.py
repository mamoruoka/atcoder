n=input()
X=[int(s) for s in n]
if sum(X)%9==0:
    print('Yes')
else:
    print('No')