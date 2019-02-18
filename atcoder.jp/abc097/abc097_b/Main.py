x=int(input())
count=0
for i in range(1,32):
    for j in range(2,10):
        s=i**j
        if s<=x and s>count:
            count=s
print(count)