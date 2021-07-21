ABCD = input()
#3 隙間の数
num = len(ABCD)-1
ans = [['-']*num]
#print (ans)

pattern = []
for i in range(2**num):
  #an1 = []
  ans = ['-']*num
  #print("pattern {}: ".format(i), end="")
  for j in range(num):
    #2進数表記で各桁が１かどうかを判定する
    if (i>>j) &1:
      #an1.append(j)
      ans[j]='+'     
  #print (an1)
  #print (ans)
  pattern.append(ans)

#print (pattern)

for i in range(len(pattern)):
  #print (str(ABCD[0])+str(pattern[i][0])+str(ABCD[1])+str(pattern[i][1])+str(ABCD[2])+str(pattern[i][2])+str(ABCD[3]))
  #print (eval(ABCD[0]+pattern[i][0]+ABCD[1]+pattern[i][1]+ABCD[2]+pattern[i][2]+ABCD[3]))
  if eval(ABCD[0]+pattern[i][0]+ABCD[1]+pattern[i][1]+ABCD[2]+pattern[i][2]+ABCD[3])==7:
    print (str(ABCD[0])+str(pattern[i][0])+str(ABCD[1])+str(pattern[i][1])+str(ABCD[2])+str(pattern[i][2])+str(ABCD[3])+'=7')
    break