n=int(input())


L=[3,5,7]

def dfs(s):
    count=0
    for i in L:
        p=s*10+i
        if p<=n:
            if set([int(j) for j in str(p)])==set(L):
                count+=dfs(p)+1 #条件を満たしているので+1
            else:
                count+=dfs(p)
    return count

print(dfs(0))