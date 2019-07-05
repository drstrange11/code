#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=12,111
n = int(input())
l =[]
for i in range(n):
    k = list(map(int,input().split()))
    l.append(k)
s = 0
for i in range(n):
    s+= l[i][i]
print(s)
