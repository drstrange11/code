import string
s1 = input()
s2 = input()
s3 = string.ascii_lowercase
l = []
for i in range(0, len(s1)) :
    k = ord(s1[i]) + s3.index(s2[i]) + 1
    if k > ord('a')+25 :
        k -= 26
    l.append(chr(k))
s4 = ''.join(l)
print(s4)
