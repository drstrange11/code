#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=14

n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
le = len(l)
ne = []
for i in range(le//2+1):
    ne.append(l[i])
    ne.append(l[le-i-1])
for x in ne[:len(ne)-1]:
    print(x,end=" ")
