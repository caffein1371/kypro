# ABC159
# 問題文
# 長さが奇数である文字列 
# Sが以下の条件をすべて満たすとき、
# Sは「強い回文」であるといいます。
# Sは回文である。Nを Sの長さとするとき、Sの 1文字目から (N−1)/2文字目まで(両端含む)からなる文字列は回文である。
# Sの (N+3)/2文字目からN文字目まで(両端含む)からなる文字列は回文である。
# Sが強い回文かどうかを判定してください。

S = input()

#print ((len(S)-1)//2)
#print ((len(S)+3)//2)
#print (S[0:(len(S)-1)//2])
#print (S[((len(S)+3)//2)-1:len(S)])
#print (S[::-1])

Skai1 = S[0:(len(S)-1)//2]
Skai1 = Skai1[::-1]
Skai2 = S[((len(S)+3)//2)-1:len(S)]
Skai2 = Skai2[::-1]

if S==S[::-1] and S[0:(len(S)-1)//2] ==Skai1 and S[((len(S)+3)//2)-1:len(S)] == Skai2: 
  print('Yes')
else:
  print("No")