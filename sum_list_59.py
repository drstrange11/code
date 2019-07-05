#https://www.guvi.in/codekata-level?level=hunter&set=6, 59
n = int(input())
l = list(map(int,input().split()))
m = list(map(int,input().split()))
for i in range(len(l)):
    print(l[i]+m[i],end=" ")
    
