# ABC166
# 問題文
# AtCoder丘陵にはN個の展望台があり、展望台 iの標高は Hiです。 また、異なる展望台どうしを結ぶ M本の道があり、道 jは展望台 Ajと展望台 Bjを結んでいます。
# 展望台iが良い展望台であるとは、展望台 iから一本の道を使って辿り着けるどの展望台よりも展望台 iの方が標高が高いことをいいます。 
# 展望台iから一本の道を使って辿り着ける展望台が存在しない場合も、展望台 iは良い展望台であるといいます。良い展望台がいくつあるか求めてください。

N,M = map(int,input().split())
Hlist = list(map(int,input().split()))

anslist = [1]*N
for i in range(M):
  A,B = map(int,input().split())
  #print (Hlist[A-1])
  #print (Hlist[B-1])
  if Hlist[A-1]<Hlist[B-1]:
    anslist[A-1]=0
  elif Hlist[A-1]>Hlist[B-1]:
    anslist[B-1]=0
  elif Hlist[A-1]==Hlist[B-1]:
    anslist[A-1]=0
    anslist[B-1]=0
    
#print (anslist)
print (sum(anslist))