import itertools
import numpy as np
N = int(input())
anslist = list(map(int,input().split()))
count = 0
for v in itertools.combinations(anslist, 2):
  #print (v)
  count+=np.prod(v)
    
print (count)