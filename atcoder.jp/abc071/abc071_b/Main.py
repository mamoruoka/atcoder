s=input()

L=list(s)

X=[0]*150
for i in L:
    X[ord(i)]+=1

ans='None'
for j in range(97,123):
    if X[j]==0:
        ans=chr(j)
        break

print(ans)