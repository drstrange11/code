#
s = input()
s = list(set(s))
s.sort()
s = ''.join(x for x in s)
print(s)
