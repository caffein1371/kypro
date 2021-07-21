# 最小値、最大値、合計値
# n個の整数 ai(i=1,2,...n)を入力し、それらの最小値、最大値、合計値を求めるプログラムを作成してください。

n = int(input())
anslist = list(map(int,input().split()))
print ("{} {} {}".format(min(anslist),max(anslist),sum(anslist)))