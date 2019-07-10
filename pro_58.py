n = int(input())
l1 = []
val = n//2 + n
for i in range(1,n+1):
  if i%2==0:
    l1.append(i)
for i in range(1,n+1):
  if i%2!=0:
    l1.append(i)
for i in range(1,n+1):
  if i%2==0:
    l1.append(i)
print(val)
for x in l1:
    print(x,end=" ")
