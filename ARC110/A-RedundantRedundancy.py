import math
from functools import reduce

def lcm(x,y):
  return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

N = int(input())

anslist = [i for i in range(2,N+1)]
  
#print (anslist)
L = lcm_list(anslist)
print (L+1)