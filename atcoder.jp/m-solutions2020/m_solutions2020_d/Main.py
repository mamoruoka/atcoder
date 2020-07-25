n=int(input())
B=list(map(int,input().split()))

m=1000
for i in range(n-1):
    if B[i]<B[i+1]:
        m=(m//B[i])*B[i+1]+m%B[i]
print(m)