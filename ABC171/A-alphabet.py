# ABC171
# 問題文
# 英大文字か英小文字のいずれか 
# 1文字 αが入力されます。αが英大文字なら A、英小文字なら a と出力してください。
alpha = input()

if alpha.islower():
  print('a')
else :
  print('A')