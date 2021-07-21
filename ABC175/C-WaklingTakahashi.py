X,K,D =map(int,input().split())

X = abs(X)
#何回動くか
straight = min(K,X//D)

#あと何回動けるか
K -= straight
#最終的な位置
X -= straight *D

if K%2==0:
  print (X)
else:
  print (D-X)