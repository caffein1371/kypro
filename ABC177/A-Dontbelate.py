# ABC177
# 問題文
# 高橋君は青木君と待ち合わせをしています。
# 待ち合わせ場所は高橋君の家からDメートル離れた地点であり、待ち合わせの時刻はT分後です。
# 高橋君は今から家を出発し、分速Sメートルで待ち合わせ場所までまっすぐ移動します。
# 待ち合わせに間に合うでしょうか？


D,T,S = map(int,input().split())
 
if D/S<=T:
  print ("Yes")
else :
  print ("No")