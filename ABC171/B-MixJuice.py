#ABC171
# 問題文
# ある店で N種類の果物、果物 1,…,N が売られており、それぞれの価格は一個あたり p1,…,pN円です。
# この店で K種類の果物を一個ずつ買うとき、それらの合計価格として考えられる最小の金額を求めてください。

N,K = map(int,input().split())
plist = list(map(int,input().split()))

plist.sort()
sum = 0
for i in range(K):
  sum+=plist[i]
print (sum)