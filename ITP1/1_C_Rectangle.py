# 長方形の面積と周の長さ
# たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。

a,b = map(int,input().split())
print ("{} {}".format(a*b,a*2+b*2))