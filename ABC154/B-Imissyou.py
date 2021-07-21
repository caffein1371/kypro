# ABC154
# 問題文
# 文字列 Sが与えられます。Sのすべての文字を x で置き換えて出力してください。

S = input()

sdash = []
for i in range(len(S)):
  sdash.append("x")
print (''.join(sdash))