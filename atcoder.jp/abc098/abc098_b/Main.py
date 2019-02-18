n=int(input())

s=input()

count=0

for i in range(n-1):
    s1=s[:i+1]
    s2=s[i+1:]  
    seki=set(s1) & set(s2)
    if len(seki)>count:
        count=len(seki)

print(count)