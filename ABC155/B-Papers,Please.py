# ABC155
# 問題文
# あなたは AtCoder 王国の入国審査官です。入国者の書類にはいくつかの整数が書かれており、あなたの仕事はこれらが条件を満たすか判定することです。
# 規約では、次の条件を満たすとき、またその時に限り、入国を承認することになっています。
# 書類に書かれている整数のうち、偶数であるものは全て、3または 5で割り切れる。
# 上の規約に従うとき、書類にN個の整数A1,A2,…,ANが書かれた入国者を承認するならば APPROVED を、しないならば DENIED を出力してください。


N = int(input())
Alist = list(map(int,input().split()))

num = 0
for i in range(N):
  if Alist[i]%2==0:
    num+=1
    #print (Alist[i])
    if Alist[i]%3==0 or Alist[i]%5==0:
      num-=1
      
if num==0:
  print ('APPROVED')
else :
  print ('DENIED')