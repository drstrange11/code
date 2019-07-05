#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11 -109


n = int(input())
l = list(input().split())
l = [x.lower() for x in l]
l.sort()
for x in l:
    print(x)
