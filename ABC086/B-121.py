import math
def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False
a,b = map(str,input().split())

num = int(a+b)
if is_integer_num(math.sqrt(num))== True:
  print ('Yes')
else:
  print ('No')