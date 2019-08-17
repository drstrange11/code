#AJ_124
n=int(input())
l=[]
for i in range(0,n):
    for j in range(i,n):
        l.append("1")
    print(*l)
    l.clear()
