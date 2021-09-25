N = int(input())
for i in range(1,100):
  if 2**i>N:
    print (i-1)
    quit()