n=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
Alice=[A[i] for i in range(0,n,2)]
Bob=[A[j] for j in range(1,n,2)]
print(sum(Alice)-sum(Bob))
