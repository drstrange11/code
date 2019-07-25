n=int(input())
li=list(map(int,input().split()))
u,v=map(int,input().split())
res=[]
for i in range(0,len(li)-1):
  for j in range(i+1,len(li)):
    subarr=li[i:j+1]
    if (subarr[0]==u and subarr[-1]==v) or (subarr[0]==v and subarr[-1]==u):
      res.append(len(subarr))
print(min(res)-1)
