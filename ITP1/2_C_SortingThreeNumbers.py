# 3 つの数の整列
# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。

a,b,c = map(int,input().split())
temp =0
if a>b:
    temp = a
    a = b
    b =temp
if b>c:
    temp = b
    b = c
    c = temp
if a>b:
    temp = a
    a = b
    b = temp
    
print ("{} {} {}".format(a,b,c))