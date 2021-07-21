# 問題文
# 文字列 
# S, Tが与えられます。次の操作を繰り返して Sを Tに変更するとき、操作回数の最小値を求めてください。
# 操作：
# Sの 1文字を選んで別の文字に書き換える

S = input()
T = input()

count = 0
for i in range(len(S)):
  if S[i]!=T[i]:
    count+=1
print (count)