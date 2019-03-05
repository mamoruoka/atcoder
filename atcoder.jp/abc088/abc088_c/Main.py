X=[]
for i in range(3):
    x=list(map(int,input().split()))
    X.append([x[0]-x[1],x[1]-x[2]])
    
if X[0]==X[1] and X[1]==X[2]:
    print('Yes')
else:
    print('No')