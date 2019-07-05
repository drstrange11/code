#https://www.guvi.in/codekata-level?level=hunter&set=6, 57
n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(len(l)):
    s^=l[i]
print(s)
    
    
