# ABC180
# 問題文
# N個のシュークリームがあります。
# シュークリームを分割することなく平等に分けることができるような人数としてあり得るものを全て求めてください。


def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

N = int(input())

anslist = sorted(divisor(N))

for i in range(len(anslist)):
  print (anslist[i])