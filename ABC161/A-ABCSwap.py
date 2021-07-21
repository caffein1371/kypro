# 問題文
# 3つの箱 A,B,Cがあります。それぞれの箱には、整数が 
# 1つ入っています。
# 現在、箱 A,B,Cに入っている整数はそれぞれ X,Y,Zです。
# これらの箱に対して以下の操作を順に行った後の、それぞれの箱に入っている整数を求めてください。

# 箱Aと箱 Bの中身を入れ替える箱 Aと箱 Cの中身を入れ替える

X,Y,Z = map(int,input().split())

temp = Y
Y = X
X = temp

temp = Z
Z = X
X = temp

print ("{} {} {}".format(X,Y,Z))