n,c,k=map(int,input().split())

x=[]
for i in range(n):
    x.append(int(input()))
        
    
x.sort()

count=1

bus_count=0

for j in range(n-1):
    bus_count+=1
    if(x[j+1-bus_count]+k<x[j+1] or bus_count==c):
        count+=1
        bus_count=0
        
print(count)