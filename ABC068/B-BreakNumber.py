N = int(input())

for i in range(7,-1,-1):
  if N>=2**i:
    print (2**i)
    break