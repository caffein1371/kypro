##########################################
import io
import sys

_INPUT = """\
7
3 4 6 7 8 9 10








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Xlist = list(map(int,input().split()))
import functools
import math
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime
prime = []
Y = sieve_of_eratosthenes(50)
for p in range(len(Y)):
    if Y[p]:
        prime.append(p)
ans = []
for i in range(len(Xlist)):
    for j in range(len(prime)):
        if Xlist[i]%prime[j]==0:
            ans.append(prime[j])
            break
#print(ans)

import math
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)
print (my_lcm(*ans))
