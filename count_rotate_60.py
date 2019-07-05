#https://www.guvi.in/codekata-level?level=hunter&set=6, 60
n = int(input())
l = list(map(int,input().split()))
m = list(map(int,input().split()))
ind1 = 1 
ind2 = m.index(l[1])
if ind1-ind2<0:
    print((ind1-ind2+n)%n)
else:
    print(ind1-ind2)

    
