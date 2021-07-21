import math
a,b,C = map(float,input().split())

S = (1/2)*a*b*math.sin(math.radians(C))
c2 = a**2+b**2-2*a*b*math.cos(math.radians(C))
L = a+b+math.sqrt(c2)
h = (S/a)*2
print ('{:8f}'.format(S))
print ('{:8f}'.format(L))
print ('{:8f}'.format(h))