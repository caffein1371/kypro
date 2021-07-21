# 2 つの数の交換
# ２つの整数 x, y を読み込み、それらを値が小さい順に出力するプログラムを作成して下さい。
# ただし、この問題は以下に示すようにいくつかのデータセットが与えられることに注意して下さい。

while True:
    x,y = map(int,input().split())
    if x==0 and y==0:
        break
    temp =0
    if x>y:
        print ("{} {}".format(y,x))
    else:
        print ("{} {}".format(x,y))
    