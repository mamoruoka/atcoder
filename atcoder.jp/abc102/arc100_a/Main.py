n=int(input())

X=list(map(int,input().split()))
Y=[]
for i in range(n):
    Y.append(X[i]-(i+1))
Y.sort()
res_1=0

if n%2==1:
    m=Y[int((n-1)/2)]
    for j in range(n):
        res_1+=abs(Y[j]-m)
else:
    m=(Y[int(n/2)-1]+Y[int(n/2)])//2
    for j in range(n):
        res_1+=abs(Y[j]-m)
        

        
print(res_1)
