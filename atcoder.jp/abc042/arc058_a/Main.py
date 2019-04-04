n,k=map(int,input().split())

D=set(map(int,input().split()))

X={0,1,2,3,4,5,6,7,8,9}-D

for i in range(n,100000):
    if set([int(a) for a in str(i)])|X==X:
        print(i)
        break