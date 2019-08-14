#19
l=list(map(int,input().split()))
n=int(l[0])
k=int(l[1])
l1=[]
for i in range(0,n):
    l1.append(input().split())
s=set(l1[0])
for i in l1:
    s=s & set(i)
m=list(s)
m.sort()
print(*m)
