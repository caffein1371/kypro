N = int(input())
S = input()

anslist = []
for i in range(0,N):
  if i==0:
    anslist.append(S[i])
  if anslist[-1]!=S[i]:
    anslist.append(S[i])
print (len(anslist))