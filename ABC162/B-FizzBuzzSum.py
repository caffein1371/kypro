# ABC162
# 問題文
# FizzBuzz列 a1,a2,...を次のように定めます。
# iが 3でも 5でも割り切れるなら、ai=FizzBuzz
# そうではなく iが 3で割り切れるなら、ai=Fizz
# そうではなく iが 5で割り切れるなら、ai=Buzz
# そうではないなら、ai=i
# FizzBuzz列の N項目までに含まれる数の和を求めてください。


N = int(input())

i = 1
sum = 0
while True:
  if i%3!=0 and i%5!=0:
    sum +=i
  i+=1
  if i==N+1:
    break
    
print (sum)