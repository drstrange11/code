#93
N=input()
temp=""
k=0
for i in range(len(N)):
  if N[i]==" ":
    temp+=N[i]
  elif k==0:
    temp+=N[i].upper()
    k=1
  elif k==1:
    temp+=N[i]
    k=0
print(temp)
