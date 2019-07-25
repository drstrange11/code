s=input()
a=len(s)
b=s[::-1]
if s==b:
  print(s[:a-1])
else:
  print(s)
