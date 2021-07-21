while True:
  n = str(input())
  if n =='-':
    break
  m = int(input())
  for i in range(m):
    h = int(input())
    temp = n[0:h]
    n = n[h:]+temp
  print (n)
    