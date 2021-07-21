# 問題文
# 高橋君は500円玉をK枚持っています。 これらの総額がX円以上である場合は Yes を、そうでない場合は No を出力してください。

K,X = map(int,input().split())

if K*500>=X:
  print ('Yes')
else:
  print ('No')