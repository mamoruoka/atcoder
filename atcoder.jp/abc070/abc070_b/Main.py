a,b,c,d=map(int,input().split())

if a<c:
    if b<=c:
        print(0)
    else:
        if b>d:
            print(d-c)
        else:
            print(b-c)
else:
    if a>d:
        print(0)
    else:
        if d>b:
            print(b-a)
        else:
            print(d-a)