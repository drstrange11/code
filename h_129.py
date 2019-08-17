#AJ_129
n=int(input())
l=[int(i) for i in input().split()]
n2=0
for i in range(0,len(l)):
    if l.count(l[i])>n2:
        n2=l.count(l[i])
        a=l[i]
print(a)
