# ABC095
# 問題文
# ファーストフードチェーン「ピザアット」のメニューは「A ピザ」「B ピザ」「AB ピザ」の 
# 3種類です。A ピザと B ピザは全く異なるピザで、これらをそれぞれ半分に切って組み合わせたものが AB ピザです。A ピザ、B ピザ、AB ピザ 1枚あたりの値段はそれぞれA円、B円、C円です。
# 中橋くんは、今夜のパーティーのために A ピザ X枚と B ピザY枚を用意する必要があります。これらのピザを入手する方法は、AピザやBピザを直接買うか、AB ピザ2枚を買って A ピザ1枚と B ピザ1枚に組み替える以外にはありません。このためには最小で何円が必要でしょうか？なお、ピザの組み替えにより、必要な量を超えたピザが発生しても構いません。


A,B,C,X,Y = map(int,input().split())
temp= A*X+B*Y
maisu = 0
nokori = 0
#print (temp)
betsu = 0
if X>Y:
  maisu =Y
  nokori=(X-Y)*A
  betsu = X*2*C
else :
  maisu =X
  nokori =(Y-X)*B
  betsu = Y*2*C
ans = maisu*2*C+nokori if maisu*2*C+nokori<temp else temp
ans = ans if ans<=betsu else betsu
print (ans)