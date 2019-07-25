s=int(input())
n2=list(map(int,input().split()))
l=[]
l.append(sum(n2))
for i in range(0,s-1):
  a,a1=n2[:i+1],n2[i+1:]
  if sum(a)>sum(a1):
    l.append(sum(a))
  else:
    l.append(sum(a1))
print(max(l))
