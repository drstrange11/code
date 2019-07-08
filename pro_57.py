#pro_57
import sys
s1, s2 = input().split()
l = len(s1)
for j in range(1,0,-1) :
    for i in range(0,l-j) :
        li, ri = i,j+i
        s3 = s1[li:ri + 1]
        if s3 in s2 :
            print('yes')
            sys.exit()
print('no')
