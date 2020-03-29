x,y,a,b,c=map(int,input().split())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
R=list(map(int,input().split()))
P.sort(reverse=True)
P=P[:x]
Q.sort(reverse=True)
Q=Q[:y]
P=P+Q
P.sort()
R.sort(reverse=True)
for i in range(min(x+y,c)):
    if P[i]<R[i]:
        P[i]=R[i]
    else:
        break
print(sum(P))