n=int(input())
l=list(map(int,input().split()))
p=0
q=0
l.sort(reverse=True)
for i in l:
  m=p+i
  if q>m:
    p=m
  else:
    p=q
    q=m
print(p,q)
