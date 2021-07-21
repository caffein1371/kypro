# 数列の反転
# 与えられた数列を逆順に出力するプログラムを作成して下さい。

n = int(input())
alist = list(map(int,input().split()))
alist = alist[::-1]
for i in range(n):
    if i!=n-1:
        print ("{} ".format(alist[i]),end ="")
    else:
        print ("{}".format(alist[i]),end ="")
print ()