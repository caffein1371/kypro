S = input()
ans = []
ans.append(S)
for i in range(len(S)-1):
  S="".join((S[-1]+S[0:len(S)-1]))
  ans.append(S)
ans = sorted(ans)
print (ans[0])
print (ans[-1])