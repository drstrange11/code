#68
n=int(input())
h=input()
h=h.split()
a=h.index(max(h))
b=h.index(min(h))
print(b+1,a+1)
