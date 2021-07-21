# ABC176
# 問題文
# 整数 Nが 9の倍数であることと、
# Nを十進法で表したときの各桁の数の和が 
# 9の倍数であることは同値です。

# Nが 9の倍数であるか判定してください。

N = list(input())
 
n = 0
for i in range(len(N)):
  n+=int(N[i])
if n%9 ==0:
  print ("Yes")
else:
  print ("No")