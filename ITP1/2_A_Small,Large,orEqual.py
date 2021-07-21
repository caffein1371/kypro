# 大小関係
# ２つの整数 a, b を読み込んで、a と b の大小関係を出力するプログラムを作成して下さい。

a,b = map(int,input().split())

if a>b:
    print ("a > b")
elif a<b:
    print ("a < b")
elif a == b:
    print ("a == b")