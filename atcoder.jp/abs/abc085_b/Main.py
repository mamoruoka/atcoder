n=int(input())


a=[int(input()) for i in range(n)]

a.sort(reverse=True)

count=1

for i in range(n-1):
    if(a[i]==a[i+1]):
        continue
    count+=1

print(count)