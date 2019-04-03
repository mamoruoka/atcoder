s=input()
k=int(input())
X=[]
for i in range(len(s)):
    for j in range(k):
        X.append(s[i:i+j+1])
X=list(set(X))

X.sort()

print(X[k-1])