n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
X=[a,b,c,d,e]
p=min(X)
if n%p==0:
    cnt=n//p+4
else:
    cnt=n//p+5 
    
print(cnt)