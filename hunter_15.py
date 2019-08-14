#15
n=int(input())
l=list(map(int, input().split()))[:n]
m=max(l)
l1=[]
for i in range(0,len(l)):
    k=l[i:]
    inter=max(k)
    if(l[i]==inter):
        l1.append(l[i])
print(*l1)
print(m)
