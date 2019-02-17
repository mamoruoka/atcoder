import itertools

n=int(input())

count=0

X=[3,5,7,11,13]

X=list(itertools.combinations(X,3))



for i in range(10):
    if X[i][0]*X[i][1]*X[i][2]<=n:
        count+=1

if n<135:
    count+=0
elif n<189:
    count+=1
else:
    count+=2
        
print(count)