#93
N=input()
temp=""
k=0
for i in range(len(N)):
  ik N[i]==" ":
    temp+=N[i]
  elik k==0:
    temp+=N[i].upper()
    k=1
  elik k==1:
    temp+=N[i]
    k=0
print(temp)
