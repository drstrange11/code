#26
m=int(input())
n=list(map(int,input().split()))
l=[]
p=1
for i in n:
  if i not in l:
    l.append(i)
for i in range(len(l)-1):
  if (l[i]<l[i+1]):
    p+=1
print(p)
