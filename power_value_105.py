#Problem Link - https://www.guvi.in/codekata-level?level=hunter&set=11, 105


n = int(input())
l = list(int(x) for x in str(n))
po = len(l)
fin = list(map(lambda x:x**po,l))
print(sum(fin))
