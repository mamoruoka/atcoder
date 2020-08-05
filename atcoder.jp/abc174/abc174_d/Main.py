n=int(input())
C=input()

r=C.count('R')
print(r-C[:r].count('R'))