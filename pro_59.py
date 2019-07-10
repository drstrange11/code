#Bar-split
s = input()
s1 = input()
bar = s.index("|")
l1 = s[:bar]
l2 = s[bar+1:]
a = l1+s1
b = l2+s1
if len(l1) == len(b):
	val = l1 + "|" + l2 + s1
	print(val)
elif len(l2) == len(a):
	val = l1 + s1 +"|"+ l2
	print(val)
else:
	print("Impossible")
