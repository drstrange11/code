#AJ_12
n=int(input())
temp=n
r=0
while(n>0):
  s=n%10
  r=r*10+s
  n=n//10
if temp==r:
  print("yes")
else:
  print("no")
