h=int(input())

for i in range(50):
    if 2**i <= h and h<2**(i+1):
        ans=i
        break
print(2**(i+1)-1)