s = input().split()
s = ''.join(x for x in s)
#print(set(s))
if len(set(s.lower()))==26:
    print('yes')
else:
    print('no')
