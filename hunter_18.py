#18
n=int(input())
l1,l2=[],[]
c=0
for i in range(0,n):
  l1.append(list(map(int,input().split())))
for i in range(0,n+2):
  if i==0:
    l2.append([0]*(n+2))
  elif i==(n+2)-1:
    l2.append([0]*(n+2))
  else:
    l2.append([0]+l1[i-1]+[0])
for i in range(0,len(l2)):
    for j in range(0,len(l2)):
      if l2[i][j]!=0 and n%2==0:
        if l2[i-1][j-1]==0 and l2[i-1][j]==0 and l2[i-1][j+1]==0 and l2[i][j-1]==0 and l2[i][j+1]==0 and l2[i+1][j-1]==0 and l2[i+1][j]==0 and l2[i+1][j-1]==0:
            c+=1
      elif l2[i][j]!=0 and n%2!=0:
        if l2[i][j-1]==0 and l2[i][j+1]==0 and l2[i-1][j]==0 and l2[i+1][j]==0:
            c+=1
print(c)
