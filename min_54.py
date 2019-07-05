#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=6, 54
n = int(input())
l = list(map(int,input().split()))
for i in range(len(l)):
    if i==len(l)-1:
        print(min(l[:i+1]))
    else:
        print(min(l[:i+1]),end=" ")
    
