#AJ_25    
a2=int(input())
a3=input().split()
l=[]
for i in a3:
  l.append(i)
l.sort()
l.sort(key=len)
for i in l:
  print (i,end=' ')
