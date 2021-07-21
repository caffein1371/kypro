# ABC166
# 問題文
# ある街に、N人のすぬけ君(すぬけ君 1、すぬけ君2、 ...、 すぬけ君 N)が住んでいます。
# この街には、 K種類のお菓子(お菓子 1、 お菓子 2 、....、お菓子 K)が売られています。お菓子 iを持っているのは、すぬけ君 Ai,1,Ai,2,⋯,Ai,diの計 di人です。
# 高橋君は今からこの街を回り、お菓子を 1つも持っていないすぬけ君にいたずらをします。このとき、何人のすぬけ君がいたずらを受けるでしょうか。

N,K = map(int,input().split())

sunuke = [0]*(N+1)
for i in range(K):
  okashi_category = input()
  #print (okashi_category)
  if okashi_category ==1:
    sunuke[input()]=1
  else:
    sunukelist = list(map(int,input().split()))
    for j in range(len(sunukelist)):
      #print(sunukelist[j])
      sunuke[sunukelist[j]]=1

print (N-sum(sunuke))