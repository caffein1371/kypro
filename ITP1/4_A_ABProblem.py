# 割り算
# ２つの整数 a と b を読み込んで、以下の値を計算するプログラムを作成して下さい：
# a ÷ b ： d (整数)
# a ÷ b の余り ： r (整数)
# a ÷ b ： f (浮動小数点数)

a,b = map(int,input().split())
print ("{} {} {:.10f}".format(a//b,a%b,a/b))