from collections import defaultdict
n=int(input())
X=defaultdict(int)
for i in range(n):
    X[input()]+=1
print(len(X))