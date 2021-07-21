N,A,B =map(int,input().split())

#AとBの差が奇数マスあればB（間が偶数マス），偶数であればAの勝利（間が奇数マス）

ans = B-A
if ans%2!=0:
  print ('Borys')
else:
  print ('Alice')