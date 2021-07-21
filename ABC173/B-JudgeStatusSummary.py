# ABC173
# 問題文
# 高橋君は、プログラミングコンテスト AXC002 に参加しており、問題 A にコードを提出しました。
# この問題には # N個のテストケースがあります。
# 各テストケース i(1≤i≤N) について、ジャッジ結果を表す文字列 Si
#  が与えられるので、ジャッジ結果が AC, WA, TLE, RE であったものの個数をそれぞれ求めてください。
# 出力形式は、出力欄を参照してください。


N = int(input())

AC = []
WA = []
TLE = []
RE = []
for i in range(N):
  inp = input()
  if inp == "AC":
  	AC.append(1)
  elif inp == "WA":
    WA.append(1)
  elif inp == "TLE":
    TLE.append(1)
  elif inp == "RE":
    RE.append(1)
  
  
print ("AC x {}".format(len(AC)))
print ("WA x {}".format(len(WA)))
print ("TLE x {}".format(len(TLE)))
print ("RE x {}".format(len(RE)))