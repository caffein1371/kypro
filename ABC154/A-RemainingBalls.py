# ABC154
# 問題文
# 文字列Sの書かれたボールがA個、文字列 Tの書かれたボールがB個あります。
# 高橋君は、文字列 Uの書かれたボールを1個選んで捨てました。文字列 S,Tの書かれたボールがそれぞれ何個残っているか求めてください。

S,T = input().split()
A,B = map(int,input().split())
U = input()

if U ==S:
  A-=1
elif U ==T:
  B-=1
print ('{} {}'.format(A,B))