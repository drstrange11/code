#28
n=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
c1=0
for i in range(len(l)):
    if l[i]>=s:
        c1=c1+1
    s=s+l[i]
print(c1)
