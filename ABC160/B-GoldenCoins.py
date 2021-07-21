# ABC160
# 問題文
# 高橋君は金色の硬貨が好きです。自分が持っている 500円硬貨 1枚につき 1000、5円硬貨 1枚につき 5の 嬉しさ を得ます。

# 高橋君は X円を持っています。これを高橋君の嬉しさが最大になるように両替したとき、高橋君の嬉しさはいくらになりますか？
# (なお、利用できる硬貨は 500円玉、100円玉、50円玉、10円玉、5円玉、1円玉の 6種類とします。)

X = int(input())

sum = 0
gohyakumai =X//500
#print (gohyakumai)
sum = gohyakumai*1000
#print (sum)
goenmai = (X%500)//5
#print (goenmai)
sum = goenmai *5 +sum

print (sum)