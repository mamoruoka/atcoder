import itertools

n=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

X=[]

for i in range(n):
    X.append(i+1)
i=0
for v in itertools.permutations(X,n):
    i+=1
    if list(v)==P:
        p=i
    if list(v)==Q:
        q=i
print(abs(p-q))