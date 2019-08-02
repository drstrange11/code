#51
n=int(input())
l=list(map(int,input().split()))
l2=[]
c=1
for i in range(n):
  val=l[i:]
  ans=len(val)
  for j in range(ans-1):
    if val[j]>0 and val[j+1]<0:
      c+=1
    elif val[j]<0 and val[j+1]>0:
      c+=1
    else:
      break
  l2.append(str(c))
  c=1
print(''.join(l2))
