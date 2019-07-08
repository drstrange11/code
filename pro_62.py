a=str(input())
b=len(a)
c=[]

for i in range(0,b):
    for j in range(i+1,b):
        c.append(a[i:j+1])
max=1
d=[]
for i in c:
    if(i==i[::-1]):
        d.append(i)
d.sort(key=len)
d=d[::-1]
print(len(a)-len(d[0]))
