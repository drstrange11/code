n=int(input())
l=list(map(int,input().split()))[:n]
t=[]
for i in range(0,n):
  if l[i]%2==0 and i%2==1 or l[i]%2==1 and i%2==0:
    t.append(l[i])
print(*t,end="")
