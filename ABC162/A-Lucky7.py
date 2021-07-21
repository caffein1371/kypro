# ABC162
# 問題文
# 3桁の整数 Nが与えられます。Nのいずれかの桁に数字の 7は含まれますか？
# 含まれるなら Yes を、含まれないなら No を出力してください。

N = input()

flag = False
for i in range(len(N)):
  if N[i] =="7":
    flag =True
if flag:
  print ("Yes")
else :
  print ("No")