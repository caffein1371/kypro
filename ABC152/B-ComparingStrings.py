# ABC152
# 問題文
# 1桁の正整数a,bが与えられます。整数aをb回繰り返してできる文字列と 整数bをa回繰り返してできる文字列のうち、辞書順で小さい方を答えてください。


a,b = map(int,input().split())

ans =[]
ans.append(a)
ans.append(b)
ans = sorted(ans)

anser = ''
for i in range(ans[1]):
  anser+=str(ans[0])
  
print (anser)