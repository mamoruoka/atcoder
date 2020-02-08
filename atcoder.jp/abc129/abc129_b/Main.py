n=int(input())
w=list(map(int,input().split()))
s=sum(w)
s1=w[0]
s2=s-w[0]
x=[]
x.append(abs(s1-s2))
for i in range(n-2):
    s1+=w[i+1]
    s2-=w[i+1]
    x.append(abs(s1-s2))
print(min(x))