#Pro_34
a,b = map(int,input().split())
cost=0
l = []
for i in range(a):
      l.append(input())
for i in range(a):
      for j in range(b-1):
            if l[i][j] != 'R' and l[i][j+1] != 'R' :
                  cost+=3
            elif l[i][j] != 'G' and l[i][j+1] != 'G':
                  cost+=5
print(cost)
