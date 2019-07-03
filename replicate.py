#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=1

n = int(input())
l = list(map(int,input().split()))
l.sort()
m = []
for i in range(len(l)-1):
    if l[i]==l[i+1]:
        m.append(l[i])
for x in set(m):
    print(x,end=" ")
