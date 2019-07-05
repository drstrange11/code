#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11


n = int(input())
l = list(int(x) for x in str(n))
fin = list(map(lambda x:x*x,l))
print(sum(fin))
