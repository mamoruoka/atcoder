n=int(input())
X=[]
for i in range(n):
    X.append(input())

print('AC x '+str(X.count('AC')))
print('WA x '+str(X.count('WA')))
print('TLE x '+str(X.count('TLE')))
print('RE x '+str(X.count('RE')))
