n=int(input())
A=[]

for i in range(n):
    A.append(int(input()))

ind=0
cnt=1
while A[ind]!=2:
    ind=A[ind]-1
    cnt+=1
    if cnt>n:
        cnt=-1
        break

print(cnt)