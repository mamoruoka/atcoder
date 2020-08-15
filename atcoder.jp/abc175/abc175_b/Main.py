n=int(input())
L=list(map(int,input().split()))
cnt=0
L.sort()
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if L[i]==L[j] or L[i]==L[k] or L[j]==L[k]:
                continue
            if L[i]+L[j]>L[k]:
                cnt+=1
print(cnt)