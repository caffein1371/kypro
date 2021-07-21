# ABC153
# 問題文
# フェネックはN体のモンスターと戦っています。
# i番目のモンスターの体力はHiです。

# フェネックは次の 2種類の行動を行うことができます。
# 攻撃：モンスターを 1体選んで攻撃することで、そのモンスターの体力を1減らす
# 必殺技：モンスターを1体選んで必殺技を使うことで、そのモンスターの体力を0にする
# 攻撃と必殺技以外の方法でモンスターの体力を減らすことはできません。
# 全てのモンスターの体力を0以下にすればフェネックの勝ちです。
# フェネックが K回まで必殺技を使えるとき、モンスターに勝つまでに行う攻撃の回数 (必殺技は数えません) の最小値を求めてください。

N,K = map(int,input().split())
Hlist = list(map(int,input().split()))

Hlist = sorted(Hlist,reverse = True)
#print (Hlist)

if len(Hlist)>=K and K!=0:
  del Hlist[0:K]
elif len(Hlist)<K:
  del Hlist[0:len(Hlist)]

if len(Hlist)>0:
  print (sum(Hlist))
else:
  print (len(Hlist))
