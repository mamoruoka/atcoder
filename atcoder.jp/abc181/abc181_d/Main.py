import  itertools
s=input()
X=[0]*10
ans='No'
for i in s:
    if X[int(i)]>=3:
        continue
    X[int(i)]+=1
M=[]
for i in range(1,10):
    for j in range(X[i]):
        M.append(i)

if len(M)>=3:
    Y=list(itertools.permutations(M,3))

    for y in Y:
        if int(y[0]*100+y[1]*10+y[2])%8==0:

            ans='Yes'
elif len(M)==2:
    if (M[0]*10+M[1])%8==0 or (M[1]*10+M[0])%8==0:
        ans='Yes'
else:
    if M[0]==8:
        ans='Yes'

print(ans)


