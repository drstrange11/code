n,m=map(eval,input().split())
a=[]
for k in range(n):
  a.append(list(map(eval,input().split())))
p=[]
o=[]
temp_o=[]
tt=[]
k=0
j=0
o.append(a[k][j])
p.append([k,j])
while [n-1,m-1] not in p:
  k=0
  for x in p:
    if x[0]+1<n and x[1]+1<m:
      temp_o.append(a[x[0]+1][x[1]]+o[k])
      temp_o.append(a[x[0]][x[1]+1]+o[k])
      tt.append([x[0]+1,x[1]])
      tt.append([x[0],x[1]+1])
    elif x[0]+1<n:
      temp_o.append(a[x[0]+1][x[1]]+o[k])
      tt.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp_o.append(a[x[0]][x[1]+1]+o[k])
      tt.append([x[0],x[1]+1])
    k+=1
  p=tt
  tt=[]
  o=temp_o
  temp_o=[]
print(max(o))
