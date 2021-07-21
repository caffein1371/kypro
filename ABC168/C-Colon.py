# ABC168
# 問題文
# 時針と分針の長さがそれぞれ Aセンチメートル、Bセンチメートルであるアナログ時計を考えます。
# 時針と分針それぞれの片方の端点は同じ定点に固定されており、この点を中心としてそれぞれの針は一定の角速度で時計回りに回転します。時針は 
# 12時間で、分針は 1時間で 1周します。
# 0時ちょうどに時針と分針は重なっていました。ちょうど H時 M分になったとき、
# 2本の針の固定されていない方の端点は何センチメートル離れているでしょうか。

import math
 
A,B,H,M = map(int,input().split())
 
degree = 0
minute = 6*M
hour=30*H+0.5*M
if abs(minute-hour)>=180:
  degree = 360-abs(minute-hour)
else :
  degree = abs(minute-hour)
#print (degree)
#print (math.degrees(degree))
#print (math.cos(math.radians(degree)))
 
c=A**2+B**2-2*A*B*math.cos(math.radians(degree))
print (math.sqrt(c))