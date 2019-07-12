#Problem Link - https://www.guvi.in/codekata-level?level=pro&set=1 ,2
num,k = map(int,input().split())
num = list(str(num))
stack = []
for digit in num:
    while k>0 and stack and stack[-1]>digit:
        stack.pop()
        k-=1
    stack.append(digit)

while k>0:
    stack.pop()
    k-=1 
stack = ''.join(x for x in stack)
print(int(stack))
