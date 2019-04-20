s=input()
ans=''
for i in range(6):
    ans+=str(s.count(chr(i+65)))+' '
ans=ans[:-1]
print(ans)