n=int(input())

a=input()
b=input()
c=input()

count=0
for i in range(n):
    if(a[i]==b[i] and b[i]==c[i]):
        continue
    elif(a[i]==b[i] and b[i]!=c[i]):
        count+=1
    elif(a[i]!=b[i] and b[i]==c[i]):
        count+=1
    elif(a[i]==c[i] and b[i]!=c[i]):
        count+=1
    elif(a[i]!=b[i] and c[i]!=b[i]):
        count+=2

print(count)