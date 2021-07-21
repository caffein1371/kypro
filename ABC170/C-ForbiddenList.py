# 問題文
# 整数 Xと、長さ Nの整数列 p1,…,pNが与えられます。
# 整数列 p1,…,pNに含まれない整数 (正とは限らない) のうち Xに最も近いもの、つまり Xとの差の絶対値が最小のものを求めてください。そのような整数が複数存在する場合は、そのうち最も小さいものを答えてください。

X,N = map(int,input().split())

min = 100

if N !=0:
  Plist = list(map(int,input().split()))
  anslist = [i for i in range(102)]
  anslist.append(-1)
  #anslist.remove(0)
  Plist = sorted(Plist)
  #print (anslist)
  for i in range(N):
    anslist.remove(Plist[i])
    temp =100
  for i in range(len(anslist)):
    if min >abs(anslist[i]-X) :
      min = abs(anslist[i]-X)
      temp = anslist[i]
  print (temp)
else :
  print (X)