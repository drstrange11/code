n=int(input())
l1=list(map(int,input().split()))
c=1
l=[]
for i in l1:
  c=c*i
for i in l1:
  l.append(c//i)
print(*l)
