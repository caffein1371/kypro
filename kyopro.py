##########################################
import io
import sys

_INPUT = """\
11



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
n = int(input())
#n =int(input())
#nまでの値をpに格納
p = [i for i in range(n)]
#2以降の倍数を0で初期化
for i in p[3:]:
     if p[i] % 2 == 0:
         p[i] = 0
#調べたい値の平方根を求める
root_n = n ** 0.5
#平方根以下の値
for i in range(3, n):
     if i > root_n:
          break
     if p[i] != 0:
          for j in range(i, n , 2):
               if i * j >= n :
                    break
               p[i * j] = 0
#0が入っているものは１つになる
#[2:]で0,1が消える
plist = sorted(list(set(p)))[2:]
plistn = len(plist)

#print(plist)
print(plistn)