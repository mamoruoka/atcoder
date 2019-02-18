a,b=map(int,input().split())

s=b-a
count=0
for i in range(1,s+1):
    count+=i
print(count-b)   