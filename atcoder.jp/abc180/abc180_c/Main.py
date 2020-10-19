n=int(input())
ans=[]
for i in range(1,int(n**0.5)+1):
  if i*i!=n:
    if n%i==0:
      ans.append(i)
      ans.append(n//i)
  else:
    ans.append(i)
ans.sort()
for a in ans:
  print(a)