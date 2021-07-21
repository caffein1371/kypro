# ABC147
# 問題文
# 3個の整数A1,A2,A3が与えられます。
# A1+A2+A3が22以上なら bust、
# 21以下なら win を出力してください。

A1,A2,A3 = map(int,input().split())
 
if A1+A2+A3>=22:
  print ('bust')
else:
  print ('win')