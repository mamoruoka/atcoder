a,b,c,k=map(int,input().split())
if a>=k:
    print(k)
elif a<=k<=a+b:
    print(a)
elif a+b<=k<=a+b+c:
    print(a-(k-a-b))
else:
    print(a-c)