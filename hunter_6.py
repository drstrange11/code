n=input()
l = list(map(int,input().split()))
f = False
for i in l:
    if l.count(i) > 1:
        f = True
        break
print(i if f else "unique")
