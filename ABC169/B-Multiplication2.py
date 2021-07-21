# ABC169
# 問題文
# N個の整数 A1,...,ANが与えられます。
# A1×...×ANを求めてください。
# ただし、結果が 10^18を超える場合は、代わりに -1 を出力してください。

#import numpy as np

N = int(input())
Alist = list(map(int,input().split()))

#ans = np.prod(Alist)
Alist.sort()
ans = 1
for i in range(N):
  #print (Alist[i])
  ans*= Alist[i]
  if Alist[i]==0:
    break
  if ans >10**18:
    break

if ans >10**18:
  print(-1)
else:
  print(ans)