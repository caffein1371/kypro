# ABC151
# 問題文
# z でない英小文字Cが与えられます。アルファベット順でCの次の文字を出力してください。

C = input()

tempnum= ord(C)
ans = chr(tempnum+1)
print (ans)