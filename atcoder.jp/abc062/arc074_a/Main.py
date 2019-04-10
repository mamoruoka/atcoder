import math

h,w=map(int,input().split())

R=[]

def func(h,w):
    for i in range(1,h+1):
        s1=i*w
        s2=(h-i)*(math.ceil(w/2))
        s3=(h-i)*(w//2)
        R.append(max(s1,s2,s3)-min(s1,s2,s3))
        
        s2=(math.ceil((h-i)/2))*w
        s3=((h-i)//2)*w
        R.append(max(s1,s2,s3)-min(s1,s2,s3))
    return min(R)

print(min(func(h,w),func(w,h)))