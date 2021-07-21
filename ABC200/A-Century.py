N = int(input())
#print (N/100)
if N/100-N//100 >=0.01:
  print (N//100+1)
else:
  print (N//100)