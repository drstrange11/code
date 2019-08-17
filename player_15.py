#AJ_15
n=input()
g=0
for i in n:
   if n.count(i)>g:
      g=n.count(i)
      ans=i
print(ans)
