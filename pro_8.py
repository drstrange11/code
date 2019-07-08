#GCD
import math
l=[]
a,b=map(int,input().split())
l1=list(map(int,input().split()))
for i in range(b):
    m,n=map(int,input().split())
    l.append([m,n])
for j in l:
     val1=j[0]-1
     val2=j[1]-1
     print(math.gcd(l1[val1],l1[val2]))
