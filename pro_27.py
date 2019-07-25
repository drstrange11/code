#27
n,m=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
t=[]
c=0
for i in range(n):
    x=v[i]/p[i]
    t.append(x)
while m>=0 and len(t)>0:
    mindex=t.index(max(t))
    if m>=p[mindex]:
        c=c+v[mindex]
        m=m-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)
print(c)
