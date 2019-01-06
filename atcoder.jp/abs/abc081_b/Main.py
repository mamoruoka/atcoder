n=int(input())

a = [int(i) for i in input().split()] 


list=[]

for j in range(n):
    count=0
    while True:
        if(a[j]==0 or a[j]%2==1):
            break
        a[j]=a[j]/2
        count+=1

    list.append(count)
    
print(min(list))