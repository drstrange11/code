#AJ_12
n,s=map(int,input().split())

l=list(map(int,input().split()))
for i in range(s):
    l=[l[-1]]+l[:-1]
print(*l,end=" ")
