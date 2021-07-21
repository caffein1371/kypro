# 円の面積と円周
# 半径 r の円の面積と円周の長さを求めるプログラムを作成して下さい。

import math
r = float(input())
print ("{:.12f} {:.12f}".format(r*r*math.pi,2*r*math.pi))