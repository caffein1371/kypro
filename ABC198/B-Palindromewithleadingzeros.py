N = input()

nList = N.rstrip('0')
if nList == nList[::-1]:
  print ("Yes")
else:
  print ("No")