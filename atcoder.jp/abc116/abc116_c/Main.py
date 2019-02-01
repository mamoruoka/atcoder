n = int(input())
h=[0]+list(map(int,input().split()))


count=0
for i in range(n):
    if(h[i+1]-h[i]>0):
        count+=(h[i+1]-h[i])
    
    
print(count)  