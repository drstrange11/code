n=input()
flag=0
for i in range(0,len(n)-1):
  for j in range(i+1,len(n)):
    if n[i]<n[j]:
      flag=1
      print(n[j:])
      break
  if flag==1:
    break
else:
  print(n)
