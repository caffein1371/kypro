N = input()
number = sum([int(N[i]) for i in range(len(N))])
if int(N)%number==0:
  print ('Yes')
else:
  print ('No')