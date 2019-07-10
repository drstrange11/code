a,b = input().split()
l=0
i=0
if len(a)>len(b):
  a,b=b,a
while i<len(a):
  l+=(ord(b[i])-ord(a[i]))
  i+=1
for i in range(i,len(b)):
  l += ord(b[i])-ord('a')+1
print(l)
