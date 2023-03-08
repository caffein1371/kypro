##########################################
import io
import sys

_INPUT = """\
999



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
n = int(input())
ans = 0
for i in range(1,n+1):
        ans+=i

n = ans
#n =int(input("n以下の素数と個数を表示。n="))
p = [i for i in range(n + 1)]

for i in p[3:]:
     if p[i] % 2 == 0:
          p[i] = 0

root_n = n ** 0.5
for i in range(3, n):
     if i > root_n:
          break
     if p[i] != 0:
          for j in range(i, n + 1, 2):
               if i * j >= n + 1 :
                    break
               p[i * j] = 0

# print(set(p))
# print(list(set(p)))
# print(sorted(list(set(p))))

plist = sorted(list(set(p)))[2:]
plistn = str(len(plist))+'個'

# print(plist)
# print(plistn)
if n in plist:
        print ('WANWAN')
else:
        print ('BOWWOW')