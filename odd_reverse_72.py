#https://www.guvi.in/codekata-level?level=hunter&set=8, 72
s = input()
l = len(s)
if s[l-1]=='.':
    s = s[:-1]
s = s.split()
for i in range(len(s)):
    if (i+1)%2!=0:
        s[i] = s[i][::-1]
k = ' '.join(x for x in s)
print(k)
