import bisect
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans=0
for i in range(n):
    ans+=bisect.bisect_left(A,B[i])*(n-bisect.bisect_right(C,B[i]))
print(ans)