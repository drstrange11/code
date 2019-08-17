#AJ_18
from collections import Counter      
string="kabali"

n=int(input())                    
k=[]
count=0
if  n>=1 and n<=1000:               
    for i in range(n):
        k.append((input()))

for val in k:
    if Counter(val)==Counter(string):     
        count=count+1
print(count)
