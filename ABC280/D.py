def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

K = int(input())
import collections
c = collections.Counter(prime_factorize(K))
#print(c)

#ルジャンドルの定理 素数nをpの何乗で割れるかを返す
def legendre(n, p):
    res = 0
    p2 = p
    while True:
        tmp = n // p2
        if tmp == 0:
            break
        res += tmp
        p2 *= p
    return res

# 判定問題
def isok(n):
    for p, e in c.items():
        if legendre(n, p) < e:
            return False
    return True

import bisect

# 二分探索
ng, ok = 1, K  # k ≥ 2 なので 1! は k の倍数にならない、また k! は必ず k の倍数
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)