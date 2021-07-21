# ABC170
# 問題文
# 庭に何匹かの動物がいます。これらはそれぞれ、
# 2本の足を持つ鶴か 4本の足を持つ亀のいずれかです。
# 高橋くんは、「庭の動物の総数は X匹で、それらの足の総数は 
# Y本である」と発言しています。この発言が正しいような鶴と亀の数の組合せが存在するか判定してください。

X,Y = map(int,input().split())

turtle_leg = 4
crane_leg = 2

for i in range(X+1):
  if Y == turtle_leg*i+crane_leg*(X-i):
    print ("Yes")
    break
  if i==X:
    print ("No")
    break