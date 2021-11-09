from collections import defaultdict
import math
from itertools import combinations
n=int(input())
X=[]
for i in range(n):
    x,y=map(int,input().split())
    X.append([x,y,i])
A=defaultdict(int)
ans=0

for p1, p2 in combinations(X, 2):
    #傾きの最小単位をリストに加えたい
    z = math.gcd(p1[1]-p2[1], p1[0]-p2[0])
    z1 = (p1[1]-p2[1])//z
    z2 = (p1[0]-p2[0])//z
    if z2==0:
        A[10**10]+=1
    else:
        A[z1/z2]+=1

print(len(A)*2)


