n=int(input())
k=[]
for i in range(0,n):
   l=list(map(int,input().split()))
   k.append(l)
s=0
for i in range(0,n):
   for j in range(0,n):
      if i+j==n-1:
         s=s+k[i][j]
print(s)
