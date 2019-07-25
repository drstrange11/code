l = input().split()
for i in range(len(l)):
    l[i] = l[i][::-1]
l = ' '.join(x for x in l)
print(l)
