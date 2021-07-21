# 組み合わせの数
# 1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる組み合わせの数を求めるプログラムを作成して下さい。
# 例えば、1 から 5 までの数から３つを選んでそれらの合計が 9 となる組み合わせは、
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# の２通りがあります。

while(True):
  a,b = map(int,input().split())
  count = 0
  if a==0 and b ==0:
    break
  for i in range(1,a+1):
    for j in range(i+1,a+1):
      for k in range(j+1,a+1):
        if i+j+k==b:
          #print (i)
          #print (j)
          #print (k)
          count+=1
  print (count)