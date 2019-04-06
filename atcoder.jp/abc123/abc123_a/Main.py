import itertools 
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
X=[a,b,c,d,e]
S=list(itertools.combinations(X,2))
ans='Yay!'
for i in range(len(S)):
    if abs(S[i][0]-S[i][1])>k:
        ans=':('
print(ans)