a,b,k=map(int,input().split())

x=max(a,b)
y=min(a,b)
X=[]
for i in range(1,y+1):
    if a%i==0 and b%i==0:
        X.append(i)

X.sort(reverse=True)
print(X[k-1])