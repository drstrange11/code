n = int(input())
l = []
for i in range(n):
	l.append(input())
val = l[0]
l.remove(val)
length = len(val)
for i in l:
	while length > 0:
		if val in i:
			break
		length-=1
		val = val[:length]
print(val)
