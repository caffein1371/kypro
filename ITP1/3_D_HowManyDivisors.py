# 約数の数
# ３つの整数 a、b、cを読み込み、aからbまでの整数の中に、cの約数がいくつあるかを求めるプログラムを作成してください。

a,b,c = map(int,input().split())

count = 0
for i in range(a,b+1):
    if c%i ==0:
        count+=1
print (count)