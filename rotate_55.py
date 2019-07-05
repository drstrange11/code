#https://www.guvi.in/codekata-level?level=hunter&set=6, 60
n,d = map(int,input().split())
l = list(map(int,input().split()))
m = l.copy()
for i in range(len(l)):
    m[(i+(n-d))%n] = l[i]
for x in m:
    print(x,end=" ")

    
