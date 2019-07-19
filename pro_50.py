m,n=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
mod=10000000
f=0
for i in range(n):
  if l[i][0]==1:
    s=l[i][1]
    c=l[i][2]
    for j in range(i+1,n):
      if l[j][0]==s:
        s=l[j][1]
        c+=l[j][2]
    if c<mod and s==m:
      mod=c
      f+=1
if f==0:
  print(-1)
else:
  print(mod)
