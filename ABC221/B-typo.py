S = list(input())
T = list(input())
ans = "No"
if S==T:
  ans = "Yes"
for i in range(len(S)-1):
  S[i],S[i+1]=S[i+1],S[i]
  if S==T:
    ans= "Yes"
  S[i],S[i+1]=S[i+1],S[i]
print (ans)