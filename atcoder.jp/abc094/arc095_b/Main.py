n=int(input())
A=list(map(int,input().split()))
 
a=max(A)
 
B=[]
 
for i in range(n):
    if A[i]==a:
        B.append(a)
    else:
    	B.append(abs(A[i]-a/2))
 
ind=B.index(min(B))
 
b=A[ind]
 
print(a,b)