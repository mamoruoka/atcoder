n=int(input())
X=[]
for i in range(n):
    X.append(input())
    
for i in range(n-1):
    if n!=len(set(X)):
        print('No')
        break
    
    if X[i][len(X[i])-1]!= X[i+1][0]:
        print('No')
        break
    
    if i==n-2:
        print('Yes')